import json
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import keyring
import base64


INVOICE_AUTOMATOR_CLIENT_SECRETS_KEY = "SerraICTInvoiceAutomatorGoogleClientSecrets"
INVOICE_AUTOMATOR_TOKEN_KEY = "SerraICTInvoiceAutomatorGoogleToken"
SYSTEM_NAME = "Serra ICT Invoice Automator"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.compose",
]


def get_client_secrets():
    client_secrets = keyring.get_password(
        SYSTEM_NAME, INVOICE_AUTOMATOR_CLIENT_SECRETS_KEY
    )
    if client_secrets:
        return json.loads(client_secrets)
    else:
        # raise exception if client secrets not found with system name and key
        raise Exception(
            f"Client secrets not found with system name '{SYSTEM_NAME}' "
            + f"and key '{INVOICE_AUTOMATOR_CLIENT_SECRETS_KEY}'. "
            + "Please add the client configuration in json format to your platform's keyring. "
            + "You can download the client configuration from https://console.cloud.google.com/apis/credentials. "
        )


def build_service(scopes=SCOPES):
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
            client_secrets = get_client_secrets()
            flow = InstalledAppFlow.from_client_config(client_secrets, scopes=scopes)
            creds = flow.run_local_server(port=0)
        keyring.set_password(SYSTEM_NAME, INVOICE_AUTOMATOR_TOKEN_KEY, creds.to_json())

    return build("gmail", "v1", credentials=creds)


def create_draft_email(message, service=build_service()):
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    create_message = {"message": {"raw": encoded_message}}
    service.users().drafts().create(userId="me", body=create_message).execute()
