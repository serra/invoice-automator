# Fibery invoices automation

This repository contains scripts that help me automate my Fibery invoice workflows.

I use the Fibery [GraphQL API] to access data.

The app will fetch invoice data from my Fibery workspace. Fibery is an online collaboration and knowledge management system. In Fibery, information is stored in an unstructured (markdown) format and in a structured, relational database-like format. The structured information is available through a GraphQL api.

## Set up environment

```shell
make bootstrap
. ./venv/bin/activate
make update
```

## How to use

```shell
make console
```

## Features

* List open invoices ready to be sent.
* Generate pdf invoices matching the style of our public website.

## Dependencies

Uses requests,
click,
Jinja2, and
pdfkit,
see [`requirements.txt`](requirements.txt) for details.
The package pdfkit requires [wkhtmltopdf] to be available on the command line.

## Security

All sensitive information is retrieved using [keyring].
Set up your platform's credential storage with the appropriate items.
The app will raise a comprehensive exception if it cannot retrieve required items.

* _Fibery_: requires an API token.
* _GMail_: requires client secrets (in json format).
  Since we send emails on behalf of an actual human, we require her permissions to do so.
  So we use OAuth2. The OAuth token expires after 24h, so you should not have to login more than once a day.
  The token is stored using [keyring].

---

## Doing

* Save email to draft box in Google workspace.
  The email should have a pdf version of the invoice attached to it.
  Subject should contain the invoice number.
  Text should be kind.
  

## Backlog

* add QR code to pdf invoices
* Upload the pdf to Fibery.
* Upload the invoice to the administration.
* Find a way to use local resources only (e.g. no links to stylesheets using https). Consider switching to [weasyprint]

---

[GraphQL API]: https://api.fibery.io/graphql.html#graphql-api-overview
[Python API]: https://developers.google.com/gmail/api/quickstart/python
[wkhtmltopdf]: https://wkhtmltopdf.org/
[weasyprint]: https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#python-api
[keyring]: https://github.com/jaraco/keyring
