# Fibery invoices automation

This repository contains scripts that help me automate my invoice workflows.
I create my invoices in Fibery,
use Fibery's [GraphQL API] to download the invoice data,
and [Google Python API for gmail] to create draft invoice emails.

## Installation and development

Clone the repository, then:

```shell
make bootstrap
. ./venv/bin/activate
make update
```

## How to use

```shell
get-paid --help
```

See the [executable specification](./docs/functionality.rst) for details.


## Dependencies and prerequisites

See [`pyproject.toml`](pyproject.toml) for all requirements.
The package pdfkit requires [wkhtmltopdf] to be available on the command line.

## Documentation

See [./docs/](./docs) for (executable) specifications.

---

## Doing

Switch to weasyprint

Dockerize

* fix headers and footers
* fix fonts and styles

## Backlog

* Sales invoices are automatically administrated, and I do not have to do anything manually.
* ---
* Add a link to the email in Fibery
* Update status to review
* ---
* publish wheel to local repository
* Add QR code to pdf invoices
* Find a way to use local resources only (e.g. no links to stylesheets using https).
  Consider switching to [weasyprint].
* a better name would be (fibery) serra ict invoice automator
* deploy to another machine e.g. with a CI tool on it, so that I can automate it further

---

[GraphQL API]: https://api.fibery.io/graphql.html#graphql-api-overview
[wkhtmltopdf]: https://wkhtmltopdf.org/
[weasyprint]: https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#python-api
[keyring]: https://github.com/jaraco/keyring
[Google Python API for gmail]: https://developers.google.com/gmail/api/quickstart/python