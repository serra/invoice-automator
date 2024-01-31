from invoice_automator.moneybird import from_fibery_invoice
from .pdf_generator import generate


def attach_pdf_files_to_invoices(invoice_client, file_client, state_filter):
    invoice_data = invoice_client.get_invoices(state_filter)
    for invoice in invoice_data:
        attach_pdf_files_to_invoice(invoice_client, file_client, invoice)


def attach_pdf_files_to_invoice_by_id(invoice_client, file_client, invoice_id):
    invoice = invoice_client.get_invoice_by_id(invoice_id)
    attach_pdf_files_to_invoice(invoice_client, file_client, invoice)


def attach_pdf_files_to_invoice(invoice_client, file_client, invoice):
    print(f"Generating PDF for invoice #{invoice['invoiceNumber']} ...", end=" ")
    filename = generate(invoice)
    print("uploading to Fibery ...", end=" ")
    file_client.upload_and_attach(filename, invoice["id"])
    invoice_client.set_state_to_review(invoice["id"])
    print(f"done.")


def save_invoice_to_moneybird_by_id(invoice_client, money_bird_client, invoice_id):
    invoice = invoice_client.get_invoice_by_id(invoice_id)
    save_invoice_to_moneybird(invoice, money_bird_client)

def save_invoice_to_moneybird(invoice, money_bird_client):
    contact_id = money_bird_client.get_or_create_contact_id(invoice["customerName"])
    mb_invoice = from_fibery_invoice(invoice)
    mb_invoice["contact_id"] = contact_id
    result = money_bird_client.create_invoice(mb_invoice)
    return result
