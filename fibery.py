import requests

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
        vat
        vatPercentage
        totalIncludingVat
        invoiceLines {
          name
          quantity
          unitPrice
          totalPrice
        }
      }
    }
    """


class InvoiceClient:
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
