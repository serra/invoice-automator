from gmail import build_service
from googleapiclient.errors import HttpError
import base64
from email.message import EmailMessage

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.compose",
]


def main():
    try:
        msg = EmailMessage()
        msg["Subject"] = "Test email"
        msg["From"] = "info@serraict.com"
        msg["To"] = "marijn.vanderzee@gmail.com"
        msg.set_content("This is a test email")
        msg.add_attachment(
            open("./bin/serra_ict_2023-1.pdf", "rb").read(),
            maintype="application",
            subtype="pdf",
            filename="test.pdf",
        )

        encoded_message = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        create_message = {"message": {"raw": encoded_message}}

        service = build_service(SCOPES)
        service.users().drafts().create(userId="me", body=create_message).execute()

        # add an attachment to the message

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
