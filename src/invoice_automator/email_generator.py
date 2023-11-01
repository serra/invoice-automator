from email.message import EmailMessage
from .template_helpers import get_template


def email_body_for_invoice(invoice):
    template = get_template("email.txt")
    return template.render(invoice=invoice)


def email_message_for_invoice(invoice, filename):
    msg = EmailMessage()
    msg["Subject"] = f"Factuur #{invoice['invoiceNumber']} van Serra ICT Diensten"
    msg["From"] = "marijn@serraict.com"
    msg["To"] = invoice["customerEmail"]
    msg.set_content(email_body_for_invoice(invoice))

    with open(filename, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=f"Factuur_{invoice['invoiceNumber']}.pdf",
        )
    return msg
