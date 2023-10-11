*** Settings ***
Documentation    High-level keywords for operating IOS-XR

Library    NAGATO.NetmikoLibrary
Library    Collections
Library    String


*** Keywords ***
Normalize Config Text IOS-XR
    [Documentation]    Converts the config to a line-by-line list and returns the list with unnecessary strings stripped.
    [Arguments]    ${config_text}
    [Return]    @{config_completed_normalization}

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

Running Config Should Be Equal IOS-XR
    [Documentation]    Verify that the output of show running-config is as expected.
    [Arguments]    ${expect_config}    ${host}

    BuiltIn.Log    ${expect_config}
    ${running_config} =    NAGATO.NetmikoLibrary.Send Command    command_string=show running-config    host=${host}

    ${expect_config_list} =    Normalize Config Text IOS-XR    ${expect_config}
    ${running_config_list} =    Normalize Config Text IOS-XR    ${running_config}
    
    Lists Should Be Equal    ${expect_config_list}    ${running_config_list}

Config File Should Exist IOS-XR
    [Documentation]    check and return content of config file
    [Arguments]    ${config_directory_path}    ${file_name}    ${host}

    ${output} =    NAGATO.NetmikoLibrary.Send Command    command_string=dir ${config_directory_path}    host=${host}

    @{stripped_output} =    Create List
    @{splitted_output} =    Split String    ${output}    separator=\n

    # In each element of config, remove unnecessary spaces at the beginning and end of the string and store them in a separate list
    FOR    ${line}    IN    @{splitted_output}
        ${stripped_line} =    Strip String    ${line}
        Collections.Append To List    ${stripped_output}    ${stripped_line}
    END

    # Returns a list that has only one element including file_name
    ${matching_element} =    Get Matches    ${stripped_output}    regexp=^.*\\s${file_name}$

    ${matching_count} =    Get Length    ${matching_element}

    Length Should Be    1    ${matching_count}

Load And Commit Replace IOS-XR
    [Documentation]    Load ${file_path} and commit replace
    [Arguments]    ${file_path}    ${host}

    # Enter Configuring Mode
    NAGATO.NetmikoLibrary.Send Command    command_string=configure terminal    expect_string=\\(config\\)#    host=${host}

    # Load and Commit Repalce
    ${load_output} =    NAGATO.NetmikoLibrary.Send Command    command_string=load ${file_path}    host=${host}

    ${result} =    Run Keyword And Return Status
    ...            Should Contain    ${load_output}    ERROR

    IF    ${result}
        Fail    msg=Got an Error when loading ${file_path}
    END

    NAGATO.NetmikoLibrary.Send Command    command_string=commit replace    expect_string=\\[no\\]:    host=${host}

    NAGATO.NetmikoLibrary.Write Channel    out_data=yes${\n}    host=${host}

    # Exit Configuring Mode
    NAGATO.NetmikoLibrary.Send Command    command_string=end    expect_string=#    host=${host}

Get File Content IOS-XR
    [Documentation]    Get and return the content of file_name
    [Arguments]    ${file_name}    ${host}
    [Return]    ${content}

    ${content} =    NAGATO.NetmikoLibrary.Send Command    command_string=run cat ${file_name}    host=${host}

    ${result} =    Run Keyword And Return Status
    ...            Should Contain    ${content}    No such file or directory

    IF    ${result}
        Fail    msg=No such file
    END
