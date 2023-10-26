import click
from fibery import InvoiceClient
from pdf_generator import generate
from email_generator import email_message_for_invoice
from gmail import create_draft_email


state_filter = "Ready"
invoice_client = None


@click.group()
@click.option("--url", envvar="SPACE_URL", help="Fibery Space URL")
@click.option("--state", default="Ready", help="Invoice state filter")
def cli(url, state):
    global invoice_client
    invoice_client = InvoiceClient(url)
    global state_filter
    state_filter = state


@cli.command(help="List invoices.")
def list_invoices():
    invoice_data = invoice_client.get_invoices(state_filter)
    for invoice in invoice_data:
        print(
            f"Invoice #{invoice['invoiceNumber']} of €{invoice['totalAmount']:.2f} for {invoice['customerName']}"
        )


@cli.command(help="Generate PDF for invoices.")
def generate_pdf_for_invoices():
    invoice_data = invoice_client.get_invoices(state_filter)
    for invoice in invoice_data:
        print(f"Generating PDF for invoice #{invoice['invoiceNumber']} ...", end=" ")
        generate(invoice)
        print(f"done.")


@cli.command(
    help="Prepare email for each invoice. Emails are not sent, but saved as draft."
)
def prepare_emails_for_invoices():
    invoice_data = invoice_client.get_invoices(state_filter)
    for invoice in invoice_data:
        print(f"Generating PDF for invoice #{invoice['invoiceNumber']} ...", end=" ")
        filename = generate(invoice)
        print(f"saving draft ...", end=" ")
        msg = email_message_for_invoice(invoice, filename)
        create_draft_email(msg)
        print(f"done.")


if __name__ == "__main__":
    cli()
