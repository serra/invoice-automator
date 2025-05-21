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

## Deployment

To make a release, sync to github and run:

```shell
make release
```

On successful release, a Docker image is created an d pushed to Dockerhub.

The [app is deployed to Digital Ocean](https://cloud.digitalocean.com/apps?i=93594d).
It hosts a webhook for Fibery at <https://automator.serraict.com/>.

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

--

### Backlog

* Fix rounding error in MoneyBird invoice and printed invoice. 
  E.g. [factuur 2025-65](https://serra.fibery.io/favorites/Project_Management/My-Tasks-2#Sales/Invoice/Open-informatiesysteem-Potlilium-69)

---

[GraphQL API]: https://api.fibery.io/graphql.html#graphql-api-overview
[weasyprint]: https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#python-api
[style guide]: https://www.serraict.com/learn/2015/10/19/style-guide