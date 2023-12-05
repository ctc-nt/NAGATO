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
  RA DNS Search list Count: 0
"""
