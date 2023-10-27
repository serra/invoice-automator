from invoice_automator import gmail


class GmailLibrary:
    def __init__(self):
        pass

    def can_load_gmail_client_secrets(self):
        gmail.get_client_secrets()
