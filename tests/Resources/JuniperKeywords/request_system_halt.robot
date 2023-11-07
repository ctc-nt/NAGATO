*** Settings ***
Documentation       `Request System Halt` Unittest

Variables           unittest.yml
Library             NAGATO.NetmikoLibrary
Resource            NAGATO/Resources/Juniper_Junos.resource

Suite Setup         Connect    &{JUNOS_2}
Suite Teardown      Disconnect All


*** Test Cases ***
Fail_01
    [Documentation]    `target_system` is incorrect and the others are correct

    Request System Halt    target_system=wrong_target_system    alias=${JUNOS_2}[alias]

Success_01
    [Documentation]    `All arguments are collect`

    Request System Halt    alias=${JUNOS_2}[alias]
