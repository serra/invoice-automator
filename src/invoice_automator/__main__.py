import click
from .fibery import InvoiceClient, FileClient
from .pdf_generator import generate
from .email_generator import email_message_for_invoice
from .gmail import create_draft_email
from .moneybird import ExternalInvoiceClient, from_fibery_invoice


state_filter = "Ready"
invoice_client = None
file_client = None


@click.group()
@click.version_option()
@click.option("--url", envvar="SPACE_URL", help="Fibery Space URL")
@click.option("--file-url", envvar="FIBERY_FILE_URL", help="Fibery Space URL")
@click.option(
    "--command-url", envvar="FIBERY_COMMAND_URL", help="Fibery Command API URL"
)
@click.option("--state", default="Ready", help="Invoice state filter")
def cli(url, file_url, command_url, state):
    global invoice_client
    invoice_client = InvoiceClient(url, command_url)
    global file_client
    file_client = FileClient(file_url, command_url)
    global state_filter
    state_filter = state


@cli.command(help="List invoices.", name="list")
def list_invoices():
    invoice_data = invoice_client.get_invoices(state_filter)
    for invoice in invoice_data:
        print(
            f"Invoice #{invoice['invoiceNumber']} of €{invoice['totalAmount']:.2f} for {invoice['customerName']}"
        )


@cli.command(help="Generate PDF for invoices.", name="gen")
def generate_pdf_for_invoices():
    invoice_data = invoice_client.get_invoices(state_filter)
    for invoice in invoice_data:
        print(f"Generating PDF for invoice #{invoice['invoiceNumber']} ...", end=" ")
        generate(invoice)
        print(f"done.")


@cli.command(
    help="Attach nice pdf file to all filtered invoices in Fibery.",
    name="email",
)
# add flag to send emails directly using gmail API
@click.option(
    "--use-gmail",
    is_flag=True,
    default=False,
    help="Send emails directly using Gmail API.",
)
def prepare_emails_for_invoices(use_gmail=False):
    invoice_data = invoice_client.get_invoices(state_filter)
    for invoice in invoice_data:
        print(f"Generating PDF for invoice #{invoice['invoiceNumber']} ...", end=" ")
        filename = generate(invoice)
        if use_gmail:
            print(f"saving draft email ...", end=" ")
            msg = email_message_for_invoice(invoice, filename)
            create_draft_email(msg)
        print("uploading to Fibery ...", end=" ")
        file_client.upload_and_attach(filename, invoice["id"])
        invoice_client.set_state_to_review(invoice["id"])
        print(f"done.")


@cli.command(help="Save invoices to MoneyBird.", name="admin")
@click.option(
    "--money-bird-base-url",
    envvar="MONEY_BIRD_BASE_URL",
    help="MoneyBird administration base URL.",
)
def administrate_invoices(money_bird_base_url):
    invoice_data = invoice_client.get_invoices("Sent")
    mb = ExternalInvoiceClient(money_bird_base_url)
    for invoice in invoice_data:
        print(f"Saving invoice #{invoice['invoiceNumber']} to MoneyBird ...", end=" ")
        contact_id = mb.get_or_create_contact_id(invoice["customerName"])
        mb_invoice = from_fibery_invoice(invoice)
        mb_invoice["contact_id"] = contact_id
        result = mb.create_invoice(mb_invoice)
        print(f"done: {result['id']}.")


if __name__ == "__main__":
    cli()
