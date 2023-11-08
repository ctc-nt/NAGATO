*** Settings ***
Documentation       High-level keywords for operating Juniper Junos

Library             NAGATO.NetmikoLibrary
Library             Collections
Library             String


*** Keywords ***
Request System Reboot
    [Documentation]    Reboot the system with specified ${option}.
    [Arguments]    ${alias}    ${option}=both-routing-engines

    NAGATO.NetmikoLibrary.Send Command    command_string=request system reboot ${option}    expect_string=Reboot the system ?    alias=${alias}

    NAGATO.NetmikoLibrary.Send Command    command_string=yes    expect_string=Shutdown NOW!    alias=${alias}
