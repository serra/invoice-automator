import os
import click
from fibery import InvoiceClient
from pdf_generator import generate


@click.group()
@click.option("--url", envvar="SPACE_URL", help="Fibery Space URL")
@click.option("--token", envvar="FIBERY_API_TOKEN", help="Fibery API Token")
@click.pass_context
def cli(ctx, url, token):
    ctx.ensure_object(dict)
    ctx.obj["client"] = InvoiceClient(url, token)


@cli.command()
@click.option("--state", default="Ready", help="List invoices by invoice state")
@click.pass_context
def list_invoices(ctx, state):
    client = ctx.obj["client"]
    invoice_data = client.get_invoices(state)
    for invoice in invoice_data:
        print(
            f"Invoice #{invoice['invoiceNumber']} of €{invoice['totalAmount']:.2f} for {invoice['customerName']} is {state}"
        )


@cli.command()
@click.option(
    "--state", default="Ready", help="Generate PDF for invoices by invoice state"
)
@click.pass_context
def generate_pdf_for_invoices(ctx, state):
    client = ctx.obj["client"]
    invoice_data = client.get_invoices(state)
    for invoice in invoice_data:
        print(f"Generating PDF for invoice #{invoice['invoiceNumber']} ...")
        generate(invoice)
        print(f"Done.")


if __name__ == "__main__":
    cli(obj={})
