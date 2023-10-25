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

### Fibery

To access Fibery, an API token is needed.
Preferably, you pass it as an environment variable `FIBERY_API_TOKEN`.
This token can be passed as a command-line argument.

### Google mail

Uses OAuth2. Since we send emails on behalf of an actual human, we require her permissions to do so.
The token expires after 24h, so you should not have to login more than once.
The client configuration (including client id and client secret) are stored using the [keyring] package.

---

## Doing

* list the last emails with te admin inbox tokens
* Save email to draft box in Google workspace.
  Google has a [Python API] that requires Python 3.10.7+, so we'd need to upgrade Python ✅.

## Backlog

* add QR code to pdf invoices
* Upload the pdf to Fibery.
* Upload the invoice to the administration.
* Find a way to use local resources only. Consider switching to [weasyprint]

---

[GraphQL API]: https://api.fibery.io/graphql.html#graphql-api-overview
[Python API]: https://developers.google.com/gmail/api/quickstart/python
[wkhtmltopdf]: https://wkhtmltopdf.org/
[weasyprint]: https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#python-api
[keyring]: https://github.com/jaraco/keyring