*** Settings ***
Documentation       High-level keywords for operating Juniper Junos

Library             NAGATO.NetmikoLibrary
Library             Collections
Library             String


*** Keywords ***
Request System Halt
    [Documentation]    Halt the system with specified ${option}.
    [Arguments]    ${alias}    ${option}=member 0 both-routing-engines

    NAGATO.NetmikoLibrary.Send Command    command_string=request system halt ${option}    expect_string=Halt the system ?    alias=${alias}

    NAGATO.NetmikoLibrary.Send Command    command_string=yes    expect_string=Shutdown NOW!    alias=${alias}
