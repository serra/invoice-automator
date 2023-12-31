import os
import requests

INVOICE_AUTOMATOR_MONEY_BIRD_TOKEN_KEY = "MoneyBirdToken"
SYSTEM_NAME = "Serra_ICT_Invoice _Automator_"


def from_fibery_invoice(fibery_invoice: dict):
    fi = fibery_invoice
    return {
        "reference": fi["invoiceNumber"],
        "date": fibery_invoice["invoiceDate"],
        "due_date": fibery_invoice["dueDate"],
        "currency": "EUR",
        "source": "Fibery",
        "source_url": f"https://serra.fibery.io/Sales/Invoice/{fi['publicId']}",
        "details_attributes": [
            {
                "description": fi["name"],
                "price": fi["totalAmount"],
                "amount": 1,
            }
        ],
        "prices_are_incl_tax": False,
    }


def get_token():
    token = os.getenv("MONEYBIRD_API_TOKEN")
    if not token:
        raise Exception(
            "MoneyBird's API Token not found in environment variables. "
            + "Please set the 'MONEYBIRD_API_TOKEN' environment variable."
        )
    return token


class ExternalInvoiceClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = get_token()
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "BEARER " + self.token,
        }

    def get_invoices(self):
        response = requests.get(
            self.base_url + +"/external_sales_invoices.json?", headers=self.headers
        )
        return response.json()

    def create_contact(self, contact_name):
        data = {"contact": {"company_name": contact_name}}
        response = requests.post(
            self.base_url + "/contacts.json", headers=self.headers, json=data
        )
        if response.status_code == 201:
            data = response.json()
            return data["id"]
        else:
            raise Exception(f"Failed to create MoneyBird contact: {response.text}")

    def get_or_create_contact_id(self, contact_name):
        response = requests.get(
            self.base_url + "/contacts.json?query=" + contact_name, headers=self.headers
        )
        if response.status_code == 200:
            # the contact exists, so use it:
            data = response.json()
            if len(data) > 0:
                return data[0]["id"]

        return self.create_contact(contact_name)

    def create_invoice(self, mb_external_invoice):
        data = {"external_sales_invoice": mb_external_invoice}
        response = requests.post(
            self.base_url + "/external_sales_invoices",
            headers=self.headers,
            json=data,
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to create MoneyBird invoice: {response.text}")
