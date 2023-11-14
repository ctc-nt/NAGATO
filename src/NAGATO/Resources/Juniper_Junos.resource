*** Settings ***
Documentation       High-level keywords for operating Juniper Junos

Library             NAGATO.NetmikoLibrary
Library             Collections
Library             String


*** Keywords ***
Start Shell Mode
    [Documentation]    Start the shell as an optional user.
    [Arguments]    ${alias}    ${user}    ${root_password}

    NAGATO.NetmikoLibrary.Send Command    command_string=start shell user ${user}    expect_string=Password:   alias=${alias}

    NAGATO.NetmikoLibrary.Write Channel    out_data=${root_password}${\n}    alias=${alias}  
    
