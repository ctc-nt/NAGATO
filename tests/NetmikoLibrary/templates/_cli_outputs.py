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
 20 deny tcp any any
ipv6 access-list Test-ACL_3 
 10 permit tcp any any eq 1000 nexthop1 vrf test2 ipv6 ::"""

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

# show ospf vrf

show_ospf_vrf = """\
Tue Jan 23 17:55:39.055 JST

 VRF test active in Routing Process "ospf 10" with ID 2.2.2.2
 Role: Primary Active
 NSR (Non-stop routing) is Enabled
 Trigger RP Switchover on detectable process restart (if NSR active)
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 It is an area border router
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
    Number of neighbors forming: 1, 0 full
 Maximum number of configured interfaces 1024
 Number of external LSA 0. Checksum Sum 00000000
 Number of opaque AS LSA 0. Checksum Sum 00000000
 Number of DCbitless external and opaque AS LSA 0
 Number of DoNotAge external and opaque AS LSA 0
 Number of areas in this router is 1. 1 normal 0 stub 0 nssa
 External flood list length 0
 SNMP trap is disabled
 LSD not connected, revision 0
 Segment Routing Global Block default (16000-23999), not allocated
 Segment Routing Local Block, unknown
 Strict-SPF capability is enabled
    Area BACKBONE(0) (Inactive)
	Number of interfaces in this area is 1
	SPF algorithm executed 1 times
	Number of LSA 1.  Checksum Sum 0x00ac56
	Number of opaque link LSA 0.  Checksum Sum 00000000
	Number of DCbitless LSA 0
	Number of indication LSA 0
	Number of DoNotAge LSA 0
	Flood list length 0
	Number of LFA enabled interfaces 0, LFA revision 0
	Number of Per Prefix LFA enabled interfaces 0
	Number of neighbors forming in staggered mode 1, 0 full
  
   VRF test active in Routing Process "ospf 20" with ID 1.1.1.1
 Role: Primary Active
 NSR (Non-stop routing) is Enabled
 Trigger RP Switchover on detectable process restart (if NSR active)
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 It is an area border router
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
    Number of neighbors forming: 1, 0 full
 Maximum number of configured interfaces 1024
 Number of external LSA 0. Checksum Sum 00000000
 Number of opaque AS LSA 0. Checksum Sum 00000000
 Number of DCbitless external and opaque AS LSA 0
 Number of DoNotAge external and opaque AS LSA 0
 Number of areas in this router is 1. 1 normal 0 stub 0 nssa
 External flood list length 0
 SNMP trap is disabled
 LSD not connected, revision 0
 Segment Routing Global Block default (16000-23999), not allocated
 Segment Routing Local Block, unknown
 Strict-SPF capability is enabled
    Area BACKBONE(0) (Inactive)
	Number of interfaces in this area is 1
	SPF algorithm executed 1 times
	Number of LSA 1.  Checksum Sum 0x00ac56
	Number of opaque link LSA 0.  Checksum Sum 00000000
	Number of DCbitless LSA 0
	Number of indication LSA 0
	Number of DoNotAge LSA 0
	Flood list length 0
	Number of LFA enabled interfaces 0, LFA revision 0
	Number of Per Prefix LFA enabled interfaces 0
	Number of neighbors forming in staggered mode 1, 0 full"""

# show ospfv3 vrf

show_ospfv3_vrf = """\
Tue Jan 23 18:03:08.550 JST

 Routing Process "ospfv3 10" with ID 2.2.2.2 VRF test
 Role: Primary Active
 NSR (Non-stop routing) is Enabled
 Trigger RP Switchover on detectable process restart (if NSR active)
 It is an area border router
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
 SNMP trap is disabled
    Area BACKBONE(0)
        Number of interfaces in this area is 1
        SPF algorithm executed 1 times
        Number of LSA 3. Checksum Sum 0x012cd4
        Number of DCbitless LSA 0
        Number of indication LSA 0
        Number of DoNotAge LSA 0
        Flood list length 0
        Number of LFA enabled interfaces 0, LFA revision 0
        Number of Per Prefix LFA enabled interfaces 0
        

 Routing Process "ospfv3 20" with ID 1.1.1.1 VRF test
 Role: Primary Active
 NSR (Non-stop routing) is Enabled
 Trigger RP Switchover on detectable process restart (if NSR active)
 It is an area border router
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
 SNMP trap is disabled
    Area BACKBONE(0)
        Number of interfaces in this area is 1
        SPF algorithm executed 1 times
        Number of LSA 3. Checksum Sum 0x012cd4
        Number of DCbitless LSA 0
        Number of indication LSA 0
        Number of DoNotAge LSA 0
        Flood list length 0
        Number of LFA enabled interfaces 0, LFA revision 0
        Number of Per Prefix LFA enabled interfaces 0"""

show_bgp_sessions = """\
Fri Jan 26 00:49:33.172 UTC

Neighbor        VRF                   Spk    AS   InQ  OutQ  NBRState     NSRState
10.1.1.100      default                 0   200     0     0  Established  None
100.100.0.2     default                 0   100     0     0  Established  None
10:1:1::100     default                 0   200     0     0  Idle         None
100:100::2      default                 0   100     0     0  Idle         None"""

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

# show vrf all

show_vrf_all = """\
Tue Feb 20 15:20:51.163 JST
VRF                  RD                  RT                         AFI   SAFI     
MGMT                 not set            
test1                1:100              
test2                1:200              """

# show bgp ipv4 unicast neighbor

show_bgp_ipv4_unicast_neighbors = """\
BGP neighbor is 10.1.1.100
 Remote AS 200, local AS 100, external link
 Remote router ID 192.0.0.1
  BGP state = Established, up for 00:30:07
  NSR State: NSR Ready
  Last read 00:00:07, Last read before reset 00:00:00
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
  Last write 00:00:00, attempted 19, written 19
  Second last write 00:00:30, attempted 19, written 19
  Last write before reset 00:00:00, attempted 0, written 0
  Second last write before reset 00:00:00, attempted 0, written 0
  Last write pulse rcvd  Feb 29 00:01:28.888 last full not set pulse count 129
  Last write pulse rcvd before reset 00:00:00
  Socket not armed for io, armed for read, armed for write
  Last write thread event before reset 00:00:00, second last 00:00:00
  Last KA expiry before reset 00:00:00, second last 00:00:00
  Last KA error before reset 00:00:00, KA not sent 00:00:00
  Last KA start before reset 00:00:00, second last 00:00:00
  Precedence: internet
  Non-stop routing is enabled
  Enforcing first AS is enabled
  Multi-protocol capability received
  Neighbor capabilities:
    Route refresh: advertised (old + new) and received (new)
    4-byte AS: advertised
    Address family IPv4 Unicast: advertised and received
  Received 163 messages, 0 notifications, 0 in queue
  Sent 65 messages, 0 notifications, 0 in queue
  Minimum time between advertisement runs is 30 secs
  Inbound message logging enabled, 3 messages buffered
  Outbound message logging enabled, 3 messages buffered

 For Address Family: IPv4 Unicast
  BGP neighbor version 202
  Update group: 0.1 Filter-group: 0.1  No Refresh request being processed
    Extended Nexthop Encoding: advertised
  Route refresh request: received 0, sent 0
  Policy for incoming advertisements is pass
  Policy for outgoing advertisements is pass
  100 accepted prefixes, 100 are bestpaths
  Exact no. of prefixes denied : 0.
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 100, suppressed 0, withdrawn 0
  An EoR was received during read-only mode
  Last ack version 202, Last synced ack version 202
  Outstanding version objects: current 0, max 1, refresh 0
  Additional-paths operation: None
  Advertise routes with local-label via Unicast SAFI

  Connections established 1; dropped 0
  Local host: 10.1.1.1, Local port: 179, IF Handle: 0x04001740
  Foreign host: 10.1.1.100, Foreign port: 32777
  Last reset 00:00:00

BGP neighbor is 100.100.0.2
 Remote AS 100, local AS 100, internal link
 Remote router ID 10.226.255.13
  BGP state = Established, up for 00:30:00
  NSR State: NSR Ready
  Last read 00:00:00, Last read before reset 00:00:00
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
  Last write 00:00:00, attempted 19, written 19
  Second last write 00:01:00, attempted 19, written 19
  Last write before reset 00:00:00, attempted 0, written 0
  Second last write before reset 00:00:00, attempted 0, written 0
  Last write pulse rcvd  Feb 29 00:01:28.910 last full not set pulse count 49
  Last write pulse rcvd before reset 00:00:00
  Socket not armed for io, armed for read, armed for write
  Last write thread event before reset 00:00:00, second last 00:00:00
  Last KA expiry before reset 00:00:00, second last 00:00:00
  Last KA error before reset 00:00:00, KA not sent 00:00:00
  Last KA start before reset 00:00:00, second last 00:00:00
  Precedence: internet
  Non-stop routing is enabled
  Multi-protocol capability received
  Neighbor capabilities:
    Route refresh: advertised (old + new) and received (old + new)
    4-byte AS: advertised and received
    Address family IPv4 Unicast: advertised and received
  Received 34 messages, 0 notifications, 0 in queue
  Sent 34 messages, 0 notifications, 0 in queue
  Minimum time between advertisement runs is 0 secs
  Inbound message logging enabled, 3 messages buffered
  Outbound message logging enabled, 3 messages buffered

 For Address Family: IPv4 Unicast
  BGP neighbor version 202
  Update group: 0.3 Filter-group: 0.2  No Refresh request being processed
  NEXT_HOP is always this router
    Extended Nexthop Encoding: advertised and received
  Route refresh request: received 0, sent 0
  100 accepted prefixes, 100 are bestpaths
  Exact no. of prefixes denied : 0.
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 100, suppressed 0, withdrawn 0
  AIGP is enabled
  An EoR was received during read-only mode
  Last ack version 202, Last synced ack version 202
  Outstanding version objects: current 0, max 1, refresh 0
  Additional-paths operation: None
  Send Multicast Attributes
  Advertise routes with local-label via Unicast SAFI

  Connections established 1; dropped 0
  Local host: 100.100.0.1, Local port: 55522, IF Handle: 0x00000000
  Foreign host: 100.100.0.2, Foreign port: 179
  Last reset 00:00:00"""

# show bgp ipv6 unicast neighbor

show_bgp_ipv6_unicast_neighbors = """\
Thu Feb 29 01:10:50.884 JST

BGP neighbor is 10:1:4::100
 Remote AS 300, local AS 100, external link
 Remote router ID 193.0.0.1
  BGP state = Established, up for 00:03:40
  NSR State: NSR Ready
  Last read 00:00:10, Last read before reset 00:00:00
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
  Last write 00:00:26, attempted 19, written 19
  Second last write 00:00:56, attempted 19, written 19
  Last write before reset 00:00:00, attempted 0, written 0
  Second last write before reset 00:00:00, attempted 0, written 0
  Last write pulse rcvd  Feb 29 01:10:40.771 last full not set pulse count 21
  Last write pulse rcvd before reset 00:00:00
  Socket not armed for io, armed for read, armed for write
  Last write thread event before reset 00:00:00, second last 00:00:00
  Last KA expiry before reset 00:00:00, second last 00:00:00
  Last KA error before reset 00:00:00, KA not sent 00:00:00
  Last KA start before reset 00:00:00, second last 00:00:00
  Precedence: internet
  Non-stop routing is enabled
  Enforcing first AS is enabled
  Multi-protocol capability received
  Neighbor capabilities:
    Route refresh: advertised (old + new) and received (new)
    4-byte AS: advertised
    Address family IPv6 Unicast: advertised and received
  Received 110 messages, 0 notifications, 0 in queue
  Sent 9 messages, 0 notifications, 0 in queue
  Minimum time between advertisement runs is 30 secs
  Inbound message logging enabled, 3 messages buffered
  Outbound message logging enabled, 3 messages buffered

 For Address Family: IPv6 Unicast
  BGP neighbor version 201
  Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
  Route refresh request: received 0, sent 0
  Policy for incoming advertisements is pass
  Policy for outgoing advertisements is pass
  100 accepted prefixes, 100 are bestpaths
  Exact no. of prefixes denied : 0.
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 100, suppressed 0, withdrawn 0
  An EoR was received during read-only mode
  Last ack version 201, Last synced ack version 201
  Outstanding version objects: current 0, max 1, refresh 0
  Additional-paths operation: None
  Advertise routes with local-label via Unicast SAFI

  Connections established 1; dropped 0
  Local host: 10:1:4::1, Local port: 46913, IF Handle: 0x04001780
  Foreign host: 10:1:4::100, Foreign port: 179
  Last reset 00:00:00

BGP neighbor is 100:100::1
 Remote AS 100, local AS 100, internal link
 Remote router ID 10.226.255.12
  BGP state = Established, up for 00:03:56
  NSR State: NSR Ready
  Last read 00:00:56, Last read before reset 00:00:00
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
  Last write 00:00:56, attempted 19, written 19
  Second last write 00:01:56, attempted 19, written 19
  Last write before reset 00:00:00, attempted 0, written 0
  Second last write before reset 00:00:00, attempted 0, written 0
  Last write pulse rcvd  Feb 29 01:09:55.044 last full not set pulse count 10
  Last write pulse rcvd before reset 00:00:00
  Socket not armed for io, armed for read, armed for write
  Last write thread event before reset 00:00:00, second last 00:00:00
  Last KA expiry before reset 00:00:00, second last 00:00:00
  Last KA error before reset 00:00:00, KA not sent 00:00:00
  Last KA start before reset 00:00:00, second last 00:00:00
  Precedence: internet
  Non-stop routing is enabled
  Multi-protocol capability received
  Neighbor capabilities:
    Route refresh: advertised (old + new) and received (old + new)
    4-byte AS: advertised and received
    Address family IPv6 Unicast: advertised and received
  Received 6 messages, 0 notifications, 0 in queue
  Sent 6 messages, 0 notifications, 0 in queue
  Minimum time between advertisement runs is 0 secs
  Inbound message logging enabled, 3 messages buffered
  Outbound message logging enabled, 3 messages buffered

 For Address Family: IPv6 Unicast
  BGP neighbor version 201
  Update group: 0.3 Filter-group: 0.1  No Refresh request being processed
  NEXT_HOP is always this router
  Route refresh request: received 0, sent 0
  100 accepted prefixes, 100 are bestpaths
  Exact no. of prefixes denied : 0.
  Cumulative no. of prefixes denied: 0. 
  Prefix advertised 100, suppressed 0, withdrawn 0
  AIGP is enabled
  An EoR was received during read-only mode
  Last ack version 201, Last synced ack version 201
  Outstanding version objects: current 0, max 1, refresh 0
  Additional-paths operation: None
  Send Multicast Attributes
  Advertise routes with local-label via Unicast SAFI

  Connections established 1; dropped 0
  Local host: 100:100::2, Local port: 179, IF Handle: 0x00000000
  Foreign host: 100:100::1, Foreign port: 41998
  Last reset 00:00:00
"""
# show bgp vrf all ipv4 unicast summary

show_bgp_vrf_all_ipv4_unicast_summary = """\
Sun Feb 25 19:12:09.983 JST

VRF: Test_01
------------
BGP VRF Test_01, state: Active
BGP Route Distinguisher: 651:1
VRF ID: 0x60000004
BGP router identifier 10.10.10.10, local AS number 100
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000013   RD version: 735
BGP main routing table version 736
BGP NSR Initial initsync version 659 (Not Reached)
BGP NSR/ISSU Sync-Group versions 0/0

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker             736        736        736        736         736           0

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
10.1.110.100      0   110     105       6      736    0    0 00:01:04        100
10.2.110.100      0   210     105       6      736    0    0 00:01:01        100


VRF: Test_02
------------
BGP VRF Test_02, state: Active
BGP Route Distinguisher: 652:2
VRF ID: 0x60000005
BGP router identifier 20.20.20.20, local AS number 100
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000014   RD version: 736
BGP main routing table version 736
BGP NSR Initial initsync version 659 (Not Reached)
BGP NSR/ISSU Sync-Group versions 0/0

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker             736        736        736        736         736           0

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
10.1.120.100      0   120     105       6      736    0    0 00:01:03        100
10.2.120.100      0   220     105       6      736    0    0 00:01:04        100
"""

# show route vrf xxx ipv4 unicast bgp

show_route_vrf_ipv4_unicast_bgp = """\
B    110.1.0.0/24 [20/0] via 10.1.110.100, 00:03:46
B    110.1.1.0/24 [20/0] via 10.1.110.100, 00:03:46
B    110.1.2.0/24 [20/0] via 10.1.110.100, 00:03:46
B    110.1.3.0/24 [20/0] via 10.1.110.100, 00:03:46
B    110.1.4.0/24 [20/0] via 10.1.110.100, 00:03:46
B    110.1.5.0/24 [20/0] via 10.1.110.100, 00:03:46
"""

# show bgp vrf all ipv6 unicast summary

show_bgp_vrf_all_ipv6_unicast_summary = """\
Sun Feb 25 19:49:23.548 JST

VRF: Test_01
------------
BGP VRF Test_01, state: Active
BGP Route Distinguisher: 651:1
VRF ID: 0x60000004
BGP router identifier 10.10.10.10, local AS number 100
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0800013   RD version: 703
BGP main routing table version 703
BGP NSR Initial initsync version 603 (Reached)
BGP NSR/ISSU Sync-Group versions 703/0

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker             703        703        703        703         703         703

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
10:1:110::100     0   110     105       7      703    0    0 00:01:22        100
10:2:110::100     0   210     106       7      703    0    0 00:01:36        100


VRF: Test_02
------------
BGP VRF Test_02, state: Active
BGP Route Distinguisher: 652:2
VRF ID: 0x60000005
BGP router identifier 20.20.20.20, local AS number 100
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0800014   RD version: 603
BGP main routing table version 703
BGP NSR Initial initsync version 603 (Reached)
BGP NSR/ISSU Sync-Group versions 703/0

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker             703        703        703        703         703         703

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
10:1:120::100     0   120     105       7      703    0    0 00:01:27        100
10:2:120::100     0   220     106       7      703    0    0 00:01:34        100
"""

# show route vrf xxx ipv6 unicast bgp

show_route_vrf_ipv6_unicast_bgp = """\

Sun Feb 25 19:49:33.798 JST

B    110:1::/64 
      [20/0] via fe80::211:1ff:fe00:1, 00:01:30, TenGigE0/0/0/0.110
B    110:1:1::/64 
      [20/0] via fe80::211:1ff:fe00:1, 00:01:30, TenGigE0/0/0/0.110
B    110:1:2::/64 
      [20/0] via fe80::211:1ff:fe00:1, 00:01:30, TenGigE0/0/0/0.110
B    110:1:3::/64 
      [20/0] via fe80::211:1ff:fe00:1, 00:01:30, TenGigE0/0/0/0.110
B    110:1:4::/64 
      [20/0] via fe80::211:1ff:fe00:1, 00:01:30, TenGigE0/0/0/0.110
B    110:1:5::/64 
      [20/0] via fe80::211:1ff:fe00:1, 00:01:30, TenGigE0/0/0/0.110
"""

# show bgp vrf all ipv6 unicast summary

show_bgp_vrf_all_ipv6_unicast_summary = """\
Sun Feb 25 21:42:25.511 JST

VRF: Test_01
------------
BGP VRF Test_01, state: Active
BGP Route Distinguisher: 651:1
VRF ID: 0x60000008
BGP router identifier 10.10.10.10, local AS number 100
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0800017   RD version: 603
BGP main routing table version 603
BGP NSR Initial initsync version 403 (Reached)
BGP NSR/ISSU Sync-Group versions 603/0

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker             603        603        603        603         603         603

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
10:1:110::100     0   110     106       8      603    0    0 00:01:58        100
10:2:110::100     0   210     106       8      603    0    0 00:01:58        100


VRF: Test_02
------------
BGP VRF Test_02, state: Active
BGP Route Distinguisher: 652:2
VRF ID: 0x60000009
BGP router identifier 20.20.20.20, local AS number 100
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0800018   RD version: 403
BGP main routing table version 603
BGP NSR Initial initsync version 403 (Reached)
BGP NSR/ISSU Sync-Group versions 603/0

BGP is operating in STANDALONE mode.


Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
Speaker             603        603        603        603         603         603

Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
10:1:120::100     0   120     107       8      603    0    0 00:02:03        100
10:2:120::100     0   220     107       8      603    0    0 00:02:09        100
"""

# show route vrf xxx ipv6 unicast bgp

show_route_vrf_ipv6_unicast_bgp = """\
Sun Feb 25 21:45:15.755 JST

B    110:1::/64 
      [20/0] via fe80::211:1ff:fe00:1, 00:04:45, TenGigE0/0/0/0.110
B    110:1:1::/64 
      [20/0] via fe80::211:1ff:fe00:1, 00:04:45, TenGigE0/0/0/0.110
B    110:1:2::/64 
      [20/0] via fe80::211:1ff:fe00:1, 00:04:45, TenGigE0/0/0/0.110
B    110:1:3::/64 
      [20/0] via fe80::211:1ff:fe00:1, 00:04:45, TenGigE0/0/0/0.110
B    110:1:4::/64 
      [20/0] via fe80::211:1ff:fe00:1, 00:04:45, TenGigE0/0/0/0.110
B    110:1:5::/64 
      [20/0] via fe80::211:1ff:fe00:1, 00:04:45, TenGigE0/0/0/0.110"""
# show route ipv4 unicast

show_route_ipv4_unicast = """\
Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
       A - access/subscriber, a - Application route
       M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path

Gateway of last resort is not set

C    10.1.1.0/24 is directly connected, 00:14:16, TenGigE0/0/0/0
L    10.1.1.1/32 is directly connected, 00:14:16, TenGigE0/0/0/0
C    10.1.2.0/24 is directly connected, 00:14:16, Loopback3
L    10.1.2.1/32 is directly connected, 00:14:16, Loopback3
C    10.1.3.0/24 is directly connected, 00:14:16, Loopback4
L    10.1.3.1/32 is directly connected, 00:14:16, Loopback4
L    10.226.255.12/32 is directly connected, 4d19h, Loopback0
S    40.0.0.0/24 [1/0] via 10.1.1.100, 00:14:15
S    50.0.0.0/24 [1/0] via 10.1.1.100, 00:14:15
C    100.100.0.0/24 is directly connected, 00:14:11, TenGigE0/0/0/39
L    100.100.0.1/32 is directly connected, 00:14:11, TenGigE0/0/0/39
L    124.245.240.16/32 is directly connected, 4d19h, Loopback2
O    200.0.0.0/24 [110/1] via 10.1.1.100, 00:14:06, TenGigE0/0/0/0
O    201.0.0.0/24 [110/1] via 10.1.1.100, 00:14:06, TenGigE0/0/0/0
"""

# show bgp ipv4 unicast

show_bgp_ipv4_unicast = """\
Wed Jan 17 12:06:51.111 JST
BGP router identifier 10.226.255.12, local AS number 100
BGP generic scan interval 60 secs
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0000000   RD version: 214
BGP main routing table version 214
BGP NSR Initial initsync version 112 (Reached)
BGP NSR/ISSU Sync-Group versions 214/0
BGP scan interval 60 secs

Status codes: s suppressed, d damped, h history, * valid, > best
              i - internal, r RIB-failure, S stale, N Nexthop-discard
Origin codes: i - IGP, e - EGP, ? - incomplete
   Network            Next Hop            Metric LocPrf Weight Path
*> 10.1.2.0/24        0.0.0.0                  0         32768 ?
*> 10.1.3.0/24        0.0.0.0                  0         32768 ?
*> 40.0.0.0/24        10.1.1.100               0         32768 ?
*> 50.0.0.0/24        10.1.1.100               0         32768 ?
*> 200.0.0.0/24       10.1.1.100               1         32768 ?
*> 201.0.0.0/24       10.1.1.100               1         32768 ?
"""

# show route ipv6 unicast

show_route_ipv6_unicast = """\
C    10:1:2::/64 is directly connected,
      00:03:13, Loopback3
C    10:1:3::/64 is directly connected,
      00:03:13, Loopback4
S    40::/64 
      [1/0] via 10:1:1::100, 00:03:13
S    50::/64 
      [1/0] via 10:1:1::100, 00:03:13
O    200::/64 
      [110/1] via fe80::211:1ff:fe00:1, 00:03:10, TenGigE0/0/0/0
O    200:0:0:1::/64 
      [110/1] via fe80::211:1ff:fe00:1, 00:03:10, TenGigE0/0/0/0
"""

# show bgp ipv6 unicast

show_bgp_ipv6_unicast = """\
Wed Jan 17 12:34:25.299 JST
BGP router identifier 10.226.255.12, local AS number 100
BGP generic scan interval 60 secs
Non-stop routing is enabled
BGP table state: Active
Table ID: 0xe0800000   RD version: 209
BGP main routing table version 209
BGP NSR Initial initsync version 109 (Reached)
BGP NSR/ISSU Sync-Group versions 209/0
BGP scan interval 60 secs

Status codes: s suppressed, d damped, h history, * valid, > best
              i - internal, r RIB-failure, S stale, N Nexthop-discard
Origin codes: i - IGP, e - EGP, ? - incomplete
   Network            Next Hop            Metric LocPrf Weight Path
*> 10:1:1::/64        ::                       0         32768 ?
*> 10:1:2::/64        ::                       0         32768 ?
*> 10:1:3::/64        ::                       0         32768 ?
*> 40::/64            10:1:1::100              0         32768 ?
*> 50::/64            10:1:1::100              0         32768 ?
*> 200::/64           fe80::211:1ff:fe00:1
                                               1         32768 ?
*> 200:0:0:1::/64     fe80::211:1ff:fe00:1
                                               1         32768 ?
"""

# show bgp ipv4 unicast advertised neighbor

show_bgp_ipv4_unicast_advertised_neighbor = """\
Thu Feb 22 15:01:35.293 JST
175.3.0.0/24 is advertised to 100.100.0.2
  Path info:
    neighbor: 10.1.1.100      neighbor router id: 192.0.0.1
    valid  external  best
Received Path ID 0, Local Path ID 1, version 216
  Attributes after inbound policy was applied:
    next hop: 10.1.1.100
    ORG AS LOCAL
    origin: EGP  neighbor as: 200  local pref: 120
    aspath: 200
  Attributes after outbound policy was applied:
    next hop: 100.100.0.1
    ORG AS LOCAL
    origin: EGP  neighbor as: 200  local pref: 120
    aspath: 200

176.3.0.0/24 is advertised to 100.100.0.2
  Path info:
    neighbor: 10.1.1.100      neighbor router id: 192.0.0.1
    valid  external  best
Received Path ID 0, Local Path ID 1, version 217
  Attributes after inbound policy was applied:
    next hop: 10.1.1.3
    ORG AS
    origin: EGP  neighbor as: 200
    aspath: 200
  Attributes after outbound policy was applied:
    next hop: 100.100.0.1
    ORG AS
    origin: EGP  neighbor as: 200
    aspath: 100 200

177.3.0.0/24 is advertised to 100.100.0.2
  Path info:
    neighbor: 10.1.1.100      neighbor router id: 192.0.0.1
    valid  external  best
Received Path ID 0, Local Path ID 1, version 213
  Attributes after inbound policy was applied:
    next hop: 10.1.1.100
    MET ORG AS
    origin: EGP  neighbor as: 200  metric: 120
    aspath: 200
  Attributes after outbound policy was applied:
    next hop: 100.100.0.1
    MET ORG AS
    origin: EGP  neighbor as: 200  metric: 120
    aspath: 200

178.3.0.0/24 is advertised to 100.100.0.2
  Path info:
    neighbor: 10.1.1.100      neighbor router id: 192.0.0.1
    valid  external  best
Received Path ID 0, Local Path ID 1, version 214
  Attributes after inbound policy was applied:
    next hop: 10.1.1.100
    ORG AS COMM
    origin: EGP  neighbor as: 200
    aspath: 200
    community: 4713:10
  Attributes after outbound policy was applied:
    next hop: 100.100.0.1
    ORG AS COMM
    origin: EGP  neighbor as: 200
    aspath: 200
    community: 4713:10

179.3.0.0/24 is advertised to 100.100.0.2
  Path info:
    neighbor: 10.1.1.100      neighbor router id: 192.0.0.1
    valid  external  best
Received Path ID 0, Local Path ID 1, version 215
  Attributes after inbound policy was applied:
    next hop: 10.1.1.100
    ORG AS
    origin: IGP  neighbor as: 200
    aspath: 200
  Attributes after outbound policy was applied:
    next hop: 100.100.0.1
    ORG AS
    origin: IGP  neighbor as: 200
    aspath: 200"""

# show bgp ipv4 unicast

show_bgp_ipv4_unicast_network = """\
Thu Feb 22 14:57:37.624 JST
BGP routing table entry for 175.3.0.0/24
Versions:
  Process           bRIB/RIB  SendTblVer
  Speaker                 103          103
Last Modified: Feb 22 14:55:46.633 for 00:01:51
Paths: (1 available, best #1)
  Advertised IPv4 Unicast paths to peers (in unique update groups):
    100.100.0.2
  Path #1: Received by speaker 0
  Advertised IPv4 Unicast paths to peers (in unique update groups):
    100.100.0.2
  200
    10.1.1.100 from 10.1.1.100 (192.0.0.1)
      Origin EGP, metric 120, localpref 100, valid, external, best, group-best
      Received Path ID 0, Local Path ID 1, version 103
      Community: 4713:10
      Origin-AS validity: (disabled)"""

# show bgp ipv6 unicast

show_bgp_ipv6_unicast_network = """\
Sun Feb 25 16:32:43.126 JST
BGP routing table entry for 175:3::/96
Versions:
  Process           bRIB/RIB  SendTblVer
  Speaker                 211          211
Last Modified: Feb 25 16:31:56.278 for 00:00:47
Paths: (1 available, best #1)
  Advertised IPv6 Unicast paths to peers (in unique update groups):
    10:1:4::100                             
  Path #1: Received by speaker 0
  Advertised IPv6 Unicast paths to peers (in unique update groups):
    10:1:4::100                             
  200
    100:100::1 from 100:100::1 (10.226.255.12)
      Origin EGP, localpref 100, valid, internal, best, group-best
      Received Path ID 0, Local Path ID 1, version 211
"""

# show bgp ipv6 unicast advertised neighbor

show_bgp_ipv6_unicast_advertised_neighbor = """\

175:3::/96 is advertised to 100:100::2
  Path info:
    neighbor: 10:1:1::100     neighbor router id: 192.0.0.1
    valid  external  best  
Received Path ID 0, Local Path ID 1, version 102
  Attributes after inbound policy was applied:
    next hop: 10:1:1::100
    ORG AS 
    origin: EGP  neighbor as: 200  
    aspath: 200
  Attributes after outbound policy was applied:
    next hop: 100:100::1
    ORG AS 
    origin: EGP  neighbor as: 200  
    aspath: 200

176:3::/96 is advertised to 100:100::2
  Path info:
    neighbor: 10:1:1::100     neighbor router id: 192.0.0.1
    valid  external  best  
Received Path ID 0, Local Path ID 1, version 103
  Attributes after inbound policy was applied:
    next hop: 10:1:1::100
    ORG AS 
    origin: EGP  neighbor as: 200  
    aspath: 200
  Attributes after outbound policy was applied:
    next hop: 100:100::1
    ORG AS 
    origin: EGP  neighbor as: 200  
    aspath: 200

177:3::/96 is advertised to 100:100::2
  Path info:
    neighbor: 10:1:1::100     neighbor router id: 192.0.0.1
    valid  external  best  
Received Path ID 0, Local Path ID 1, version 104
  Attributes after inbound policy was applied:
    next hop: 10:1:1::100
    ORG AS 
    origin: EGP  neighbor as: 200  
    aspath: 200
  Attributes after outbound policy was applied:
    next hop: 100:100::1
    ORG AS 
    origin: EGP  neighbor as: 200  
    aspath: 200

178:3::/96 is advertised to 100:100::2
  Path info:
    neighbor: 10:1:1::100     neighbor router id: 192.0.0.1
    valid  external  best  
Received Path ID 0, Local Path ID 1, version 105
  Attributes after inbound policy was applied:
    next hop: 10:1:1::100
    ORG AS 
    origin: EGP  neighbor as: 200  
    aspath: 200
  Attributes after outbound policy was applied:
    next hop: 100:100::1
    ORG AS 
    origin: EGP  neighbor as: 200  
    aspath: 200

179:3::/96 is advertised to 100:100::2
  Path info:
    neighbor: 10:1:1::100     neighbor router id: 192.0.0.1
    valid  external  best  
Received Path ID 0, Local Path ID 1, version 106
  Attributes after inbound policy was applied:
    next hop: 10:1:1::100
    ORG AS 
    origin: EGP  neighbor as: 200  
    aspath: 200
  Attributes after outbound policy was applied:
    next hop: 100:100::1
    ORG AS 
    origin: EGP  neighbor as: 200  
    aspath: 200"""

# show vrf

show_vrf = """\
Mon Feb 19 05:35:47.935 UTC
VRF                  RD                  RT                         AFI   SAFI     
test1                1000:1001          
                                         import  1000:1002           IPV4  Unicast  
                                         export  1000:1001           IPV4  Unicast """

# show route vrf all ipv4

show_route_vrf_all_ipv4 = """\
VRF: MGMT


Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
       A - access/subscriber, a - Application route
       M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path

Gateway of last resort is not set

C    172.17.17.0/24 is directly connected, 19:33:12, MgmtEth0/RSP0/CPU0/0
L    172.17.17.91/32 is directly connected, 19:33:12, MgmtEth0/RSP0/CPU0/0
C    172.31.0.0/24 is directly connected, 19:31:33, MgmtEth0/RSP1/CPU0/0
L    172.31.0.104/32 is directly connected, 19:31:33, MgmtEth0/RSP1/CPU0/0

VRF: test1


Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
       A - access/subscriber, a - Application route
       M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path

Gateway of last resort is not set

C    50.10.100.0/24 is directly connected, 00:02:24, Loopback1001
L    50.10.100.1/32 is directly connected, 00:02:24, Loopback1001
B    50.10.200.0/24 is directly connected, 00:00:21, Loopback1002 (nexthop in vrf test2)

VRF: test2


Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
       A - access/subscriber, a - Application route
       M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path

Gateway of last resort is not set

B    50.10.100.0/24 is directly connected, 00:00:21, Loopback1001 (nexthop in vrf test1)
C    192.0.0.0/8 is directly connected, 1w3d, EINT0/RSP0/CPU0
                 is directly connected, 1w3d, EINT0/RSP1/CPU0"""

# show interfaces brief

show_interfaces_brief = """\
Tue Mar 12 08:18:19.561 JST

               Intf       Intf        LineP              Encap  MTU        BW
               Name       State       State               Type (byte)    (Kbps)
--------------------------------------------------------------------------------
                Lo0          up          up           Loopback  1500          0
    Mg0/RSP0/CPU0/0          up          up               ARPA  1514    1000000
          Te0/0/0/0          up          up               ARPA  1514   10000000
        Te0/0/0/0.1          up          up             802.1Q  1518   10000000
"""

# show lacp

show_lacp = """\
Thu Mar  7 17:59:32.121 JST
State: a - Port is marked as Aggregatable.
       s - Port is Synchronized with peer.
       c - Port is marked as Collecting.
       d - Port is marked as Distributing.
       A - Device is in Active mode.
       F - Device requests PDUs from the peer at fast rate.
       D - Port is using default values for partner information.
       E - Information about partner has expired.

Bundle-Ether1

  Port          (rate)  State    Port ID       Key    System ID
  --------------------  -------- ------------- ------ ------------------------
Local
  Te0/0/0/38       30s  ascdA--- 0x8000,0x0002 0x0001 0x8000,90-88-55-5a-b8-ec
   Partner         30s  ascdA--- 0x8000,0x0002 0x0001 0x8000,34-88-18-cf-40-cd
  Te0/0/0/39       30s  ascdA--- 0x8000,0x0001 0x0001 0x8000,90-88-55-5a-b8-ec
   Partner         30s  ascdA--- 0x8000,0x0001 0x0001 0x8000,34-88-18-cf-40-cd

  Port                  Receive    Period Selection  Mux       A Churn P Churn
  --------------------  ---------- ------ ---------- --------- ------- -------
Local
  Te0/0/0/38            Current    Slow   Selected   Distrib   None    None   
  Te0/0/0/39            Current    Slow   Selected   Distrib   None    None"""

# show lacp counters

show_lacp_counters = """\
Thu Mar  7 18:04:07.313 JST

Bundle-Ether1
                            LACPDUs                      Timeouts
Port            Sent        Received    Excess      Expired     Defaulted
--------------  ----------------------------------  ----------------------
Te0/0/0/38              15          15           0           1           1

Te0/0/0/39              14          15           0           1           1

                            Marker
Port            Received    Resp. Sent  Excess      Pkt Errors  Last Cleared
--------------  ----------------------------------  ----------  ------------
Te0/0/0/38               0           0           0           0  5m2s

Te0/0/0/39               0           0           0           0  5m2s

Port               Last LACP Timeout                  LACP Timeout Transition
--------------  --------------------------------      ----------------------
Te0/0/0/38               0                                 0

Te0/0/0/39               0                                 0"""

# show bfd ipv4

show_bfd_ipv4 = """\
Tue Mar  5 09:47:29.492 JST
show bfd ipv4 session
IPV4 Sessions Up: 1, Down: 0, Unknown/Retry: 0, Total: 1
"""

# show bfd ipv4 session

show_bfd_ipv4_session = """\
Tue Mar  5 09:47:29.973 JST
Interface           Dest Addr           Local det time(int*mult)      State     
                                    Echo             Async   H/W   NPU     
------------------- --------------- ---------------- ---------------- ----------
Te0/0/0/38          100.100.0.2     300ms(100ms*3)   6s(2s*3)         UP        
                                                             No    n/a            """

# shwo bfd ipv6

show_bfd_ipv6 = """\
Tue Mar  5 09:50:55.825 JST
show bfd ipv6 session
IPV6 Sessions Up: 1, Down: 0, Unknown/Retry: 0, Total: 1
"""

# shwo bfd ipv6 session

show_bfd_ipv6_session = """\
Tue Mar  5 09:50:56.308 JST
Interface           Dest Addr      
                                        Local det time(int*mult)      State     
H/W                 NPU             Echo             Async           
------------------- --------------- ---------------- ---------------- ----------
Te0/0/0/38          fe80::4eec:fff:fee7:e3c6                      
No                  n/a             0s(0s*0)         300ms(100ms*3)   UP        """

show_bfd_ipv4_session_detail = """\
Tue Mar 12 20:16:22.003 JST
I/f: TenGigE0/0/0/38, Location: 0/0/CPU0
Dest: 100.100.0.2
Src: 100.100.0.1
 State: UP for 0d:0h:0m:21s, number of times UP: 1
 Session type: PR/V4/SH
Received parameters:
 Version: 1, desired tx interval: 100 ms, required rx interval: 100 ms
 Required echo rx interval: 0 ms, multiplier: 10, diag: None
 My discr: 2148007937, your discr: 2148007981, state UP, D/F/P/C/A: 0/0/0/1/0
Transmitted parameters:
 Version: 1, desired tx interval: 100 ms, required rx interval: 100 ms
 Required echo rx interval: 0 ms, multiplier: 10, diag: None
 My discr: 2148007981, your discr: 2148007937, state UP, D/F/P/C/A: 0/0/0/1/0
Timer Values:
 Local negotiated async tx interval: 100 ms
 Remote negotiated async tx interval: 100 ms
 Desired echo tx interval: 0 s, local negotiated echo tx interval: 0 ms
 Echo detection time: 0 ms(0 ms*10), async detection time: 1 s(100 ms*10)
Local Stats:
 Intervals between async packets:
   Tx: Number of intervals=100, min=83 ms, max=101 ms, avg=91 ms
       Last packet transmitted 59 ms ago
   Rx: Number of intervals=100, min=84 ms, max=101 ms, avg=92 ms
       Last packet received 46 ms ago
 Intervals between echo packets:
   Tx: Number of intervals=0, min=0 s, max=0 s, avg=0 s
       Last packet transmitted 0 s ago
   Rx: Number of intervals=0, min=0 s, max=0 s, avg=0 s
       Last packet received 0 s ago
 Latency of echo packets (time between tx and rx):
   Number of packets: 0, min=0 ms, max=0 ms, avg=0 ms
Session owner information:
                            Desired               Adjusted
  Client               Interval   Multiplier Interval   Multiplier
  -------------------- --------------------- ---------------------
  ospf-1               100 ms     10         100 ms     10  """
