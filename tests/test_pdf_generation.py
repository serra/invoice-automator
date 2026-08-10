import json
import os
from invoice_automator.pdf_generator import (
    generate,
    generate_qr_code,
    payable_amount,
    remittance_for_invoice,
)
from invoice_automator.template_helpers import currency_format


def test_pdf_generation():
    invoice = json.load(open("tests/data/invoice_1.json"))
    invoice_path = generate(invoice)
    assert os.path.exists(invoice_path)


def test_pdf_generation_for_credit_note():
    """A credit note has nothing to pay, so it gets no payment QR code."""
    invoice = json.load(open("tests/data/invoice_1.json"))
    invoice["invoiceNumber"] = "2023-01-credit"
    for field in ("totalAmount", "vat", "totalIncludingVat"):
        invoice[field] = -invoice[field]

    assert generate_qr_code(invoice) is None

    invoice_path = generate(invoice)
    assert os.path.exists(invoice_path)


def test_payable_amount_is_rounded_like_the_invoice_total():
    """The QR code must ask for the amount the invoice shows, to the cent."""
    invoice = {"totalIncludingVat": 6972.625}

    assert f"{payable_amount(invoice):.2f}" == "6972.63"
    assert currency_format(invoice["totalIncludingVat"]) == "€ 6 972,63"


def test_no_payable_amount_when_there_is_nothing_to_pay():
    assert payable_amount({"totalIncludingVat": -395.97}) is None
    assert payable_amount({"totalIncludingVat": 0}) is None
    assert payable_amount({"totalIncludingVat": 0.004}) is None
    assert payable_amount({"totalIncludingVat": 1000000000}) is None


def test_remittance():
    invoice = json.load(open("tests/data/invoice_1.json"))
    remittance = remittance_for_invoice(invoice)
    assert (
        remittance.isalnum()
    ), f"Remittance should be alphanumeric, but is '{remittance}'."


def test_currency_format_rounding():
    """Test that currency formatting rounds correctly."""
    # Test the specific case mentioned: 6972.625 should round to €6972,63
    assert currency_format(6972.625) == "€ 6 972,63"

    # Test additional rounding cases
    assert currency_format(1234.565) == "€ 1 234,57"  # Round up
    assert currency_format(1234.564) == "€ 1 234,56"  # Round down
    assert currency_format(0.005) == "€ 0,01"  # Small value round up
    assert currency_format(0.004) == "€ 0,00"  # Small value round down

    # Test negative values
    assert currency_format(-42.625) == "€ -42,63"  # Negative round up

    # Test zero
    assert currency_format(0) == "€ 0,00"

    # Test with different currency symbol
    assert currency_format(123.45, symbol="$") == "$ 123,45"
