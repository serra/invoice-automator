import os
from invoice_automator import fibery


class FiberyLibrary:
    def __init__(self):
        pass

    def Fibery_API_token_is_stored_in_credential_storage_to_access_invoices(self):
        url = os.environ["SPACE_URL"]
        # this will raise a clear exception
        # if the authorization token is not available or invalid
        self.client = fibery.InvoiceClient(url)
        invoices = self.client.get_invoices("Ready")
