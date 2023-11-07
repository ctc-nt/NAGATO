*** Settings ***
Documentation       High-level keywords for operating Juniper Junos

Library             NAGATO.NetmikoLibrary
Library             Collections
Library             String


*** Keywords ***
Request System Halt
    [Documentation]    Halt the system specified in ${target_system}.user
    [Arguments]    ${alias}    ${target_system}=member 0 both-routing-engines

    NAGATO.NetmikoLibrary.Send Command    command_string=request system halt ${target_system}    expect_string=Halt the system ?    alias=${alias}

    NAGATO.NetmikoLibrary.Send Command    command_string=yes    expect_string=Shutdown NOW!    alias=${alias}
