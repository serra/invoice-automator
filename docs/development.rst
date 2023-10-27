Development
===========

See ./../readme.md for instructions on how to set up the development environment.
Use this executable specification to validate your dev setup.

To run it:

    make check-environment

Access invoices stored in Fibery
--------------------------------

To access Fibery, you need to add a Fibery API token to your credentials storage.
You can generate a token `in the Fibery UI <https://serra.fibery.io/fibery/settings/api-tokens>`_

The URL to the Fibery environment should be specified an environment variable.

.. code:: robotframework
    
    *** Test Cases ***
    The environment is set up to access Fibery:
        Environment Variable Should Be Set    SPACE_URL
        Fibery API token is stored in credential storage to access invoices

About these specifications
------------------------

This is an executable specification that 
can be executed with `Robot Framework <http://robotframework.org/>`_.

.. code:: robotframework

    *** Settings ***
    Library          OperatingSystem
    Library          ./lib/FiberyLibrary.py







