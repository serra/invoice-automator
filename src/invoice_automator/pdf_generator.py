import os

from .template_helpers import get_template
from pdfkit import from_string

# check dest_dir
dest_dir = os.environ.get("INVOICE_DESTINATION_FOLDER", "output")
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)


options = {
    "page-size": "A4",
    "footer-html": "style/footer.html",
    "header-html": "style/header.html",
}

stylesheets = [
    "style/css//invoice.css",
    "style/css/bootstrap.min.css",
    "style/css/style.css",
]


def generate(invoice):
    template = get_template("invoice.html")
    html = template.render(invoice=invoice)
    invoice_path = os.path.join(dest_dir, f"serra_ict_{invoice['invoiceNumber']}.pdf")
    pdf = from_string(html, invoice_path, options=options, css=stylesheets)
    return invoice_path
