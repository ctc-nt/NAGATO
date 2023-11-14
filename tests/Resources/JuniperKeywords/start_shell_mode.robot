*** Settings ***
Documentation       `Start Shell Mode` Unittest
Variables           unittest.yml
Library             NAGATO.NetmikoLibrary
Resource            NAGATO/Resources/Juniper_Junos.resource

Suite Setup         Connect    &{JUNOS_1}                
Suite Teardown      Disconnect All

*** Test Cases ***
Success_01
    [Documentation]    `All arguments are collect`
    Start Shell Mode    alias=${JUNOS_1}[alias]    root_password=ntdev2021

