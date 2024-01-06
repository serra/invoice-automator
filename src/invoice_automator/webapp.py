import logging
from pprint import pprint
from fastapi import FastAPI, Request
from .__main__ import invoice_client, file_client
from .commands import attach_pdf_files_to_invoices


logger = logging.getLogger(__name__)
logger.info("Starting webapp ... ")

app = FastAPI()


@app.post("/invoice-updated")
async def update_invoices(request: Request):
    logger.info("Updating invoices ... ")
    data = await request.json()
    pprint(data)
    return {"message": "Invoices updated!"}
