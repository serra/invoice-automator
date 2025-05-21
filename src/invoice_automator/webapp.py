import logging
import os
from fastapi import FastAPI, Request
from .__main__ import invoice_client, file_client
from .commands import attach_pdf_files_to_invoice_by_id, save_invoice_to_moneybird_by_id
from .fibery import (
    SENT_STATE_ID,
    id_for_invoice_with_state_changed_to,
    id_for_invoice_with_state_changed_to_ready,
)
from .moneybird import ExternalInvoiceClient

logger = logging.getLogger(__name__)
logger.info("Starting webapp ... ")

app = FastAPI()


@app.post("/invoice-updated")
async def update_invoices(request: Request):
    logger.info("Updating invoices ... ")
    data = await request.json()
    ready_invoice_id = id_for_invoice_with_state_changed_to_ready(data)
    sent_invoice_id = id_for_invoice_with_state_changed_to(SENT_STATE_ID, data)
    if ready_invoice_id:
        logger.info(
            f"State changed to ready for invoice {ready_invoice_id[:5]}, attaching files ... "
        )
        attach_pdf_files_to_invoice_by_id(invoice_client, file_client, ready_invoice_id)
    elif sent_invoice_id:
        money_bird_client = ExternalInvoiceClient(
            base_url=os.getenv("MONEY_BIRD_BASE_URL")
        )
        logger.info(
            f"State changed to sent for invoice {sent_invoice_id[:5]}, adding invoice to administration ... "
        )
        save_invoice_to_moneybird_by_id(
            invoice_client, money_bird_client, sent_invoice_id
        )
    else:
        logger.info("State not changed to ready or sent, doing nothing ... ")
    return {"message": "Invoices updated!"}
