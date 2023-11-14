*** Settings ***
Documentation       `Request System Halt` Unittest

Variables           unittest.yml
Library             NAGATO.NetmikoLibrary
Resource            NAGATO/Resources/Juniper_Junos.resource

Suite Setup         Connect    &{JUNOS_1}
Suite Teardown      Disconnect All

*** Test Cases ***
Fail_01
    [Documentation]    One argument is incorrect and the others are correct
    ${status} =   Run Keyword And Return Status    
    ...    Request System Halt    member=wrong_member    alias=${JUNOS_1}[alias]
    Should Be Equal    ${status}    ${False}

    
Success_01
    [Documentation]    All arguments are collect

    Request System Halt    alias=${JUNOS_1}[alias]

    # Confirm not to be able to ssh connection to assert if halt successfully or not
    Disconnect    alias=${JUNOS_1}[alias]
    ${status} =    Run Keyword And Return Status    Connect    assert_halt    ${JUNOS_1}[device_type]    ${JUNOS_1}[host]    ${JUNOS_1}[username]    ${JUNOS_1}[password]
    Should Be Equal    ${status}    ${False}