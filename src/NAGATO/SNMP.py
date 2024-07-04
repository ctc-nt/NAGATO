from pysnmp.error import PySnmpError
from pysnmp.hlapi import (
    CommunityData,
    ContextData,
    ObjectIdentity,
    ObjectType,
    SnmpEngine,
    UdpTransportTarget,
    getCmd,
    walkCmd
)
from robot.api import logger
from robot.api.deco import keyword, library


@library(scope="SUITE", version="1.0.0")
class SNMP:
    """A library providing keywords for operations relevant to SNMP."""

    @keyword
    def snmpwalk(self, host: str, oid: str, port: int = 161, community: str = "public") -> dict:
        """Execute GetNext Request to ``host`` and return all values as a dictionary.
        This keyword supports only IPv4 and SNMP version 1 or 2c.

        Example:
        | ${objects} = | `Snmpwalk` | host=192.168.2.1 | oid=1.3.6.1.2.1.1.1 |
        | `Builtin.Log` | ${objects} | formatter=repr |
        """

        object_dict = {}

        for errorIndication, errorStatus, errorIndex, varBinds in walkCmd(
            SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((host, port)),
            ContextData(),
            ObjectType(ObjectIdentity(oid)),
            lexicographicMode=False,
        ):
            if errorIndication:
                logger.error(errorIndication)
                break
            elif errorStatus:
                logger.error(
                    "%s at %s"
                    % (
                        errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
                    )
                )
                break
            else:
                for varBind in varBinds:
                    logger.info(" = ".join([x.prettyPrint() for x in varBind]))
                    object_dict[str(varBind[0])] = varBind[1].prettyPrint()

        return object_dict

    @keyword
    def get_request(self, host: str, oid: str, port: int = 161, community: str = "public") -> str:
        """Execute Get Request to ``host`` and return the value of ``oid`` .
        This keyword supports only IPv4 and SNMP version 1 or 2c.

        Example:
        | ${object} = | `Get Request` | host=192.168.2.1 | oid=1.3.6.1.2.1.1.1.0 |
        | Should Contain | ${object} | IOS-XE |
        """

        errorIndication, errorStatus, errorIndex, varBinds = getCmd(
            SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((host, port)),
            ContextData(),
            ObjectType(ObjectIdentity(oid)),
        )

        if errorIndication:
            logger.error(errorIndication)
            raise PySnmpError(f"GetRequest failed. host:{repr(host)}, community:{repr(community)}, oid:{repr(oid)}")
        elif errorStatus:
            logger.error(
                "%s at %s"
                % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
                )
            )
            raise PySnmpError(f"GetRequest failed. host:{repr(host)}, community:{repr(community)}, oid:{repr(oid)}")
        else:
            varBind = varBinds[0]
            logger.info(f"{varBind[0]} = {varBind[1]}")

        return str(varBind[1])
