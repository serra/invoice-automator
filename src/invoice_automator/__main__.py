import click
import uvicorn


# logging configuration
import logging
import logging.config

try:
    logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)
except:
    logging.basicConfig(level=logging.WARN)
    logging.warning(
        "Could not open 'logging.conf'; falling back to basic logging configuration"
    )


from .commands import attach_pdf_files_to_invoices, save_invoice_to_moneybird

from .fibery import InvoiceClient, FileClient
from .pdf_generator import generate
from .moneybird import ExternalInvoiceClient, from_fibery_invoice

state_filter = "Ready"
invoice_client = None
file_client = None


@click.group()
@click.version_option()
@click.option("--url", envvar="SPACE_URL", help="Fibery Space URL")
@click.option("--file-url", envvar="FIBERY_FILE_URL", help="Fibery File URL")
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
    name="attach",
)
def prepare_emails_for_invoices():
    attach_pdf_files_to_invoices(invoice_client, file_client, state_filter)


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
        result = save_invoice_to_moneybird(invoice, mb)
        print(f"done: {result['id']}.")


@cli.command(help="Start web app")
@click.option("--port", default=5000, help="Port to run web app on")
@click.option("--host", default="0.0.0.0", help="Host to run web app on")
def webapp(port: int, host: str):
    from .webapp import app

    uvicorn.run(app, port=port, host=host)


if __name__ == "__main__":
    cli()
