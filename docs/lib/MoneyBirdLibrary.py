from invoice_automator.moneybird import ExternalInvoiceClient


class MoneyBirdLibrary:
    def __init__(self):
        pass

    def the_invoices_in_the_sent_column_in_fibery_are_stored_as_an_external_invoice_in_moneybird(
        self,
    ):
        client = ExternalInvoiceClient()
        invoices = client.get_invoices()

        for inv in invoices:
            ref = inv["reference"]
            assert ref.startswith(
                "serra_ict"
            ), "Invoice reference should start with 'serra_ict'"

            assert ref.split("-")[-1].isdigit(), (
                "Invoice reference should end with a dash and a number, "
                + "but was "
                + ref
            )

            assert inv["date"] is not None, "Invoice date should be filled"
