API Access
==========

The invoice automator needs access to:

- Fibery
- MoneyBird

This document describes how to set up the environment to access these services.

Accessing and storing Secrets
-----------------------------

The Invoice Automator uses the `keyring package <https://pypi.org/project/keyring/>`_ 
to store and access secrets in our development environment.
Keyring comes with sensible defaults for most operating systems,
but you can also configure it to use a different backend.
Secrets (such as passwords, api keys, oAuth access tokens) 
are _never_ saved to disk or displayed on screen.

In the development environment, store the api token in the credential storage of your operating system.
Use the init script `../scripts/init_api_tokens.sh`_ to set up the environment.

Access invoices stored in Fibery
--------------------------------

To access Fibery, you need to a Fibery API token.
You can generate a token `in the Fibery UI <https://serra.fibery.io/fibery/settings/api-tokens>`_

The URL to the Fibery API and this token should be specified as an environment variable.


.. code:: robotframework
    
    *** Test Cases ***
    The development environment is set up to access Fibery
        Environment Variable Should Be Set    SPACE_URL
        Fibery API token is stored in credential storage to access invoices

You can access the Fibery GraphQL API unsing this 
`GraphiQL UI  <https://serra.fibery.io/api/graphql/space/Sales>`_ too.


Access to MoneyBird
-------------------

We use the MoneyBird API to add sales invoices to our MoneyBird administration.

In the development environment, store the api token in the credential storage of your operating system.

.. code:: robotframework

    *** Test Cases ***
    The environment is set up to access our MoneyBird administration
        can access credential  "Serra ICT Invoice Automator"    "SerraICTInvoiceAutomatorMoneyBirdToken"
        Environment Variable Should Be Set    MONEY_BIRD_BASE_URL

Moneybird provides a test environment, use this for integration testing.
We do not use our production administration for testing.

About these specifications
--------------------------

This is an executable specification that 
can be executed with `Robot Framework <http://robotframework.org/>`_.

.. code:: robotframework

    *** Settings ***
    Library          OperatingSystem
    Library          ./lib/FiberyLibrary.py
    Library          ./lib/KeyringLibrary.py







