FROM python:3.10

WORKDIR /invoice-automator

COPY . /invoice-automator/

RUN pip install --upgrade pip setuptools wheel setuptools_scm
RUN pip install --no-cache-dir --upgrade .
# wkhtmltopdf is required for pdfkit

CMD ["get-paid", "--help"]