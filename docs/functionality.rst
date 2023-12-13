Invoice Automator
=================

Invoice Automator is Serra ICT's simple command line application 
to create and email pretty emails based on data from our administration system.

Main features:

* List open invoices ready to be sent.
* Generate pdf invoices matching the style of our public website.
* Create email drafts in the authenticated user's GMail draft mailbox.

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

The application uses `wkhtmltopdf <http://wkhtmltopdf.org/>`_ to generate PDF files.

.. code:: robotframework

    *** Test Cases ***
    Webkit to PDF tool is available on the command line:
        Run Successfully     wkhtmltopdf --version

    *** Test Cases ***
    Create PDF documents for all invoices in the 'Ready' state
        Run Successfully     get-paid gen

Send invoices
~~~~~~~~~~~~~

To send emails, we use the `email` command.

.. code:: robotframework

    *** Test Cases ***
    Prepare emails for all invoices in the 'Ready' state
        Run Successfully     get-paid email
        The invoices emails are in the Drafts folder with pdf invoices as attachments
        The pdf files are attached to the invoice entities in Fibery

The emails are reviewed manually before sending.
Once emails are sent, the state of the invoices
the user moves them to the sent column in Fibery.

Administrate invoices
~~~~~~~~~~~~~~~~~~~~~

To administrate invoices, we use the `admin` command.

.. code:: robotframework

    *** Test Cases ***
    Administrate all invoices in the sent column
        Run Successfully     get-paid admin
        The invoices in the sent column in Fibery are stored as an external invoice in MoneyBird




About these specifications
--------------------------


This is an executable specification that 
can be executed with `Robot Framework <http://robotframework.org/>`_.

.. code:: robotframework

    *** Settings ***
    Resource    ./lib/CliKeywords.robot
    Library          ./lib/FiberyLibrary.py
    Library          ./lib/GmailLibrary.py
    Library          ./lib/MoneyBirdLibrary.py