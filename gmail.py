import json
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import keyring

INVOICE_AUTOMATOR_TOKEN_KEY = "SerraICTInvoiceAutomatorToken"
SYSTEM_NAME = "Serra ICT Invoice Automator"


def build_service(scopes):
    creds = None
    token = keyring.get_password(SYSTEM_NAME, INVOICE_AUTOMATOR_TOKEN_KEY)
    if token:
        token_json = json.loads(token)
        creds = Credentials.from_authorized_user_info(token_json, scopes)

    # If there are no (valid) credentials available, let the user log in.
    # This is necessary because we are using email on behalf of an actual human.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes)
            creds = flow.run_local_server(port=0)
        keyring.set_password(SYSTEM_NAME, INVOICE_AUTOMATOR_TOKEN_KEY, creds.to_json())

    return build("gmail", "v1", credentials=creds)
