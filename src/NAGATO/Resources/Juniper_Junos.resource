*** Settings ***
Documentation       High-level keywords for operating Juniper Junos

Library             NAGATO.NetmikoLibrary


*** Keywords ***
Request System Halt
    [Documentation]    Halt the system with specified options.
    [Arguments]    ${alias}    ${member}=${EMPTY}    ${routing-engine}=${EMPTY}    ${at-time}=${EMPTY}    ${in-minutes}=${EMPTY}    ${media}=${EMPTY}    ${message}=${EMPTY}

    ${output} =    NAGATO.NetmikoLibrary.Send Command
    ...    command_string=request system halt ${member} ${routing-engine} ${at-time} ${in-minutes} ${media} ${message}
    ...    expect_string=Halt the system ?    alias=${alias}

    NAGATO.NetmikoLibrary.Write Channel    out_data=yes    alias=${alias}
    
Request System Reboot
    [Documentation]    Reboot the system with specified ${option}.
    [Arguments]    ${alias}    ${option}=both-routing-engines

    NAGATO.NetmikoLibrary.Send Command    command_string=request system reboot ${option}    expect_string=Reboot the system ?    alias=${alias}

    NAGATO.NetmikoLibrary.Send Command    command_string=yes    expect_string=Shutdown NOW!    alias=${alias}

