from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader

def email_body_for_invoice(invoice):
    return f""


def email_message_for_invoice(invoice, filename):
    msg = EmailMessage()
    msg["Subject"] = f"Invoice #{invoice['invoiceNumber']} from Serra ICT Diensten"
    msg["From"] = "marijn@serraict.com"
    msg["To"] = invoice["customerEmail"]
    msg.set_content(
        f"Dear {invoice['customerName']},\n\nPlease find attached invoice #{invoice['invoiceNumber']}.\n\nBest regards,\nMarijn van der Zee"
    )
    msg.add_attachment(
        open(filename, "rb").read(),
        maintype="application",
        subtype="pdf",
        filename=f"Invoice_{invoice['invoiceNumber']}.pdf",
    )
    return msg
