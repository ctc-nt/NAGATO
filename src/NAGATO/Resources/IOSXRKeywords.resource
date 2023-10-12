*** Settings ***
Documentation       High-level keywords for operating IOS-XR

Library             NAGATO.NetmikoLibrary
Library             Collections
Library             String


*** Keywords ***
Normalize Config Text IOS-XR
    [Documentation]    Converts the config to a line-by-line list and returns the list with unnecessary strings stripped.
    [Arguments]    ${config_text}

    @{stripped_config_list} =    Create List
    @{config_list} =    Split String    ${config_text}    separator=\n

    # In each element of config, remove unnecessary spaces at the beginning and end of the string and store them in a separate list
    FOR    ${config_line}    IN    @{config_list}
        ${stripped_line} =    Strip String    ${config_line}
        Collections.Append To List    ${stripped_config_list}    ${stripped_line}
    END

    # Returns a list that excludes elements beginning with !
    ${config_list_normalized_1} =    Get Matches    ${stripped_config_list}    regexp=^(?!\!).*$
    # Returns a list excluding elements containing the Building configuration string
    ${config_list_normalized_2} =    Get Matches    ${config_list_normalized_1}    regexp=^(?!.*Building\\sconfiguration).*$
    # Returns a list excluding elements with time
    ${config_completed_normalization} =    Get Matches    ${config_list_normalized_2}    regexp=^(?!.*\\d{2}:\\d{2}:\\d{2}\.\\d{3}\\s\\w{3}).*$
    Remove Values From List    ${config_completed_normalization}    ${EMPTY}
    BuiltIn.Log    ${config_completed_normalization}
    RETURN    @{config_completed_normalization}

Running Config Should Be Equal IOS-XR
    [Documentation]    Verify that the output of show running-config is as expected.
    [Arguments]    ${expect_config}    ${host}

    BuiltIn.Log    ${expect_config}
    ${running_config} =    NAGATO.NetmikoLibrary.Send Command    command_string=show running-config    host=${host}

    ${expect_config_list} =    Normalize Config Text IOS-XR    ${expect_config}
    ${running_config_list} =    Normalize Config Text IOS-XR    ${running_config}

    Lists Should Be Equal    ${expect_config_list}    ${running_config_list}

Load And Commit Replace IOS-XR
    [Documentation]    Load ${file_path} and commit replace
    [Arguments]    ${file_path}    ${host}

    NAGATO.NetmikoLibrary.Enter Config Mode    host=${host}

    # Load and Commit Repalce
    ${load_output} =    NAGATO.NetmikoLibrary.Send Command    command_string=load ${file_path}    host=${host}

    ${result} =    Run Keyword And Return Status
    ...    Should Contain    ${load_output}    ERROR

    IF    ${result}    Fail    msg=Got an Error when loading ${file_path}

    NAGATO.NetmikoLibrary.Send Command    command_string=commit replace    expect_string=\\[no\\]:    host=${host}

    NAGATO.NetmikoLibrary.Write Channel    out_data=yes${\n}    host=${host}

    NAGATO.NetmikoLibrary.Read Until Pattern    pattern=\\(config\\)#    host=${host}

    NAGATO.NetmikoLibrary.Exit Config Mode    host=${host}

Get File Content IOS-XR
    [Documentation]    Get and return the content of file_name
    [Arguments]    ${file_name}    ${host}

    ${content} =    NAGATO.NetmikoLibrary.Send Command    command_string=run cat ${file_name}    host=${host}

    ${result} =    Run Keyword And Return Status
    ...    Should Contain    ${content}    No such file or directory

    IF    ${result}    Fail    msg=No such file
    RETURN    ${content}
