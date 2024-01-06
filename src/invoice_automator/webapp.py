import logging
from pprint import pprint
from fastapi import FastAPI, Request
from .__main__ import invoice_client, file_client
from .commands import attach_pdf_files_to_invoices


root_logger = logging.getLogger(__name__)
root_logger.info("Starting webapp ... ")

app = FastAPI()


@app.post("/invoice-updated")
async def update_invoices(request: Request):
    root_logger.info("Updating invoices ... ")
    print("Request headers:")
    pprint(dict(request.headers))
    body = await request.body()
    print("Request body:")
    pprint(body.decode())
    return {"message": "Invoices updated!"}
