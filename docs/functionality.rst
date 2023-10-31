Invoice Automator
=================

Invoice Automator is Serra ICT's simple command line application 
to create and email pretty emails based on data from our administration system.

Installation
------------

See readme in the `src` folder.

.. note:: 
    
    This application is only tested on Mac OS X.
    It might work on other platforms, but we don't know.

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

To list invoices, use the `list-invoices` command.

.. code:: robotframework

    *** Test Cases ***
    List invoice information
        Run Successfully     get-paid list-invoices
        Run Successfully     get-paid --state=Draft list-invoices

    The default state is 'Ready', so these commands are equivalent:
        Run Successfully     get-paid list-invoices
        Run Successfully     get-paid --state=Ready list-invoices

PDF generation
~~~~~~~~~~~~~~

The application uses `wkhtmltopdf <http://wkhtmltopdf.org/>`_ to generate PDF files.

.. code:: robotframework

    *** Test Cases ***
    Webkit to PDF tool is available on the command line:
        Run Successfully     wkhtmltopdf --version

    *** Test Cases ***
    Create PDF documents for all invoices in the 'Ready' state
        Run Successfully     get-paid generate-pdf-for-invoices

About these specifications
--------------------------


This is an executable specification that 
can be executed with `Robot Framework <http://robotframework.org/>`_.

.. code:: robotframework

    *** Settings ***
    Resource    ./lib/CliKeywords.robot