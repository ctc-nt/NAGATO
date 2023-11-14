*** Settings ***
Documentation       `Start Shell Mode` Unittest

Variables           unittest.yml
Library             NAGATO.NetmikoLibrary
Resource            NAGATO/Resources/Juniper_Junos.resource

Suite Setup         Connect    &{JUNOS_1}
Suite Teardown      Disconnect All


*** Test Cases ***
Success_01
    [Documentation]    All arguments are collect.
    Start Shell Mode    alias=${JUNOS_1}[alias]    user=root    root_password=ntdev2021
    ${output} =    NAGATO.NetmikoLibrary.Read Until Pattern    pattern=#    alias=${JUNOS_1}[alias]
    Should Contain    ${output}    item=#

Fail_01
    [Documentation]    One argument is incorrect and others are correct.

    ${status} =    Run Keyword And Return Status    Start Shell Mode    alias=${JUNOS_1}[alias]    user=root    root_password=wrong_pw
    Should Be Equal    ${status}    ${False}
