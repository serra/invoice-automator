import base64
import os

from decimal import Decimal

from .template_helpers import get_template, round_amount
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration

from py_epc_qr.transaction import consumer_epc_qr


# check dest_dir
dest_dir = os.environ.get("INVOICE_DESTINATION_FOLDER", "./output")
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)


options = {
    "page-size": "A4",
    "footer-html": "style/footer.html",
    "header-html": "style/header.html",
}

stylesheets = [
    "style/css/invoice.css",
    "style/css/bootstrap.css",
    "style/css/style.css",
]

# An EPC payment QR code can only hold an amount within these bounds,
# see py_epc_qr.checks.check_amount.
MIN_QR_AMOUNT = Decimal("0.01")
MAX_QR_AMOUNT = Decimal("999999999.99")


def generate(invoice):
    png_base64_encode_qr_image = generate_qr_code(invoice)

    template = get_template("invoice.html")
    html = HTML(
        string=template.render(
            invoice=invoice,
            png_base64_encode_qr_image=png_base64_encode_qr_image,
            png_base64_encode_logo=get_logo_as_base64(),
        )
    )
    invoice_path = os.path.join(dest_dir, f"serra_ict_{invoice['invoiceNumber']}.pdf")
    html.write_pdf(
        invoice_path, stylesheets=stylesheets, font_config=FontConfiguration()
    )
    return invoice_path


def payable_amount(invoice):
    """Returns the amount to pay, rounded to cents the same way the invoice
    shows it, or None when it does not fit on a payment QR code."""
    amount = round_amount(invoice["totalIncludingVat"])
    if not MIN_QR_AMOUNT <= amount <= MAX_QR_AMOUNT:
        return None
    return amount


def generate_qr_code(invoice):
    """Returns a payment QR code for the invoice, or None when there is
    nothing to pay, as is the case for a credit note."""
    nr = invoice["invoiceNumber"]
    amount = payable_amount(invoice)
    if amount is None:
        print("no payment QR code ...", end=" ")
        return None
    qr_code_path = os.path.join(dest_dir, f"serra_ict_qr_for_{nr}.png")
    epc_qr = consumer_epc_qr(
        beneficiary="Serra ICT Diensten",
        iban="NL97ADYB1000003119",
        amount=f"{amount:.2f}",
        remittance=remittance_for_invoice(invoice),
    )
    epc_qr.to_qr(file_name=qr_code_path)

    return embed_image_as_base64(qr_code_path)


def embed_image_as_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


def remittance_for_invoice(invoice):
    nr = invoice["invoiceNumber"]
    remittance = f"F{nr}"
    remittance = "".join([c for c in remittance if c.isalnum()])
    return remittance


logo = embed_image_as_base64("style/img/logo.png")


def get_logo_as_base64():
    return logo
