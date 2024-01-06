# Fibery invoices automation

This repository contains scripts that automate my invoice workflows.
I create my invoices in Fibery, use Fibery's [GraphQL API] to download the invoice data.

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

See the [executable specification](./docs/functionality.rst) for details on usage.

## Dependencies and prerequisites

Python 3.10 and [weasyprint].
See [`pyproject.toml`](pyproject.toml) for all requirements.
Not required, but for best renderings of pdf invoices, install the fonts required by our [style guide].

## Documentation

See [./docs/](./docs) for (executable) specifications.

## Work

### Doing

* When an invoice is updated, we see a log message in DO.
  * add webhook for invoices
  * request information is logged and visible in DO
  * scripts to create and maintain webhooks are added to this repository
  * documentation  is updated

### Backlog


* Only respond to state changes of invoices, not to every update
  * state field change -> log it
  * other field change -> ignore it
* Sales invoices are automatically administrated, and I do not have to do anything manually.
* ---
* publish wheel to local repository

* Find a way to use local resources only (e.g. no links to stylesheets using https, no external images).
  Consider switching to [weasyprint].
* a better name would be (fibery) serra ict invoice automator
* deploy to another machine e.g. with a CI tool on it, so that I can automate it further

---

[GraphQL API]: https://api.fibery.io/graphql.html#graphql-api-overview
[weasyprint]: https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#python-api
[style guide]: https://www.serraict.com/learn/2015/10/19/style-guide