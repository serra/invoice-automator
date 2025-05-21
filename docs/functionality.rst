Invoice Automator
=================

Invoice Automator is Serra ICT's simple command line application 
to create and email pretty emails based on data from our administration system.

Main features:

* List open invoices ready to be sent.
* Generate pdf invoices matching the style of our public website.

Installation
------------

See readme in the `src` folder.

Usage
-----

After installation, you can run the application by running `get-paid` in your terminal.

.. code:: robotframework

    *** Test Cases ***
    Run the application and get help
        Run Successfully     get-paid
        Run Successfully     get-paid --help

List invoices
~~~~~~~~~~~~~

To list invoices, use the `list` command.

.. code:: robotframework

    *** Test Cases ***
    List invoice information
        Run Successfully     get-paid list
        Run Successfully     get-paid --state=Draft list

    The default state is 'Ready', so these commands are equivalent:
        Run Successfully     get-paid list
        Run Successfully     get-paid --state=Ready list

Generate PDF files
~~~~~~~~~~~~~~~~~~

The application uses weasyprint to generate PDF files.

.. code:: robotframework

    *** Test Cases ***
    Create PDF documents for all invoices in the 'Ready' state
        Run Successfully     get-paid gen

Attach invoices
~~~~~~~~~~~~~~~

A user can send the emails using the Fibery user interface.
An invoice will have a `send invoice` button that will send the email.
Fibery uses SendGrid to send emails.
This script will attach the pdf to the invoice entity in Fibery.

.. code:: robotframework

    *** Test Cases ***
    Prepare emails for all invoices in the 'Ready' state
        Run Successfully     get-paid attach
        The pdf files are attached to the invoice entities in Fibery
        The invoices are moved out of the Ready column in Fibery

The emails are reviewed manually before sending.

Administrate invoices
~~~~~~~~~~~~~~~~~~~~~

To administrate invoices, we use the `admin` command.

.. code:: robotframework

    *** Test Cases ***
    Administrate all invoices in the sent column
        Run Successfully     get-paid admin
        The invoices in the sent column in Fibery are stored as an external invoice in MoneyBird

Automation
~~~~~~~~~~

The application can be run as a web application.
This web application can respond to webhooks from Fibery.

The production application is running a local server.
The base url for this application is https://automator.serraict.com.

The following webhooks are configured:

* Invoice updated, handled by `invoice-updated <https://automator.serraict.com/invoice-updated>`_

See `the api documentation <https://automator.serraict.com/docs>`_.

About these specifications
--------------------------

This is an executable specification that 
can be executed with `Robot Framework <http://robotframework.org/>`_.

.. code:: robotframework

    *** Settings ***
    Resource    ./lib/CliKeywords.robot
    Library          ./lib/FiberyLibrary.py
    Library          ./lib/MoneyBirdLibrary.py