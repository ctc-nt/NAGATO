*** Settings ***
Library    NAGATO.IxNetworkLibrary
Library    NAGATO.NetmikoLibrary
Library    NAGATO.NetworkUtils
Resource    NAGATO/Resources/IOSXRKeywords.resource


*** Test Cases ***
sample_01
    [Documentation]   sample of NAGATO.NetmikoLibrary's Keywords
    [Setup]    NAGATO.NetmikoLibrary.Connect    device_type=cisco_ios    host=172.17.17.179    alias=sample    username=cisco    password=cisco

    NAGATO.NetmikoLibrary.Send Command    command_string=show version    host=sample

    # パーサが必要な場合は、use_textfsm=Trueにするだけ
    [Teardown]    NAGATO.NetmikoLibrary.Disconnect All

sample_02
    [Documentation]    sample of NAGATO/Resources/IOSXRKeywords.resource's Keywords

    ${normalized_config} =    Normalize Config Text IOS-XR    config_text=${sample_config}
    Log Many    ${normalized_config}



*** Variables ***
${sample_config} =   
...    hostname NCS560_WSE
...    clock timezone JST Asia/Tokyo
...    username cisco
...     group root-lr
...     group cisco-support
...     password 7 070C285F4D06
...    !
...    line console
...     exec-timeout 0 0
...    !
...    line default
...     exec-timeout 0 0
...     session-limit 10
...     session-timeout 0
...     transport input all
...    !
...    vty-pool default 0 99 line-template default
...    ntp
...     server vrf MGMT 192.168.0.141
...     update-calendar
...    !
...    interface Bundle-Ether10
...    !
...    interface Bundle-Ether10.100 l2transport
...     encapsulation dot1q 100
...    !
...    interface MgmtEth0/RP0/CPU0/0
...     description To_Kanri-SW
...     ipv4 address 192.168.0.124 255.255.255.0
...    !
...    interface TenGigE0/2/0/0
...     bundle id 10 mode on
...    !
...    interface TenGigE0/2/0/1
...     bundle id 10 mode on
...    !
...    interface TenGigE0/2/0/2
...     bundle id 10 mode on
...    !
...    interface TenGigE0/2/0/3
...     bundle id 10 mode on
...    !
...    interface TenGigE0/4/0/7.100 l2transport
...     encapsulation dot1q 100
...    !
...    l2vpn
...     bridge group bg1
...      bridge-domain bd1
...       interface Bundle-Ether10.100
...       !
...       interface TenGigE0/4/0/7.100
...       !
...      !
...     !
...    !
...    ssh client source-interface Loopback0
...    ssh timeout 120
...    ssh server rate-limit 600
...    ssh server session-limit 100
...    ssh server v2
...    ssh server vrf MGMT
...    ssh server vrf default
...    ssh server vrf mgmt_DNET
...    telnet vrf MGMT ipv4 server max-servers 10
...    telnet vrf default ipv4 server max-servers 20
...    end
