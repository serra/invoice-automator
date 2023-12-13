import json
import os
import requests
import keyring

invoice_query = """
    {
      findInvoices(state: {name: {is: "%s"}}) {
        id
        publicId
        name
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
          timeLogs {
            name
            date
            timeSpent
          }
        }
        files {
          name
          contentType
        }
      }
    }
    """

INVOICE_AUTOMATOR_TOKEN_KEY = "SerraICTInvoiceAutomatorFiberyToken"
SYSTEM_NAME = "Serra ICT Invoice Automator"


def get_token():
    token = keyring.get_password(SYSTEM_NAME, INVOICE_AUTOMATOR_TOKEN_KEY)
    if not token:
        raise Exception(
            f"Fibery API Token not found in keyring. "
            + "Please add the token to your platform's keyring "
            + f"with system name '{SYSTEM_NAME}' "
            + f"and key '{INVOICE_AUTOMATOR_TOKEN_KEY}'. "
        )
    return token


class InvoiceClient:
    def __init__(self, url):
        self.url = url
        self.token = get_token()

    def get_invoices(self, state):
        query = invoice_query % state

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Token " + self.token,
        }

        response = requests.post(self.url, json={"query": query}, headers=headers)
        return response.json()["data"]["findInvoices"]


class FileClient:
    def __init__(self, file_url, command_url):
        self.url = file_url
        self.command_url = command_url
        self.token = get_token()

    def upload_file(self, path):
        headers = {
            "Authorization": "Token " + self.token,
        }
        with open(path, "rb") as f:
            response = requests.post(
                self.url,
                headers=headers,
                files={"file": (os.path.basename(path), f, "application/pdf")},
            )

        return response.json()["fibery/id"]

    def attach_file_to_entity(self, file_id, entity_id):
        command = {
            "command": "fibery.entity/add-collection-items",
            "args": {
                "type": "Sales/Invoice",
                "field": "Files/Files",
                "entity": {"fibery/id": entity_id},
                "items": [{"fibery/id": file_id}],
            },
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Token " + self.token,
        }

        response = requests.post(self.command_url, json=[command], headers=headers)

    def upload_and_attach(self, path, entity_id):
        file_id = self.upload_file(path)
        self.attach_file_to_entity(file_id, entity_id)
