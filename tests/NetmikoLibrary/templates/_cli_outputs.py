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

# show ntp associations

show_ntp_associations = """\
Wed Jul 30 04:03:13.471 PST DST
  
     address         ref clock     st  when  poll reach  delay  offset    disp
*~172.19.69.1      172.24.114.33     3    25    64    3    2.89  57550122  39377
 ~2001:db8::feed   .INIT.           16     -    64    0    0.00   -15.0   15937
 ~2001:db8::beef vrf vrf_1
                  .INIT.           16     -    64    0    0.00   0.000   16.0
* sys_peer, # selected, + candidate, - outlayer, x falseticker, ~ configured"""

# show protocols ipv4 ospf

show_protocols_ipv4_ospf = """\
Routing Protocol OSPF 1
  Router Id: 55.55.55.55
  Distance: 110
  Non-Stop Forwarding: Enabled
  Redistribution:
    connected
    isis 3
  Area 0
    MPLS/TE enabled
    GigabitEthernet 0/3/0/3
    Loopback0
  Area 1
    Loopback1

Routing Protocol OSPF 2
  Router Id: 3.3.3.3
  Distance: 110
  Non-Stop Forwarding: Disabled
  Redistribution:
    None
  Area 0
    Loopback3"""

# show protocols ipv6 ospfv3

show_protocols_ipv6_ospf = """\
Routing Protocol OSPFv3 1
  Router Id: 10.0.0.1
  Distance: 110
  Graceful Restart: Enabled
  Redistribution:
    None
  Area 0
    HundredGigE 0/2/0/2
    Loopback1
  Area 1
    Loopback2

Routing Protocol OSPFv3 2
  Router Id: 1.1.1.1
  Distance: 110
  Graceful Restart: Disabled
  Redistribution:
    None
  Area 0
    Loopback3
"""

# show route ipv4 summary

show_route_ipv4_summary = """\
Mon Feb 16 01:42:20.842 JST
Route Source                     Routes     Backup     Deleted     Memory(bytes)
connected                        1          1          0           432          
local                            2          0          0           432          
application fib_mgr              0          0          0           0            
dagr                             0          0          0           0            
static                           0          0          0           0            
vxlan                            0          0          0           0            
ospf 1                           0          0          0           0            
Total                            3          1          0           864"""

show_route_ipv6_summary = """\
Thu Dec 28 08:23:03.504 UTC
Route Source                     Routes     Backup     Deleted     Memory(bytes)
local-iid sidmgr                 0          0          0           0            
connected                        1          0          0           216          
connected l2tpv3_xconnect        0          0          0           0            
local                            1          0          0           216          
local-srv6 xtc_srv6              0          0          0           0            
static                           0          0          0           0            
vxlan                            0          0          0           0            
ospf 1                           0          0          0           0            
ospf 2                           0          0          0           0            
Total                            2          0          0           432"""

# show ospfv3 neighbor
show_ospfv3_neighbor = """\
Mon Feb 16 01:42:20.842 JST

* Indicates MADJ interface

Neighbors for OSPFv3 TEST

Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2         1     FULL/BDR        00:00:36    192.168.1.2     GigabitEthernet0/0/0/5
    Neighbor is up for 00:18:29
192.168.16.10   5     FULL/DR          0:00:33    192.168.48.189      GigabitEthernet 0/3/0/3
    Neighbor is up for 18:45:27

Total neighbor count: 2"""

show_lacp_io = """\
Fri Jan 12 18:24:45.565 JST
Bundle-Ether1

Interface TenGigE0/0/0/38
-------------------------
Interface handle:            0x04000f40
Interface media type:        Ethernet
Periodic transmit interval:  30000ms
Requested transmit interval: 0ms
Source MAC address:          4014.823b.f6e6
Actor system:   0x8000, 90-88-55-5a-b8-ec
Actor key:      0x0001
Actor port:     0x8000, 0x0002
Actor state:     Act  (T/o)  Agg   Sync   Coll   Dist  (Def) (Exp)
Partner system: 0x8000, 34-88-18-cf-40-63
Partner key:    0x0001
Partner port:   0x8000, 0x0002
Partner state:   Act  (T/o)  Agg   Sync   Coll   Dist  (Def) (Exp)
Collector max delay:   65535

Interface TenGigE0/0/0/39
-------------------------
Interface handle:            0x04000f80
Interface media type:        Ethernet
Periodic transmit interval:  30000ms
Requested transmit interval: 0ms
Source MAC address:          4014.823b.f6e7
Actor system:   0x8000, 90-88-55-5a-b8-ec
Actor key:      0x0001
Actor port:     0x8000, 0x0001
Actor state:     Act  (T/o)  Agg   Sync   Coll   Dist  (Def) (Exp)
Partner system: 0x8000, 34-88-18-cf-40-63
Partner key:    0x0001
Partner port:   0x8000, 0x0001
Partner state:   Act  (T/o)  Agg   Sync   Coll   Dist  (Def) (Exp)
Collector max delay:   65535

Bundle-Ether2

Interface HundredGigE0/1/0/42
-----------------------------
Interface handle:            0x06000240
Interface media type:        Ethernet
Periodic transmit interval:  1000ms
Requested transmit interval: 0ms
Source MAC address:          4cec.0f1f.1054
Actor system:   0x8000, 90-88-55-5a-b8-ec
Actor key:      0x0002
Actor port:     0x8000, 0x0004
Actor state:     Act   T/o   Agg   Sync   Coll   Dist  (Def) (Exp)
Partner system: 0x8000, 34-88-18-cf-40-63
Partner key:    0x0002
Partner port:   0x8000, 0x0004
Partner state:   Act   T/o   Agg   Sync   Coll   Dist  (Def) (Exp)
Collector max delay:   65535"""

show_ospf = """\
Wed Jan 24 06:41:09.455 UTC
 Routing Process "ospf 10" with ID 2.2.2.2
 Role: Primary Active
 NSR (Non-stop routing) is Enabled
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 Router is not originating router-LSAs with maximum metric
 Initial SPF schedule delay 50 msecs
 Minimum hold time between two consecutive SPFs 200 msecs
 Maximum wait time between two consecutive SPFs 5000 msecs
 Initial LSA throttle delay 50 msecs
 Minimum hold time for LSA throttle 200 msecs
 Maximum wait time for LSA throttle 5000 msecs
 Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
 LSA refresh interval 1800 seconds
 Flood pacing interval 33 msecs. Retransmission pacing interval 66 msecs
 Adjacency stagger enabled; initial (per area): 2, maximum: 64
    Number of neighbors forming: 0, 0 full
 Maximum number of configured interfaces 1024
 Number of external LSA 0. Checksum Sum 00000000
 Number of opaque AS LSA 0. Checksum Sum 00000000
 Number of DCbitless external and opaque AS LSA 0
 Number of DoNotAge external and opaque AS LSA 0
 Number of areas in this router is 1. 1 normal 0 stub 0 nssa
 External flood list length 0
 SNMP trap is enabled
 LSD not connected, revision 0
 Segment Routing Global Block default (16000-23999), not allocated
 Segment Routing Local Block, unknown
 Strict-SPF capability is enabled
    Area BACKBONE(0) (Inactive)
	    Number of interfaces in this area is 0
	    It is a NSSA area
	    SPF algorithm executed 1 times
	    Number of LSA 0.  Checksum Sum 00000000
	    Number of opaque link LSA 0.  Checksum Sum 00000000
	    Number of DCbitless LSA 0
	    Number of indication LSA 0
	    Number of DoNotAge LSA 0
	    Flood list length 0
	    Number of LFA enabled interfaces 0, LFA revision 0
	    Number of Per Prefix LFA enabled interfaces 0
	    Number of neighbors forming in staggered mode 0, 0 full
    Area 10
	    Number of interfaces in this area is 0
	    It is a NSSA area
	    SPF algorithm executed 1 times
	    Number of LSA 0.  Checksum Sum 00000000
	    Number of opaque link LSA 0.  Checksum Sum 00000000
	    Number of DCbitless LSA 0
	    Number of indication LSA 0
	    Number of DoNotAge LSA 0
	    Flood list length 0
	    Number of LFA enabled interfaces 0, LFA revision 0
	    Number of Per Prefix LFA enabled interfaces 0
	    Number of neighbors forming in staggered mode 0, 0 full

 Routing Process "ospf 20" with ID 2.2.2.2
 Role: Primary Active
 NSR (Non-stop routing) is Enabled
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 Router is not originating router-LSAs with maximum metric
 Initial SPF schedule delay 50 msecs
 Minimum hold time between two consecutive SPFs 200 msecs
 Maximum wait time between two consecutive SPFs 5000 msecs
 Initial LSA throttle delay 50 msecs
 Minimum hold time for LSA throttle 200 msecs
 Maximum wait time for LSA throttle 5000 msecs
 Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
 LSA refresh interval 1800 seconds
 Flood pacing interval 33 msecs. Retransmission pacing interval 66 msecs
 Adjacency stagger enabled; initial (per area): 2, maximum: 64
    Number of neighbors forming: 0, 0 full
 Maximum number of configured interfaces 1024
 Number of external LSA 0. Checksum Sum 00000000
 Number of opaque AS LSA 0. Checksum Sum 00000000
 Number of DCbitless external and opaque AS LSA 0
 Number of DoNotAge external and opaque AS LSA 0
 Number of areas in this router is 1. 1 normal 0 stub 0 nssa
 External flood list length 0
 SNMP trap is enabled
 LSD not connected, revision 0
 Segment Routing Global Block default (16000-23999), not allocated
 Segment Routing Local Block, unknown
 Strict-SPF capability is enabled
    Area BACKBONE(0) (Inactive)
	    Number of interfaces in this area is 0
	    It is a NSSA area
	    SPF algorithm executed 1 times
	    Number of LSA 0.  Checksum Sum 00000000
	    Number of opaque link LSA 0.  Checksum Sum 00000000
	    Number of DCbitless LSA 0
	    Number of indication LSA 0
	    Number of DoNotAge LSA 0
	    Flood list length 0
	    Number of LFA enabled interfaces 0, LFA revision 0
	    Number of Per Prefix LFA enabled interfaces 0
	    Number of neighbors forming in staggered mode 0, 0 full
    Area 20
	    Number of interfaces in this area is 0
	    It is a NSSA area
	    SPF algorithm executed 1 times
	    Number of LSA 0.  Checksum Sum 00000000
	    Number of opaque link LSA 0.  Checksum Sum 00000000
	    Number of DCbitless LSA 0
	    Number of indication LSA 0
	    Number of DoNotAge LSA 0
	    Flood list length 0
	    Number of LFA enabled interfaces 0, LFA revision 0
	    Number of Per Prefix LFA enabled interfaces 0
	    Number of neighbors forming in staggered mode 0, 0 full"""

show_ospfv3 = """\
Wed Jan 24 06:51:58.760 UTC
 Routing Process "ospfv3 10" with ID 2.2.2.2
 Role: Primary Active
 NSR (Non-stop routing) is Enabled
 Initial SPF schedule delay 50 msecs
 Minimum hold time between two consecutive SPFs 200 msecs
 Maximum wait time between two consecutive SPFs 5000 msecs
 Initial LSA throttle delay 50 msecs
 Minimum hold time for LSA throttle 200 msecs
 Maximum wait time for LSA throttle 5000 msecs
 Minimum LSA arrival 100 msecs
 LSA group pacing timer 240 secs
 Interface flood pacing timer 33 msecs
 Retransmission pacing timer 66 msecs
 Maximum number of configured interfaces 1024
 Maximum number of configured paths 64
 Number of external LSA 0. Checksum Sum 00000000
 Number of areas in this router is 1. 1 normal 0 stub 0 nssa
 Auto cost is enabled. Reference bandwidth 100
 SNMP trap is enabled
    Area BACKBONE(0) (Inactive)
        Number of interfaces in this area is 0
	      It is a NSSA area
        SPF algorithm executed 0 times
        Number of LSA 0. Checksum Sum 00000000
        Number of DCbitless LSA 0
        Number of indication LSA 0
        Number of DoNotAge LSA 0
        Flood list length 0
        Number of LFA enabled interfaces 0, LFA revision 0
        Number of Per Prefix LFA enabled interfaces 0
    Area 10
	      Number of interfaces in this area is 0
	      It is a NSSA area
	      SPF algorithm executed 1 times
	      Number of LSA 0.  Checksum Sum 00000000
	      Number of opaque link LSA 0.  Checksum Sum 00000000
	      Number of DCbitless LSA 0
	      Number of indication LSA 0
	      Number of DoNotAge LSA 0
	      Flood list length 0
	      Number of LFA enabled interfaces 0, LFA revision 0
	      Number of Per Prefix LFA enabled interfaces 0
	      Number of neighbors forming in staggered mode 0, 0 full

 Routing Process "ospfv3 20" with ID 2.2.2.2
 Role: Primary Active
 NSR (Non-stop routing) is Enabled
 Initial SPF schedule delay 50 msecs
 Minimum hold time between two consecutive SPFs 200 msecs
 Maximum wait time between two consecutive SPFs 5000 msecs
 Initial LSA throttle delay 50 msecs
 Minimum hold time for LSA throttle 200 msecs
 Maximum wait time for LSA throttle 5000 msecs
 Minimum LSA arrival 100 msecs
 LSA group pacing timer 240 secs
 Interface flood pacing timer 33 msecs
 Retransmission pacing timer 66 msecs
 Maximum number of configured interfaces 1024
 Maximum number of configured paths 64
 Number of external LSA 0. Checksum Sum 00000000
 Number of areas in this router is 1. 1 normal 0 stub 0 nssa
 Auto cost is enabled. Reference bandwidth 100
 SNMP trap is enabled
    Area BACKBONE(0) (Inactive)
        Number of interfaces in this area is 0
	      It is a NSSA area
        SPF algorithm executed 0 times
        Number of LSA 0. Checksum Sum 00000000
        Number of DCbitless LSA 0
        Number of indication LSA 0
        Number of DoNotAge LSA 0
        Flood list length 0
        Number of LFA enabled interfaces 0, LFA revision 0
        Number of Per Prefix LFA enabled interfaces 0
    Area 20
	      Number of interfaces in this area is 0
	      It is a NSSA area
	      SPF algorithm executed 1 times
	      Number of LSA 0.  Checksum Sum 00000000
	      Number of opaque link LSA 0.  Checksum Sum 00000000
	      Number of DCbitless LSA 0
	      Number of indication LSA 0
	      Number of DoNotAge LSA 0
	      Flood list length 0
	      Number of LFA enabled interfaces 0, LFA revision 0
	      Number of Per Prefix LFA enabled interfaces 0
	      Number of neighbors forming in staggered mode 0, 0 full"""

# show access-lists interface

show_access_lists_interface = """\
Mon Jan 22 11:32:28.599 JST
Input ACL (common): N/A (interface): N/A
Output ACL: Test-ACL_1 """


show_bgp_sessions = """\
Fri Jan 26 00:49:33.172 UTC

Neighbor        VRF                   Spk    AS   InQ  OutQ  NBRState     NSRState
10.10.10.1      default                 0   100     0     0  Idle         None
20.20.20.1      default                 0   100     0     0  Idle         None"""

# show ospf interface

show_ospf_interface = """\
Wed Feb  7 15:42:30.033 JST

Interfaces for OSPF 1

TenGigE0/0/0/38 is up, line protocol is up 
  Internet Address 10.10.10.2/24, Area 0, SID 0, Strict-SPF SID 0
  Label stack Primary label 0 Backup label 0 SRTE label 0
  Process ID 1, Router ID 2.2.2.2, Network Type BROADCAST, Cost: 10
  Transmit Delay is 1 sec, State WAITING, Priority 10, MTU 1500, MaxPktSz 1500
  Forward reference No, Unnumbered no,  Bandwidth 10000000 
  RIB LC sync Yes
  No designated router on this network
  No backup designated router on this network
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    Hello due in 00:00:00:009
    Wait time before Designated router selection 00:00:20
  Index 1/1, flood queue length 0
  Next 0(0)/0(0)
  Last flood scan length is 0, maximum is 0
  Last flood scan time is 0 msec, maximum is 0 msec
  LS Ack List: current length 0, high water mark 0
  Neighbor Count is 0, Adjacent neighbor count is 0
  Suppress hello for 0 neighbor(s)
  Multi-area interface Count is 0
  Segment Routing Forwarding MPLS enabled: Yes
Loopback1 is up, line protocol is up
  Internet Address 2.2.2.2/32, Area 0, SID 0, Strict-SPF SID 0
  Label stack Primary label 0 Backup label 0 SRTE label 0
  Process ID 1, Router ID 1.1.1.1, Network Type LOOPBACK, Cost: 1
  Loopback interface is treated as a stub Host
  Transmit Delay is 1 sec, State WAITING, Priority 110, MTU 1500, MaxPktSz 1500
  Forward reference No, Unnumbered no,  Bandwidth 10000000 
  RIB LC sync Yes
  No designated router on this network
  No backup designated router on this network
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    Hello due in 00:00:00:009
    Wait time before Designated router selection 00:00:20
  Index 1/1, flood queue length 0
  Next 0(0)/0(0)
  Last flood scan length is 0, maximum is 0
  Last flood scan time is 0 msec, maximum is 0 msec
  LS Ack List: current length 0, high water mark 0
  Neighbor Count is 0, Adjacent neighbor count is 0
  Suppress hello for 0 neighbor(s)
  Multi-area interface Count is 0
  Segment Routing Forwarding MPLS enabled: Yes"""

# show ospfv3 interface

show_ospfv3_interface = """\
Wed Feb  7 15:43:50.379 JST

TenGigE0/0/0/38 is up, line protocol is up
  Link Local address fe80::4eec:fff:fee7:e3c6, Interface ID 42
  Area 0, Process ID 1, Instance ID 0, Router ID 2.2.2.2
  Network Type BROADCAST, Cost: 10
  Bandwidth : 10000000
  RIB LC sync Yes
  Transmit Delay is 1 sec, State WAITING, MTU 1500,  Priority 10 
  No designated router on this network
  No backup designated router on this network
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    Hello due in 00:00:03
    Wait time before Designated router selection 00:00:23
  Index 1/1/1, flood queue length 0
  Next 0(0)/0(0)/0(0)
  Last flood scan length is 0, maximum is 0
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 0, Adjacent neighbor count is 0
  Suppress hello for 0 neighbor(s)
  Reference count is 2 
TenGigE0/0/0/39 is up, line protocol is up
  Link Local address fe80::4eec:fff:fee7:e3c6, Interface ID 42
  Area 0, Process ID 1, Instance ID 0, Router ID 1.1.1.1
  Network Type BROADCAST, Cost: 10
  Bandwidth : 10000000
  RIB LC sync Yes
  Transmit Delay is 1 sec, State WAITING, MTU 1500,  Priority 110 
  No designated router on this network
  No backup designated router on this network
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    Hello due in 00:00:03
    Wait time before Designated router selection 00:00:23
  Index 1/1/1, flood queue length 0
  Next 0(0)/0(0)/0(0)
  Last flood scan length is 0, maximum is 0
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 0, Adjacent neighbor count is 0
  Suppress hello for 0 neighbor(s)
  Reference count is 2 """

# show route ipv4

show_route_ipv4 = """\
Codes: C - connected, S - static, R - RIP, B - BGP
     D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
     N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
     E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
     i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
     ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
     U - per-user static route, o - ODR, L - local, G  - DAGR
     A - access/subscriber, (!) - FRR Backup path
  
Gateway of last resort is 1.0.0.1 to network 0.0.0.0
  
S*   0.0.0.0/0 [1/0] via 1.0.0.1, 13:14:59
C    1.0.0.0/16 is directly connected, 13:14:59, MgmtEth0/5/CPU0/0
L    1.0.14.15/32 is directly connected, 13:14:59, MgmtEth0/5/CPU0/0
O E2 5.2.5.0/24 [110/20] via 3.3.3.1, 00:04:20, GigabitEthernet0/3/0/0 
O E2 6.2.6.0/24 [110/20] via 3.3.3.1, 00:04:20, GigabitEthernet0/3/0/0
C    7.2.7.0/24 is directly connected, 00:04:20, GigabitEthernet0/3/0/7
L    7.2.7.2/32 is directly connected, 00:04:20, GigabitEthernet0/3/0/7
O E2 8.2.8.0/24 [110/20] via 3.3.3.1, 00:04:20, GigabitEthernet0/3/0/0
  
C    10.3.0.0/16 is directly connected, 13:14:59, GigabitEthernet0/0/0/0
L    10.3.0.2/32 is directly connected, 13:14:59, GigabitEthernet0/0/0/0"""
