![nagato](/images/Nagato_Logo_Horizontal.png)

NAGATO
===============
Network Automation Gears and Test Orchestrator.

Contents
- [Introduction](#introduction)
- [Libraries](#libraries)
- [High-Level Keywords](#high-level-keywords)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)

Introduction
-------------
NAGATO provides components for network test automation, that is based on Robot Framework.  
The project is hosted on [GitHub](https://github.com/ctc-nt/NAGATO).

NAGATO provides the following:  
- Robot Framework tools dedicated to automating infrastructure tests
- System to automatically generate tests incorporating the created tools

![nagato](/images/Nagato_Scope_of_Provision.png)

Libraries
-------------
The RobotFramework Libraries in NAGATO is the following:

 LIBRARY NAME | DESCRIPTION |
| ---- | ---- |
| IxNetworkLibrary | Provide operations on IxNetwork |
| NetmikoLibrary | Provide operations on network devices through ssh/telent connections |
| NetworkUtils | Provide various operations from the terminal |

For general information about using test libraries with Robot Framework, see
[Robot Framework User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#using-test-libraries).

High-Level Keywords
-------------
The RobotFramework resource files in NAGATO is the following:

 LIBRARY NAME | DESCRIPTION |
| ---- | ---- |
| IOSXRKeywords.resource | Provides high-level keywords defining the basic operations of IOSXR using NetmikoLibrary |


Installation
------------
The recommended installation method is using pip:
```
pip install git+https://github.com/ctc-nt/NAGATO@main
```

This command will also install the latest of the following packages:
- [robotframework](https://pypi.org/project/robotframework/)
- [ixnetwork-restpy](https://pypi.org/project/ixnetwork-restpy/)
- [netmiko](https://pypi.org/project/netmiko/)
- [ntc-templates](https://pypi.org/project/ntc-templates/)
- [pysnmplib](https://pypi.org/project/pysnmplib/)

Usage
-----
To use NAGATO in Robot Framework tests,  
you must import the libraries　you want to use using the library settings.

One of the advantages of the Robot Framework is that it can be written  
in a form similar to natural language,  
so write tests that are as easy-to-understand as possible.

Below is an example of a robot file created using NetmikoLibrary and IOSXRKeywords.resource.

```robotframework
*** Settings ***
Documentation          This example demonstrates executing a command on a remote machine
...                    and getting its output.
...
...                    Notice how connections are handled as part of the suite setup and
...                    teardown. This saves some time when executing several test cases.

Library                NAGATO.NetmikoLibrary
Resource               NAGATO/Resources/IOSXRKeywords.resource
Suite Setup            Connect   &{device}
Suite Teardown         Disconnect All

*** Variables ***
&{device}
...    device_type=cisco_xr
...    host=192.0.2.1
...    alias=test
...    username=test
...    password=test

*** Test Cases ***
Execute Command And Verify Parsed Output
    [Documentation]    Send the command, get the parsed output, and verify that it is as expected
    ...                If parsing is not needed, the use_textfsm argument is not necessary.

    ${parsed_output} =    NAGATO.NetmikoLibrary.Send Command    command_string=show version    use_textfsm=${True}
    Should Be Equal    ${output}[0][hardware]    ASR9K

Get Normalized Running Config
    [Documentation]    Get only the configuration contents that do not contain date data 
    ...                from the output of show running-config

    ${output} =    NAGATO.NetmikoLibrary.Send Command     command_string=show running-config
    ${normalized_config} =    IOSXRKeywords.Normalize Config Text IOS-XR    ${output}
    Builtin.Log    ${normalized_config}
```

Support
-----