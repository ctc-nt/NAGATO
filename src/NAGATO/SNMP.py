"""
Copyright 2024 ITOCHU Techno-Solutions Corporation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

import asyncio

from pysnmp.error import PySnmpError
from pysnmp.hlapi.asyncio import (
    CommunityData,
    ContextData,
    Slim,
    SnmpEngine,
    UdpTransportTarget,
    walkCmd,
)
from pysnmp.smi.rfc1902 import ObjectIdentity, ObjectType
from robot.api import logger
from robot.api.deco import keyword, library

from NAGATO.version import get_version


@library
class SNMP:
    """A library providing keywords for operations relevant to SNMP."""

    ROBOT_LIBRARY_SCOPE = "SUITE"
    ROBOT_LIBRARY_VERSION = get_version()

    @keyword
    def snmpwalk(self, host: str, oid: str, port: int = 161, community: str = "public") -> dict:
        """Execute GetNext Request to ``host`` and return all values as a dictionary.
        This keyword supports only IPv4 and SNMP version 1 or 2c.

        Example:
        | ${objects} = | `Snmpwalk` | host=192.168.2.1 | oid=1.3.6.1.2.1.1.1 |
        | `Builtin.Log` | ${objects} | formatter=repr |
        """

        async def walk() -> dict:
            result = {}

            iterator = walkCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((host, port)), ContextData(), ObjectType(ObjectIdentity(oid)))

            async for errorIndication, errorStatus, errorIndex, varBinds in iterator:
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
                        _oid, _value = varBind
                        try:
                            result[str(_oid)] = str(_value)
                        except Exception as e:
                            print(f"Error getting label for OID {_oid}: {e}")

            return result

        return asyncio.run(walk())

    @keyword
    def get_request(self, host: str, oid: str, port: int = 161, community: str = "public", version: int = 2) -> str:
        """Execute Get Request to ``host`` and return the value of ``oid`` .
        This keyword supports only IPv4 and SNMP version 1 or 2c.

        Example:
        | ${object} = | `Get Request` | host=192.168.2.1 | oid=1.3.6.1.2.1.1.1.0 |
        | Should Contain | ${object} | IOS-XE |
        """

        async def get():
            with Slim(version) as slim:
                errorIndication, errorStatus, errorIndex, varBinds = await slim.get(community, host, port, ObjectType(ObjectIdentity(oid)))
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
                    for varBind in varBinds:
                        logger.info(" = ".join([x.prettyPrint() for x in varBind]))
                        if "no such" in str(varBind[1].prettyPrint().lower()):
                            logger.warn(varBind[1].prettyPrint())

                        return varBind[1].prettyPrint()

        return asyncio.run(get())
