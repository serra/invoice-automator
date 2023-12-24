import json
import os
from invoice_automator.pdf_generator import generate


def test_pdf_generation():
    invoice = json.load(open("tests/data/invoice_1.json"))
    invoice_path = generate(invoice)
    assert os.path.exists(invoice_path)
