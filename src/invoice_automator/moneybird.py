import keyring
import requests

INVOICE_AUTOMATOR_MONEY_BIRD_TOKEN_KEY = "SerraICTInvoiceAutomatorMoneyBirdToken"
SYSTEM_NAME = "Serra ICT Invoice Automator"
MONEY_BIRD_ADMINISTRATION_ID = "406911143627458262"
MONEY_BIRD_BASE_URL = f"https://moneybird.com/api/v2/{MONEY_BIRD_ADMINISTRATION_ID}/"


def from_fibery_invoice(fibery_invoice: dict):
    fi = fibery_invoice
    return {
        "reference": fi["invoiceNumber"],
        # "invoice_date": fibery_invoice["invoiceDate"],
        # "due_date": fibery_invoice["dueDate"],
        # "state": "draft",
        # "currency": "EUR",
        # "prices_are_incl_tax": True,
        # "discount": 0,
        # "discount_type": "percentage",
        # "invoice_lines": [
        #     {
        #         "description": fibery_invoice["description"],
        #         "price": fibery_invoice["totalAmount"],
        #         "tax_rate_id": fibery_invoice["taxRate"]["id"],
        #         "quantity": 1,
        #     }
        # ],
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

    def create_invoice(self, invoice):
        mb_external_invoice = from_fibery_invoice(invoice)

        response = requests.post(
            self.base_url + "/external_sales_invoice",
            json=invoice,
            headers=self.headers,
        )
        return response.json()
