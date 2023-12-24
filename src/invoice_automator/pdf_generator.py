import os

from .template_helpers import get_template
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

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
    "style/css/invoice.css",
    "style/css/bootstrap.css",
    "style/css/style.css",
]


def generate(invoice):
    template = get_template("invoice.html")
    html = HTML(string=template.render(invoice=invoice))
    invoice_path = os.path.join(dest_dir, f"serra_ict_{invoice['invoiceNumber']}.pdf")
    html.write_pdf(
        invoice_path, stylesheets=stylesheets, font_config=FontConfiguration()
    )
    return invoice_path
