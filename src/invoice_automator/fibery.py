import requests
import keyring

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

INVOICE_AUTOMATOR_TOKEN_KEY = "SerraICTInvoiceAutomatorFiberyToken"
SYSTEM_NAME = "Serra ICT Invoice Automator"


class InvoiceClient:
    def __init__(self, url):
        self.url = url
        self.token = keyring.get_password(SYSTEM_NAME, INVOICE_AUTOMATOR_TOKEN_KEY)
        if not self.token:
            raise Exception(
                f"Fibery API Token not found in keyring. "
                + "Please add the token to your platform's keyring "
                + f"with system name '{SYSTEM_NAME}' "
                + f"and key '{INVOICE_AUTOMATOR_TOKEN_KEY}'. "
            )

    def get_invoices(self, state):
        query = invoice_query % state

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Token " + self.token,
        }

        response = requests.post(self.url, json={"query": query}, headers=headers)
        return response.json()["data"]["findInvoices"]
