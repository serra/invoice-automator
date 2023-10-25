import click
from fibery import InvoiceClient
from pdf_generator import generate
from email_generator import email_message_for_invoice
from gmail import create_draft_email


@click.group()
@click.option("--url", envvar="SPACE_URL", help="Fibery Space URL")
@click.pass_context
def cli(ctx, url):
    ctx.ensure_object(dict)
    ctx.obj["client"] = InvoiceClient(url)


@cli.command(help="List invoices.")
@click.option("--state", default="Ready")
@click.pass_context
def list_invoices(ctx, state):
    client = ctx.obj["client"]
    invoice_data = client.get_invoices(state)
    for invoice in invoice_data:
        print(
            f"Invoice #{invoice['invoiceNumber']} of €{invoice['totalAmount']:.2f} for {invoice['customerName']} is {state}"
        )


@cli.command(help="Generate PDF for invoices.")
@click.option("--state", default="Ready")
@click.pass_context
def generate_pdf_for_invoices(ctx, state):
    client = ctx.obj["client"]
    invoice_data = client.get_invoices(state)
    for invoice in invoice_data:
        print(f"Generating PDF for invoice #{invoice['invoiceNumber']} ...")
        generate(invoice)
        print(f"Done.")


@cli.command(
    help="Prepare email for each invoice. Emails are not sent, but saved as draft."
)
@click.option("--state", default="Ready")
@click.pass_context
def prepare_emails_for_invoices(ctx, state):
    client = ctx.obj["client"]
    invoice_data = client.get_invoices(state)
    for invoice in invoice_data:
        print(f"Generating PDF for invoice #{invoice['invoiceNumber']} ...")
        filename = generate(invoice)
        print(f"Sending email for invoice #{invoice['invoiceNumber']} ...")
        msg = email_message_for_invoice(invoice, filename)
        create_draft_email(msg)
        print(f"Done.")


if __name__ == "__main__":
    cli(obj={})
