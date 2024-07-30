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
Documentation       High-level keywords for operating Cisco IOS-XR

Library             NAGATO.NetmikoLibrary
Library             Collections
Library             String


*** Keywords ***
Normalize Config Text
    [Documentation]    Converts the config to a line-by-line list and returns the list with unnecessary strings stripped.
    [Arguments]    ${config_text}

    @{stripped_config_list} =    Create List
    @{config_list} =    Split String    ${config_text}    separator=\n

    # In each element of config, remove unnecessary spaces at the beginning and end of the string and store them in a separate list
    FOR    ${config_line}    IN    @{config_list}
        ${stripped_line} =    Strip String    ${config_line}
        Collections.Append To List    ${stripped_config_list}    ${stripped_line}
    END

    # Strips strings beginning with "!"
    ${config_list_normalized_1} =    Get Matches    ${stripped_config_list}    regexp=^(?!\!).*$
    # Strips a Building configuration string
    ${config_list_normalized_2} =    Get Matches    ${config_list_normalized_1}    regexp=^(?!.*Building\\sconfiguration).*$
    # Strips timestamps
    ${config_completed_normalization} =    Get Matches    ${config_list_normalized_2}    regexp=^(?!.*\\d{2}:\\d{2}:\\d{2}\.\\d{3}\\s\\w{3}).*$
    # Strips empty lines
    Remove Values From List    ${config_completed_normalization}    ${EMPTY}

    RETURN    @{config_completed_normalization}

Running Config Should Be Equal
    [Documentation]    Checks that the output of show running-config is as expected.
    [Arguments]    ${expect_config}    ${alias}

    ${running_config} =    NAGATO.NetmikoLibrary.Send Command    command_string=show running-config    alias=${alias}

    ${expect_config_list} =    Normalize Config Text    ${expect_config}
    ${running_config_list} =    Normalize Config Text    ${running_config}

    Sort List    ${expect_config_list}
    Sort List    ${running_config_list}

    Lists Should Be Equal    ${expect_config_list}    ${running_config_list}

Load And Commit Replace
    [Documentation]    Executes "load ${file_path}" and "commit replace".
    [Arguments]    ${file_path}    ${alias}

    NAGATO.NetmikoLibrary.Enter Config Mode    alias=${alias}

    # Load and Commit Replace
    ${load_output} =    NAGATO.NetmikoLibrary.Send Command    command_string=load ${file_path}    alias=${alias}

    ${result} =    Run Keyword And Return Status
    ...    Should Contain    ${load_output}    ERROR

    IF    ${result}    Fail    msg=Got an Error when loading ${file_path}

    NAGATO.NetmikoLibrary.Send Command    command_string=commit replace    expect_string=\\[no\\]:    alias=${alias}

    NAGATO.NetmikoLibrary.Write Channel    out_data=yes${\n}    alias=${alias}

    NAGATO.NetmikoLibrary.Read Until Pattern    pattern=\\(config\\)#    alias=${alias}

    NAGATO.NetmikoLibrary.Exit Config Mode    alias=${alias}

Get File Content
    [Documentation]    Get and return the content of file_name.
    [Arguments]    ${file_name}    ${alias}

    ${content} =    NAGATO.NetmikoLibrary.Send Command    command_string=run cat ${file_name}    alias=${alias}

    ${result} =    Run Keyword And Return Status
    ...    Should Contain    ${content}    No such file or directory

    IF    ${result}    Fail    msg=No such file
    RETURN    ${content}
