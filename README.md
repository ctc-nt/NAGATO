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
- [Reference](#reference)

Introduction
-------------
NAGATO provides components for network test automation. It is based on Robot Framework.  
The project is hosted on [GitHub](https://github.com/ctc-nt/NAGATO).

NAGATO provides the following:  
- Robot Framework tools for automating infrastructure tests
- System to automatically generate robot files for tests incorporating the created tools

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
| Cisco_IOS_XR.resource | Provides high-level keywords defining the basic operations of Cisco IOS-XR using NetmikoLibrary |
| Juniper_Junos.resource | Provides high-level keywords defining the basic operations of Junos using NetmikoLibrary |

Installation
------------
Execute the following command:
```
pip install git+https://github.com/ctc-nt/NAGATO@main
```

The command will also install the following latest-packages:
- [robotframework](https://pypi.org/project/robotframework/)
- [ixnetwork-restpy](https://pypi.org/project/ixnetwork-restpy/)
- [netmiko](https://pypi.org/project/netmiko/)
- [ntc-templates](https://pypi.org/project/ntc-templates/)
- [pysnmplib](https://pypi.org/project/pysnmplib/)

Usage
-----
To use NAGATO in Robot Framework tests,  
import the libraries you want to use in the settings section.

One of the advantages to use Robot Framework  
in a form closer to Natural Language,  
so write tests as easy-to-understand as possible.

Below is an example of a robot file using NetmikoLibrary and Cisco_IOS_XR.resource.

```robotframework
*** Settings ***
Documentation          This example demonstrates executing a command on a remote machine
...                    and getting its output.
...
...                    Notice how connections are handled as part of the suite setup and
...                    teardown. This saves some time when executing several test cases.

Library                NAGATO.NetmikoLibrary
Resource               NAGATO/Resources/Cisco_IOS_XR.resource
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

    ${parsed_output} =    NAGATO.NetmikoLibrary.Send Command    command_string=show version    use_textfsm=${True}  host=${device}[alias]
    Should Be Equal    ${output}[0][hardware]    ASR9K

Get Normalized Running Config
    [Documentation]    Get only the configuration contents that do not contain date data 
    ...                from the output of show running-config

    ${output} =    NAGATO.NetmikoLibrary.Send Command     command_string=show running-config    host=${device}[alias]
    ${normalized_config} =    Cisco_IOS_XR.Normalize Config Text    ${output}
    Builtin.Log    ${normalized_config}
```

Reference
----
- [Robot Framework Libraries docs](./docs/index.md)  
NAGATOで提供しているRobot Framework Librariesのキーワード一覧へのリンク
- [Contribution](./POLICIES_ja.md)  
NAGATOのリリースポリシーやコントリビューションについて記載したページへのリンク
