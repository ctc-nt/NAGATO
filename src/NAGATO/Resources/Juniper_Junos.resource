*** Comments ***
Copyright 2024 ITOCHU Techno-Solutions Corporation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


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
