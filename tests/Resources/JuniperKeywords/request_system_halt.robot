*** Settings ***
Documentation       `Request System Halt` Unittest

Variables           unittest.yml
Resource            NAGATO/Resources/Juniper_Junos.resource

Suite Setup         Connect    &{JUNOS_1}
Suite Teardown      Disconnect All


*** Test Cases ***
Fail_01
    [Documentation]    `member` is incorrect and the others are correct
    Run Keyword And Expect Error    ReadTimeout:*    Request System Halt    member=wrong_member    alias=${JUNOS_1}[alias]

Fail_02
    [Documentation]    `routing-engine` is incorrect and the others are correct
    Run Keyword And Expect Error    ReadTimeout:*    Request System Halt    routing-engine=wrong_re    alias=${JUNOS_1}[alias]

Fail_03
    [Documentation]    `at-time` is incorrect and the others are correct
    Run Keyword And Expect Error    ReadTimeout:*    Request System Halt    at-time=at wrong_time    alias=${JUNOS_1}[alias]

Fail_04
    [Documentation]    `in-minutes` is incorrect and the others are correct
    Run Keyword And Expect Error    ReadTimeout:*    Request System Halt    in-minutes=in worng_min    alias=${JUNOS_1}[alias]

Fail_05
    [Documentation]    `media` is incorrect and the others are correct
    Run Keyword And Expect Error    ReadTimeout:*    Request System Halt    media=wrong_media    alias=${JUNOS_1}[alias]

Fail_06
    [Documentation]    `message` is incorrect and the others are correct
    Run Keyword And Expect Error    ReadTimeout:*    Request System Halt    message=wrong_msg    alias=${JUNOS_1}[alias]

Success_01
    [Documentation]    All arguments are collect

    Request System Halt    alias=${JUNOS_1}[alias]

    # Confirm not to be able to ssh connection to assert if halt successfully or not
    Disconnect    alias=${JUNOS_1}[alias]
    Run Keyword And Expect Error    EOFError    
    ...    Connect    alias=assert_halt    device_type=${JUNOS_1}[device_type]    host=${JUNOS_1}[host]    username=${JUNOS_1}[username]    password=${JUNOS_1}[password]
