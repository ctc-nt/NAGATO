*** Settings ***
Documentation    `Config File Should Exist IOS-XR` Unittest

Variables    unittest.yml
Library    NAGATO.NetmikoLibrary
Resource    ../../../src/NAGATO/Resources/IOSXRKeywords.resource

Suite Setup    Connect    &{DUT_1}
Suite Teardown    Disconnect All


*** Test Cases ***
Success_01
    [Documentation]    All Argumets are correct

    ${content} =    Get File Content IOS-XR    file_name=plane_config.cfg    host=${DUT_1}[alias]

    Should Not Be Empty    ${content}

Fail_01
    [Documentation]    `file_name` is incorrect and the others are correct

    Run Keyword And Expect Error    No such file
    ...    Get File Content IOS-XR    file_name=wrong_filename.cfg    host=${DUT_1}[alias]
