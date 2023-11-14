*** Settings ***
Documentation       High-level keywords for operating Juniper Junos

Library             NAGATO.NetmikoLibrary
Library             Collections
Library             String


*** Keywords ***
Request System Halt
    [Documentation]    Halt the system with specified options.
    [Arguments]    ${alias}    ${member}=${EMPTY}    ${routing-engine}=${EMPTY}    ${at-time}=${EMPTY}    ${in-minutes}=${EMPTY}    ${in-minutes}=${EMPTY}    ${media}=${EMPTY}    ${message}=${EMPTY}

    ${output} =    NAGATO.NetmikoLibrary.Send Command    
    ...    command_string=request system halt ${member} ${routing-engine} ${at-time} ${in-minutes} ${in-minutes} ${media} ${message}
    ...    expect_string=Halt the system ?    alias=${alias}

    NAGATO.NetmikoLibrary.Write Channel    out_data=yes    alias=${alias}