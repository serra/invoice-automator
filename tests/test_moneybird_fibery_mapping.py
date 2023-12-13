from invoice_automator.moneybird import from_fibery_invoice

# generated from graphql query
example_fibery_invoice = {
    "id": "a_long_uuid",
    "publicId": "46",
    "name": "van Oord Datalab",
    "invoiceNumber": "2023-46",
    "customerReference": "Cust12345",
    "customerName": "John Doe",
    "customerEmail": "john.doe@example.com",
    "customerAddress": "123 ABC Street",
    "customerZipcode": "10001",
    "customerCity": "New York",
    "invoiceDate": "2023-11-30",
    "dueDate": "2023-12-14",
    "totalAmount": 500.00,
    "vat": 110.00,
    "vatPercentage": 21,
    "totalIncludingVat": 610.00,
    "invoiceLines": [
        {
            "name": "Product 1",
            "quantity": 2,
            "unitPrice": 250.00,
            "totalPrice": 500.00,
            "timeLogs": [
                {"name": "Time log 1", "date": "2022-01-05", "timeSpent": "5 hours"}
            ],
        }
    ],
    "files": [{"name": "invoice1.pdf", "contentType": "application/pdf"}],
}

# this is the MoneyBird external invoice spec.
# full reference: https://developer.moneybird.com/api/external_sales_invoices/#post_external_sales_invoices
"""
| Map | Parameter                                               | Type    | Description      |
| --- | ------------------------------------------------------- | ------- | ---------------- |
|  *  | `external_sales_invoice[contact_id]`                    | Integer | Should be a valid contact id. |
|  *  | `external_sales_invoice[reference]`                     | String  |                  |
|  *  | `external_sales_invoice[date]`                          | String  |                  |
|  *  | `external_sales_invoice[due_date]`                      | String  |                  |
|  +  | `external_sales_invoice[currency]`                      | String  | ISO three-character currency code, e.g. EUR or USD. |
|  +  | `external_sales_invoice[prices_are_incl_tax]`           | Boolean |                  |
|  *  | `external_sales_invoice[source]`                        | String  |                  |
|  *  | `external_sales_invoice[source_url]`                    | String  |                  |
|     | `external_sales_invoice[details_attributes][id]`        | Integer |                  |
|  *  | `external_sales_invoice[details_attributes][description]` | String |         |
|     | `external_sales_invoice[details_attributes][period]`    | String  | String with a date range: 20140101..20141231, presets are also allowed: this_month, prev_month, next_month, etc. |
|  *  | `external_sales_invoice[details_attributes][price]`     | Decimal | Both a decimal and a string ‘10,95’ are accepted. |
|  +  | `external_sales_invoice[details_attributes][amount]`    | String  |                 |
|     | `external_sales_invoice[details_attributes][tax_rate_id]` | Integer | Should be a valid tax rate id. |
|     | `external_sales_invoice[details_attributes][ledger_account_id]` | Integer | Should be a valid ledger account id. |
|     | `external_sales_invoice[details_attributes][project_id]` | Integer | Should be a valid project id. |
|     | `external_sales_invoice[details_attributes][row_order]` | Integer |              |
|     | `external_sales_invoice[details_attributes][_destroy]`  | Boolean |              |

*: mapped
+: constant value to be defined in the mapping

"""


def test_invoice_mapping():
    inv = from_fibery_invoice(example_fibery_invoice)

    assert inv["reference"] == "2023-46"
    assert inv["date"] == "2023-11-30"
    assert inv["due_date"] == "2023-12-14"
    assert inv["currency"] == "EUR"
    assert inv["source"] == "Fibery"
    assert inv["source_url"] == "https://serra.fibery.io/Sales/Invoice/46"
    assert inv["details_attributes"][0]["description"] == "van Oord Datalab"
    assert inv["details_attributes"][0]["price"] == 500.00
    assert inv["details_attributes"][0]["amount"] == 1
    assert inv["prices_are_incl_tax"] == False
