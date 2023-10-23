import os
import click
import requests
from pdf_generator import generate

invoice_query = """
    {
      findInvoices(state: {name: {is: "%s"}}) {
        invoiceNumber
        customerReference
        customerName
        customerEmail
        customerAddress
        customerZipcode
        customerCity
        invoiceDate
        dueDate
        totalAmount
        invoiceLines {
          name
          quantity
          unitPrice
          totalPrice
        }
      }
    }
    """


class Client:
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def get_invoices(self, state):
        query = invoice_query % state

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Token " + self.token,
        }

        response = requests.post(self.url, json={"query": query}, headers=headers)
        return response.json()["data"]["findInvoices"]

    def sum_invoices(self, state):
        invoices = self.get_invoices(state)
        total_amount = sum([invoice["totalAmount"] for invoice in invoices])
        return total_amount


@click.group()
@click.option("--url", envvar="SPACE_URL", help="Fibery Space URL")
@click.option("--token", envvar="FIBERY_API_TOKEN", help="Fibery API Token")
@click.pass_context
def cli(ctx, url, token):
    ctx.ensure_object(dict)
    ctx.obj["client"] = Client(url, token)


@cli.command()
@click.option("--state", default="Ready", help="Filter invoices by state")
@click.pass_context
def list_invoices(ctx, state):
    client = ctx.obj["client"]
    invoice_data = client.get_invoices(state)
    for invoice in invoice_data:
        print(
            f"Invoice #{invoice['invoiceNumber']} of {invoice['totalAmount']} for {invoice['customerName']} is {state}"
        )


@cli.command()
@click.option("--state", default="Ready", help="Filter invoices by state")
@click.pass_context
def generate_pdf_for_invoices(ctx, state):
    client = ctx.obj["client"]
    invoice_data = client.get_invoices(state)
    for invoice in invoice_data:
        print(f"Generating PDF for invoice #{invoice['invoiceNumber']} ...")
        print(f"Done.")


if __name__ == "__main__":
    cli(obj={})
