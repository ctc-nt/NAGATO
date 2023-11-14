*** Settings ***
Documentation       `Request System Halt` Unittest

Variables           unittest.yml
Library             NAGATO.NetmikoLibrary
Resource            NAGATO/Resources/Juniper_Junos.resource

Suite Setup         Connect    &{JUNOS_1}
Suite Teardown      Disconnect All

Fail_01
                    [Documentation]    One argument is incorrect and the others are correct
                    ${output} =    Run Keyword And Return Status    Request System Halt    member=wrong_member    alias=${JUNOS_1}[alias]
                    Run Keyword If    ${False}
...                 Should Contain    ${output}    ReadTimeout:
Success_01
                    [Documentation]    `All arguments are collect`
                    Request System Halt    alias=${JUNOS_1}[alias]
                    ${output} =    NAGATO.NetmikoLibrary.Read Channel    alias=${JUNOS_1}[alias]
                    Should Contain    ${output}    Please press any key to reboot.
