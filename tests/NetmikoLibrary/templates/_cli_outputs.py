# show chassis environment

show_chassis_environment = """\
Class Item                           Status     Measurement
Temp  PEM 0                          OK         30 degrees C / 86 degrees F
      PEM 1                          OK         35 degrees C / 95 degrees F
      PEM 2                          Check     
      PEM 3                          Check     
      Routing Engine 0               OK         32 degrees C / 89 degrees F"""

# show chassis routing-engine

show_chassis_routing_engine = """\
Routing Engine status:
  Slot 0:
    Current state                  Master

Routing Engine status:
  Slot 1:
    Current state                  Backup"""

# show bundle bundle-ether

show_bundle_bundle_ether = """\
Bundle-Ether10
  Status:                                    Up
  Local links <active/standby/configured>:   2 / 0 / 2
  Local bandwidth <effective/available>:     110000000 (110000000) kbps
  MAC address (source):                      9088.555a.b8bb (Chassis pool)
  Inter-chassis link:                        No
  Minimum active links / bandwidth:          1 / 1 kbps
  Maximum active links:                      64
  Wait while timer:                          2000 ms
  Load balancing:                            
    Link order signaling:                    Not configured
    Hash type:                               Default
    Locality threshold:                      None
  LACP:                                      Not operational
    Flap suppression timer:                  Off
    Cisco extensions:                        Disabled
    Non-revertive:                           Disabled
  mLACP:                                     Not configured
  IPv4 BFD:                                  Not configured
  IPv6 BFD:                                  Not configured
  Port                  Device           State        Port ID         B/W, kbps
  --------------------  ---------------  -----------  --------------  ----------
  Te0/0/0/38            Local            Active       0x8000, 0x0000    10000000
      Link is Active
  Hu0/1/0/42            Local            Active       0x8000, 0x0000   100000000
      Link is Active"""

# show ethernet oam event-log

show_ethernet_oam_event_log = """\
Mon Dec  4 11:27:06.463 JST
Local Action Taken:
    N/A    - No action needed         EFD    - Interface brought down using EFD
    None   - No action taken          Err.D  - Interface error-disabled        
    Logged - System logged           

TenGigE0/0/0/38
================================================================================
                                                                       Breaching
Time                    Type                    Loc'n Action Threshold Value
----------------------- ----------------------- ----- ------ --------- ---------
Mon Dec 04 11:26:38 JST Dying gasp              Local Logged       N/A       N/A
Mon Dec 04 11:26:38 JST Frame fail              Local Logged       N/A       N/A

TenGigE0/0/0/39
================================================================================
                                                                       Breaching
Time                    Type                    Loc'n Action Threshold Value
----------------------- ----------------------- ----- ------ --------- ---------
Mon Dec 04 11:26:38 JST Frame                   Local Logged       N/A       N/A"""

# show ipv6 interface

show_ipv6_interface = """\
Mon Dec  4 14:26:35.893 JST
TenGigE0/0/0/1 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
  IPv6 is enabled, link-local address is fe80::4eec:fff:fe16:aa61 [TENTATIVE]
  Global unicast address(es):
    ::ffff:192.168.100.2, subnet is ::ffff:192.168.100.2/128 [TENTATIVE]
  Joined group address(es): ff02::2 ff02::1
  MTU is 1514 (1500 is available to IPv6)
  ICMP redirects are disabled
  ICMP unreachables are enabled
  ND DAD is enabled, number of DAD attempts 1
  ND reachable time is 0 milliseconds
  ND cache entry limit is 1000000000
  ND advertised retransmit interval is 0 milliseconds
  ND router advertisements are sent every 160 to 240 seconds
  ND router advertisements live for 1800 seconds
  Hosts use stateless autoconfig for addresses.
  Outgoing access list is not set
  Inbound  common access list is not set, access list is not set
  Table Id is 0xe0800000
  Complete protocol adjacency: 0
  Complete glean adjacency: 0
  Incomplete protocol adjacency: 0
  Incomplete glean adjacency: 0
  Dropped protocol request: 0
  Dropped glean request: 0
  RA DNS Server Address Count: 0
  RA DNS Search list Count: 0"""

# show access-lists

show_access_lists = """\
Tue Dec  5 19:16:06.952 JST
ipv4 access-list Test-ACL_1
 10 deny ipv4 host 172.17.17.20 any
 20 permit ipv4 172.17.17.0 0.0.0.255 any
ipv4 access-list Test-ACL_2
 10 permit tcp any 172.16.0.0 0.0.255.255 eq telnet
 20 deny tcp any any"""

# show bgp neighbors brief

show_bgp_neighbors_brief = """\
Thu Dec  7 11:03:46.913 JST

Neighbor        Spk    AS Description                          Up/Down  NBRState 
100.100.0.2       0   100                                      00:00:00 Active 
2001:10::2        0   100                                      00:56:58 Established 
10.10.10.10       0 65001 this is test thisistest 1            00:00:00 Idle """
