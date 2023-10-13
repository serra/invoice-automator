# Fibery invoices automation

This repository contains scripts that help me automate my Fibery invoice workflows.

I use the Fibery [GraphQL API] to access data.

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

[GraphQL API]: https://api.fibery.io/graphql.html#graphql-api-overview
