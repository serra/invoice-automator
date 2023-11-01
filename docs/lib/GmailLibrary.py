from invoice_automator import gmail


class GmailLibrary:
    def __init__(self):
        pass

    def can_load_gmail_client_secrets(self):
        gmail.get_client_secrets()

    def the_invoices_emails_are_in_the_drafts_folder_with_pdf_invoices_as_attachments(
        self,
    ):
        # for now, verify this using visual inspection
        pass
