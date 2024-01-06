# these examples were taken from monitoring the system
from invoice_automator.fibery import id_for_invoice_with_state_changed_to_ready


invoice_state_changed_from_draft_to_ready = {
    "authorId": "1b06e986-c6a0-4fbe-8fb5-f0167aa336ce",
    "command": {"correlationId": "f04ba190-ac9f-11ee-bab0-6beacf954aac"},
    "creationDate": "2024-01-06T14:29:02.818Z",
    "effects": [
        {
            "effect": "fibery.entity/update",
            "id": "8165d970-abb5-11ee-8c9c-13c3809b3d29",
            "type": "Sales/Invoice",
            "typeId": "3b3e1c96-c89c-4650-a884-ebb864ed076e",
            "values": {
                "fibery/modification-date": "2024-01-06T14:29:02.789Z",
                "workflow/state": {"fibery/id": "a69f6220-6811-11ee-9c7a-0bc3e2dc4277"},
            },
            "valuesBefore": {
                "fibery/modification-date": "2024-01-06T14:19:25.404Z",
                "workflow/state": {"fibery/id": "b3677d57-a0e1-41ca-b068-376dec6fa300"},
            },
        }
    ],
    "sequenceId": 7359,
}

invoice_name_changed = {
    "authorId": "1b06e986-c6a0-4fbe-8fb5-f0167aa336ce",
    "command": {"correlationId": "a68ce360-aca0-11ee-bab0-6beacf954aac"},
    "creationDate": "2024-01-06T14:34:08.638Z",
    "effects": [
        {
            "acl-index": 0,
            "effect": "fibery.entity/update",
            "id": "8165d970-abb5-11ee-8c9c-13c3809b3d29",
            "type": "Sales/Invoice",
            "typeId": "3b3e1c96-c89c-4650-a884-ebb864ed076e",
            "values": {
                "Sales/Name": "test invoice - name changed",
                "fibery/modification-date": "2024-01-06T14:34:08.605Z",
            },
            "valuesBefore": {
                "Sales/Name": "test invoice - new name",
                "fibery/modification-date": "2024-01-06T14:29:02.789Z",
            },
        }
    ],
    "sequenceId": 7360,
}

invoice_created = {
    "authorId": "1b06e986-c6a0-4fbe-8fb5-f0167aa336ce",
    "command": {"correlationId": "53bcd361-aca1-11ee-bab0-6beacf954aac"},
    "creationDate": "2024-01-06T14:38:59.159Z",
    "effects": [
        {
            "acl-index": 0,
            "effect": "fibery.entity/create",
            "id": "53bcd360-aca1-11ee-bab0-6beacf954aac",
            "type": "Sales/Invoice",
            "typeId": "3b3e1c96-c89c-4650-a884-ebb864ed076e",
            "values": {
                "Sales/Customer Address": None,
                "Sales/Customer City": None,
                "Sales/Customer Email": None,
                "Sales/Customer Name": None,
                "Sales/Customer Reference": None,
                "Sales/Customer Zipcode": None,
                "Sales/Due Date": None,
                "Sales/Invoice Date": None,
                "Sales/Invoice Number": None,
                "Sales/Invoice Number_0c0upwp_deleted": None,
                "Sales/Invoice Number_0gcqlw0_deleted": None,
                "Sales/Invoice Sequence Number": None,
                "Sales/Name": "new draft invoice",
                "Sales/Status": None,
                "Sales/Total Amount": None,
                "Sales/Total Amount_0rsgh1m_deleted": None,
                "Sales/Total Including VAT": None,
                "Sales/Total Including_0a5xj39_deleted": None,
                "Sales/VAT": None,
                "Sales/VAT Percentage": None,
                "fibery/creation-date": "2024-01-06T14:38:59.126Z",
                "fibery/modification-date": "2024-01-06T14:38:59.126Z",
                "fibery/public-id": "53",
                "fibery/rank": -6569916191130599,
            },
        },
        {
            "effect": "fibery.entity/update",
            "id": "53bcd360-aca1-11ee-bab0-6beacf954aac",
            "type": "Sales/Invoice",
            "typeId": "3b3e1c96-c89c-4650-a884-ebb864ed076e",
            "values": {
                "fibery/created-by": {
                    "fibery/id": "1b06e986-c6a0-4fbe-8fb5-f0167aa336ce"
                },
                "fibery/modification-date": "2024-01-06T14:38:59.126Z",
            },
            "valuesBefore": {
                "fibery/created-by": None,
                "fibery/modification-date": "2024-01-06T14:38:59.126Z",
            },
        },
        {
            "effect": "fibery.entity/update",
            "id": "53bcd360-aca1-11ee-bab0-6beacf954aac",
            "type": "Sales/Invoice",
            "typeId": "3b3e1c96-c89c-4650-a884-ebb864ed076e",
            "values": {
                "fibery/modification-date": "2024-01-06T14:38:59.126Z",
                "workflow/state": {"fibery/id": "b3677d57-a0e1-41ca-b068-376dec6fa300"},
            },
            "valuesBefore": {
                "fibery/modification-date": "2024-01-06T14:38:59.126Z",
                "workflow/state": None,
            },
        },
    ],
    "sequenceId": 7361,
}

invoice_deleted = {
    "authorId": "1b06e986-c6a0-4fbe-8fb5-f0167aa336ce",
    "command": {"correlationId": "c6d5b330-aca1-11ee-bab0-6beacf954aac"},
    "creationDate": "2024-01-06T14:42:12.309Z",
    "effects": [
        {
            "effect": "fibery.entity/update",
            "id": "53bcd360-aca1-11ee-bab0-6beacf954aac",
            "type": "Sales/Invoice",
            "typeId": "3b3e1c96-c89c-4650-a884-ebb864ed076e",
            "values": {
                "fibery/created-by": None,
                "fibery/modification-date": "2024-01-06T14:42:12.278Z",
            },
            "valuesBefore": {
                "fibery/created-by": {
                    "fibery/id": "1b06e986-c6a0-4fbe-8fb5-f0167aa336ce"
                },
                "fibery/modification-date": "2024-01-06T14:38:59.757Z",
            },
        },
        {
            "effect": "fibery.entity/update",
            "id": "53bcd360-aca1-11ee-bab0-6beacf954aac",
            "type": "Sales/Invoice",
            "typeId": "3b3e1c96-c89c-4650-a884-ebb864ed076e",
            "values": {
                "fibery/modification-date": "2024-01-06T14:42:12.278Z",
                "workflow/state": None,
            },
            "valuesBefore": {
                "fibery/modification-date": "2024-01-06T14:38:59.757Z",
                "workflow/state": {"fibery/id": "b3677d57-a0e1-41ca-b068-376dec6fa300"},
            },
        },
        #     {
        #         "acl-index": 0,
        #         "effect": "fibery.entity/delete",
        #         "id": "53bcd360-aca1-11ee-bab0-6beacf954aac",
        #         "type": "Sales/Invoice",
        #         "typeId": "3b3e1c96-c89c-4650-a884-ebb864ed076e",
        #         "valuesBefore": {
        #             "Sales/Customer Address": None,
        #             "Sales/Customer City": None,
        #             "Sales/Customer Email": None,
        #             "Sales/Customer Name": None,
        #             "Sales/Customer Reference": None,
        #             "Sales/Customer Zipcode": None,
        #             "Sales/Due Date": None,
        #             "Sales/Invoice Date": None,
        #             "Sales/Invoice Number": "-",
        #             "Sales/Invoice Number_0c0upwp_deleted": None,
        #             "Sales/Invoice Number_0gcqlw0_deleted": None,
        #             "Sales/Invoice Sequence Number": None,
        #             "Sales/Name": "new draft invoice",
        #             "Sales/Status": None,
        #             "Sales/Total Amount": "0",
        #             "Sales/Total Amount_0rsgh1m_deleted": None,
        #             "Sales/Total Including VAT": "0",
        #             "Sales/Total Including_0a5xj39_deleted": None,
        #             "Sales/VAT": "0",
        #             "Sales/VAT Percentage": None,
        #             "fibery/creation-date": "2024-01-06T14:38:59.126Z",
        #             "fibery/modification-date": "2024-01-06T14:42:12.278Z",
        #             "fibery/public-id": "53",
        #             "fibery/rank": -6569916191130599,
        #         },
        #     },
        #
    ],
    "sequenceId": 7367,
}

# not tested: batch updates where multiple entities change in the same transaction


def test_invoice_state_changed_from_draft_to_ready():
    assert id_for_invoice_with_state_changed_to_ready(
        invoice_state_changed_from_draft_to_ready
    )
    assert not id_for_invoice_with_state_changed_to_ready(invoice_name_changed)
    assert not id_for_invoice_with_state_changed_to_ready(invoice_created)
    assert not id_for_invoice_with_state_changed_to_ready(invoice_deleted)
    assert (
        id_for_invoice_with_state_changed_to_ready(
            invoice_state_changed_from_draft_to_ready
        )
        == "8165d970-abb5-11ee-8c9c-13c3809b3d29"
    ), "invoice id should be extracted from effects, but we got the wrong one"
