from .pdf_generator import generate


def attach_pdf_files_to_invoices(invoice_client, file_client, state_filter):
    invoice_data = invoice_client.get_invoices(state_filter)
    for invoice in invoice_data:
        print(f"Generating PDF for invoice #{invoice['invoiceNumber']} ...", end=" ")
        filename = generate(invoice)
        print("uploading to Fibery ...", end=" ")
        file_client.upload_and_attach(filename, invoice["id"])
        invoice_client.set_state_to_review(invoice["id"])
        print(f"done.")
    pass
