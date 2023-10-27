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

About these specifications
------------------------

This is an executable specification that 
can be executed with `Robot Framework <http://robotframework.org/>`_.

.. code:: robotframework

    *** Settings ***
    Library          OperatingSystem

    *** Keywords ***
    Run Successfully
        [Arguments]    ${command}
        ${rc}    ${stderr}=    Run And Return RC And Output    ${command}
        Should Be Equal As Integers    ${rc}    0
        ...    reason=Command failed with error: ${stderr}