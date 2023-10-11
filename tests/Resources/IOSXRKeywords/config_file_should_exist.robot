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

    Config File Should Exist IOS-XR    config_directory_path=disk0:    file_name=plane_config.cfg    host=${DUT_1}[alias]

Fail_01
    [Documentation]    `config_directory_path` is incorrect and the others are correct

    Run Keyword And Expect Error    Length of '1' should be 0 but is 1.
    ...    Config File Should Exist IOS-XR    config_directory_path=wrong_directory    file_name=plane_config.cfg    host=${DUT_1}[alias]

Fail_02
    [Documentation]    `file_name` is incorrect and the others are correct

    Run Keyword And Expect Error    Length of '1' should be 0 but is 1.
    ...    Config File Should Exist IOS-XR    config_directory_path=disk0:    file_name=wrong_file.cfg    host=${DUT_1}[alias]

