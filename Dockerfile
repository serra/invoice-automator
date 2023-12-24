FROM python:3.10

WORKDIR /invoice-automator

COPY . /invoice-automator/

RUN apt-get update && apt-get install -y python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0
RUN apt-get install -y fonts-open-sans
RUN pip install --upgrade pip setuptools wheel setuptools_scm
RUN pip install --no-cache-dir --upgrade .
RUN mkdir -p /invoice-automator/output/invoices

CMD ["get-paid", "attach"]