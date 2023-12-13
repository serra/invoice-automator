import keyring
import requests

INVOICE_AUTOMATOR_MONEY_BIRD_TOKEN_KEY = "SerraICTInvoiceAutomatorMoneyBirdToken"
SYSTEM_NAME = "Serra ICT Invoice Automator"
MONEY_BIRD_ADMINISTRATION_ID = "406911143627458262"
MONEY_BIRD_BASE_URL = f"https://moneybird.com/api/v2/{MONEY_BIRD_ADMINISTRATION_ID}/"


def from_fibery_invoice(fibery_invoice: dict):
    fi = fibery_invoice
    return {
        "contact_id": 407113669141333734,  # TODO: map to MoneyBird contact
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
    token = keyring.get_password(SYSTEM_NAME, INVOICE_AUTOMATOR_MONEY_BIRD_TOKEN_KEY)
    if not token:
        raise Exception(
            f"MoneyBird's API Token not found in keyring. "
            + "Please add the token to your platform's keyring "
            + f"with system name '{SYSTEM_NAME}' "
            + f"and key '{INVOICE_AUTOMATOR_MONEY_BIRD_TOKEN_KEY}'. "
        )
    return token


class ExternalInvoiceClient:
    def __init__(self, base_url=MONEY_BIRD_BASE_URL):
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

    def create_invoice(self, mb_external_invoice):
        data = {"external_sales_invoice": mb_external_invoice}
        response = requests.post(
            self.base_url + "/external_sales_invoices",
            headers=self.headers,
            json=data,
        )
        print(response.text)
