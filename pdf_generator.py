import os
from jinja2 import Environment, FileSystemLoader
from pdfkit import from_string

# check dest_dir
dest_dir = os.environ.get("INVOICE_DESTINATION_FOLDER", "bin")
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)


def currency_format(value, symbol="€"):
    try:
        money = "{:,.2f}".format(value)
        money = money.replace(",", " ").replace(".", ",")
        return f"{symbol} {money}"
    except (ValueError, TypeError):
        return value


# Load the Jinja2 template
env = Environment(loader=FileSystemLoader("templates"))
env.filters["currency"] = currency_format

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
    template = env.get_template("invoice.html")
    html = template.render(invoice=invoice)
    invoice_path = os.path.join(dest_dir, f"serra_ict_{invoice['invoiceNumber']}.pdf")
    pdf = from_string(html, invoice_path, options=options, css=stylesheets)
    return invoice_path
