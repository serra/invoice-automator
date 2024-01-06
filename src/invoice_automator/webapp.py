import logging
from pprint import pprint
from fastapi import FastAPI, Request
from .__main__ import invoice_client, file_client
from .commands import attach_pdf_files_to_invoices
from .fibery import id_for_invoice_with_state_changed_to_ready


logger = logging.getLogger(__name__)
logger.info("Starting webapp ... ")

app = FastAPI()


@app.post("/invoice-updated")
async def update_invoices(request: Request):
    logger.info("Updating invoices ... ")
    data = await request.json()
    id = id_for_invoice_with_state_changed_to_ready(data)
    if id:
        logger.info(
            f"State changed to ready for invoice {id[:5]}, attaching files ... "
        )
    else:
        logger.info("State not changed to ready, doing nothing ... ")
    return {"message": "Invoices updated!"}
