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
    Wait Until Keyword Succeeds    300 s    60s    Establish Connection    alias=${JUNOS_1}[alias]

Fail_01
    [Documentation]    `option` is incorrect and the others are correct
    Run Keyword And Expect Error    ReadTimeout:*    Request System Reboot    option=wrong_option    alias=${JUNOS_1}[alias]
