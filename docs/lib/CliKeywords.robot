*** Settings ***
Library     OperatingSystem


*** Keywords ***
Run Successfully
    [Arguments]    ${command}
    ${rc}    ${stderr}=    Run And Return RC And Output    ${command}
    Should Be Equal As Integers    ${rc}    0
    ...    reason=Command failed with error: ${stderr}
