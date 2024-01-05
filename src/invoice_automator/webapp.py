import logging
from fastapi import FastAPI

root_logger = logging.getLogger(__name__)
root_logger.info("Starting webapp ... ")

app = FastAPI()


@app.get("/update-invoices")
def update_invoices():
    root_logger.info("Updating invoices ... ")
    return {"message": "Invoices updated!"}
