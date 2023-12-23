FROM python:3.10

WORKDIR /invoice-automator

COPY . /invoice-automator/

RUN pip install --upgrade pip setuptools wheel setuptools_scm
RUN pip install --no-cache-dir --upgrade .
RUN apt-get update && apt-get install -y wkhtmltopdf
RUN mkdir ./output/invoices

CMD ["get-paid", "gen"]