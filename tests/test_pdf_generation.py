import json
import os
from invoice_automator.pdf_generator import generate, remittance_for_invoice


def test_pdf_generation():
    invoice = json.load(open("tests/data/invoice_1.json"))
    invoice_path = generate(invoice)
    assert os.path.exists(invoice_path)


def test_remittance():
    invoice = json.load(open("tests/data/invoice_1.json"))
    remittance = remittance_for_invoice(invoice)
    assert (
        remittance.isalnum()
    ), f"Remittance should be alphanumeric, but is '{remittance}'."
