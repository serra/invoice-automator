import logging
from fastapi import FastAPI
from .__main__ import invoice_client, file_client
from .commands import attach_pdf_files_to_invoices

root_logger = logging.getLogger(__name__)
root_logger.info("Starting webapp ... ")

app = FastAPI()


@app.get("/update-invoices")
def update_invoices():
    root_logger.info("Updating invoices ... ")
    attach_pdf_files_to_invoices(invoice_client, file_client, "Ready")
    return {"message": "Invoices updated!"}
