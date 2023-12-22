import os
from invoice_automator import fibery
from robot.api import ContinuableFailure


class FiberyLibrary:
    def __init__(self):
        self.url = os.environ["SPACE_URL"]
        cmd_url = os.environ["FIBERY_COMMAND_URL"]
        self.client = fibery.InvoiceClient(self.url, cmd_url)

    def Fibery_API_token_is_stored_in_credential_storage_to_access_invoices(self):
        # this will raise a clear exception
        # if the authorization token is not available or invalid
        invoices = self.client.get_invoices("Ready")

    def the_pdf_files_are_attached_to_the_invoice_entities_in_Fibery(self):
        invoices = self.client.get_invoices("Ready")
        for invoice in invoices:
            if not any(
                file["contentType"] == "application/pdf" for file in invoice["files"]
            ):
                raise ContinuableFailure(
                    f"Expected invoice {invoice['invoiceNumber']} to have a PDF file attached"
                )

    def the_invoices_are_moved_out_of_the_ready_column_in_Fibery(self):
        invoices = self.client.get_invoices("Ready")
        if len(invoices) > 0:
            raise ContinuableFailure(
                f"Expected all invoices to be moved out of the Ready column, but found {len(invoices)} still in Ready"
            )
