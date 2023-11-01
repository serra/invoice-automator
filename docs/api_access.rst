API Access
==========

The invoice automator needs access to:

- Fibery
- Gmail

This document describes how to set up the environment to access these services.

Accessing Secrets
-----------------

The Invoice Automator uses the `keyring package <https://pypi.org/project/keyring/>`_ 
to store and access secrets.
Keyring comes with sensible defaults for most operating systems,
but you can also configure it to use a different backend.
Secrets (such as passwords, api keys, oAuth access tokens) 
are _never_ saved to disk or displayed on screen.

Access invoices stored in Fibery
--------------------------------

To access Fibery, you need to add a Fibery API token to your credentials storage.
You can generate a token `in the Fibery UI <https://serra.fibery.io/fibery/settings/api-tokens>`_

The URL to the Fibery API should be specified as an environment variable.

.. code:: robotframework
    
    *** Test Cases ***
    The environment is set up to access Fibery
        Environment Variable Should Be Set    SPACE_URL
        Fibery API token is stored in credential storage to access invoices

You can access the Fibery GraphQL API unsing this 
`GraphiQL UI  <https://serra.fibery.io/api/graphql/space/Sales>`_ too.

Access to Gmail
---------------

We send out invoices via Gmail on behalf of an actual human.
This human needs to grant the invoice automator access to their Gmail account.
This is done via oAuth2.

The GMail API is managed through the 
`Google Cloud project Serra ICT Invoice Automator <https://console.cloud.google.com/apis/credentials?project=serraict-invoice-atomator>`_.
Download the credentials file in json format and store it in your platform's keyring.

.. code:: robotframework

    *** Test Cases ***
    The environment is set up to start the Gmail OAuth2 workflow
        can access credential  "Serra ICT Invoice Automator"    "SerraICTInvoiceAutomatorGoogleClientSecrets"
        can load gmail client secrets

About these specifications
------------------------

This is an executable specification that 
can be executed with `Robot Framework <http://robotframework.org/>`_.

.. code:: robotframework

    *** Settings ***
    Library          OperatingSystem
    Library          ./lib/FiberyLibrary.py
    Library          ./lib/GmailLibrary.py
    Library          ./lib/KeyringLibrary.py







