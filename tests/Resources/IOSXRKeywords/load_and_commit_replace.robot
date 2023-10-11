*** Settings ***
Documentation    `Load And Commit Replace IOS-XR` Unittest

Variables    unittest.yml
Library    NAGATO.NetmikoLibrary
Resource    ../../../src/NAGATO/Resources/IOSXRKeywords.resource

Suite Setup    Connect    &{DUT_1}
Suite Teardown    Disconnect All


*** Test Cases ***
Success_01
    [Documentation]    All Argumets are correct

    Load And Commit Replace IOS-XR    file_path=disk0:plane_config.cfg    host=${DUT_1}[alias]

Fail_01
    [Documentation]    `file_path` is incorrect and the others are correct

    Run Keyword And Expect Error    Got an Error when loading wrong_filepath
    ...    Load And Commit Replace IOS-XR    file_path=wrong_filepath    host=${DUT_1}[alias]
