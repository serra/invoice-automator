# Fibery invoices automation

This repository contains scripts that help me automate my Fibery invoice workflows.

I use the Fibery [GraphQL API] to access data.

The app will fetch invoice data from my Fibery workspace. Fibery is an online collaboration and knowledge management system. In Fibery, information is stored in an unstructured (markdown) format and in a structured, relational database-like format. The structured information is available through a GraphQL api.

## Set up environment

```
make bootstrap
. ./venv/bin/activate
make update
```

## How to use

Set the `FIBERY_API_TOKEN` environment variable to your API key.
I use 1password: `. ./export_api_token_from_1password.sh`.

```
make console
```

---

## Doing

Print invoice number, customer name and total to the command line.

## Backlog

* Generate a pdf for the ready invoices, with customer name, total amount and invoice number.
* Upload the pdf to Fibery.
* Add all invoice data to the invoice
* Add logo to the invoice
* Pretty-format dates and money fields
* Upload the invoice to the administration.


---

[GraphQL API]: https://api.fibery.io/graphql.html#graphql-api-overview
