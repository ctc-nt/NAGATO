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
      Link is Active
"""
