import os
import requests

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

INVOICE_AUTOMATOR_TOKEN_KEY = "FIBERY_API_TOKEN"
REVIEW_STATE_ID = "5e42d1c0-74a4-11ee-8870-33f30b17590d"
READY_STATE_ID = "a69f6220-6811-11ee-9c7a-0bc3e2dc4277"


def get_token():
    token = os.getenv("FIBERY_API_TOKEN")
    if not token:
        raise Exception(
            "Fibery API Token not found in the environment variables. "
            + "Please add the 'FIBERY_API_TOKEN' to your environment variables."
        )
    return token


class InvoiceClient:
    def __init__(self, url, command_url):
        self.url = url
        self.command_url = command_url
        self.token = get_token()
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Token " + self.token,
        }

    def get_invoices(self, state):
        query = invoice_query % state

        response = requests.post(self.url, json={"query": query}, headers=self.headers)
        if response.status_code != 200:
            raise Exception(
                f"Failed to query for invoices: {response.text} - token: {self.token}"
            )
        return response.json()["data"]["findInvoices"]

    def set_state_to_review(self, invoice_id):
        command = {
            "command": "fibery.entity/update",
            "args": {
                "type": "Sales/Invoice",
                "entity": {
                    "fibery/id": invoice_id,
                    "workflow/state": {
                        "fibery/id": REVIEW_STATE_ID,
                    },
                },
            },
        }
        response = requests.post(self.command_url, json=[command], headers=self.headers)
        if response.status_code != 200:
            raise Exception(
                f"Failed to set state of invoice {invoice_id} to review: {response.text}"
            )


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


def id_for_invoice_with_state_changed_to_ready(data):
    for effect in data["effects"]:
        if (
            effect["effect"] == "fibery.entity/update"
            and effect["type"] == "Sales/Invoice"
            # in case of a delete, this might be empty, so we have to explicitly check:
            and effect["values"].get("workflow/state")
            and effect["values"].get("workflow/state", {}).get("fibery/id")
            == READY_STATE_ID
        ):
            return effect["id"]

    return None
