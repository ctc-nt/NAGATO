*** Settings ***
Documentation       `Load And Commit Replace` Unittest

Variables           unittest.yml
Library             NAGATO.NetmikoLibrary
Resource            NAGATO/Resources/Cisco_IOS_XR.resource

Suite Setup         Connect    &{DUT_1}
Suite Teardown      Disconnect All


*** Test Cases ***
Success_01
    [Documentation]    All Arguments are correct

    Load And Commit Replace    file_path=disk0:plane_config.cfg    alias=${DUT_1}[alias]

Fail_01
    [Documentation]    `file_path` is incorrect and the others are correct

    Run Keyword And Expect Error    Got an Error when loading wrong_filepath
    ...    Load And Commit Replace    file_path=wrong_filepath    alias=${DUT_1}[alias]
