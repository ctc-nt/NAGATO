*** Settings ***
Documentation       `Request System Reboot` Unittest

Variables           unittest.yml
Library             NAGATO.NetmikoLibrary
Resource            NAGATO/Resources/Juniper_Junos.resource

Suite Setup         Connect    &{JUNOS_1}
Suite Teardown      Disconnect All


*** Test Cases ***
Success_01
    [Documentation]    `All arguments are collect`
    Request System Reboot    option=${EMPTY}    alias=${JUNOS_1}[alias]

    # Assert if the system successfully reboot.
    ${result} =    Run Keyword And Return Status    Connect    &{JUNOS_1}
    IF    ${result} == ${False}
        Sleep    180s    reason=To wait until reboot successfully
        Connect    &{JUNOS_1}    alias=assertion_success
    END

Fail_01
    [Documentation]    `option` is incorrect and the others are correct
    Request System Reboot    option=wrong_option    alias=${JUNOS_1}[alias]
