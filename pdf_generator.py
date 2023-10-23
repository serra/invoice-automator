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


def generate(invoice):
    template = env.get_template("invoice.html")
    html = template.render(invoice=invoice)

    # Convert the HTML to a PDF using pdfkit
    pdf = from_string(html, False)
    invoice_path = os.path.join(dest_dir, f"serra_ict_{invoice['invoiceNumber']}.pdf")
    # Save the PDF to a file
    print(
        f"reference: {invoice['customerReference']} {invoice['customerReference'] is None}"
    )
    with open(invoice_path, "wb") as f:
        f.write(pdf)
