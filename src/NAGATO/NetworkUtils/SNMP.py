from pysnmp.error import PySnmpError
from pysnmp.hlapi import (
    CommunityData,
    ContextData,
    ObjectIdentity,
    ObjectType,
    SnmpEngine,
    UdpTransportTarget,
    getCmd,
    nextCmd,
)
from robot.api import logger
from robot.api.deco import keyword


class SNMP:
    """NetworkUtils.SNMPはSNMPに関する操作を提供するRobot Frameworkライブラリです。"""

    @keyword
    def snmpwalk(self, host: str, oid: str, port: int = 161, community: str = "public") -> dict:
        """``host`` に対し、指定した ``oid`` に対するGetNext Requestを実行します。
        その後、取得した全てのOIDとその値を返します。

        Example:
        | ${oid_list} = | `Snmpwalk` | host=10.0.0.1 | oid=1.3.6.1.2.1.1.1 |
        | `Builtin.Log` | ${oid_list} | formatter=repr |
        """

        # 現在の実装: v1/v2cで動作、IPv4のみ対応
        # TODO: v1/v2c, v3で使い分ける
        # TODO: IPv4, IPv6に対応

        object_dict = {}

        for errorIndication, errorStatus, errorIndex, varBinds in nextCmd(
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
        """``host`` に対し、指定した ``oid`` に対するSNMP GetRequestを実行し、そのOIDの値を返します。

        Example:
        | ${result} = | `Get Request` | host=192.168.1.1 | oid=1.3.6.1.2.1.1.1.0 |
        | Should Contain | ${result} | IOS-XE |
        """

        # 現在の実装: v1/v2cで動作、IPv4のみ対応
        # TODO: v1/v2c, v3で使い分ける
        # TODO: IPv4, IPv6に対応

        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(
                SnmpEngine(),
                CommunityData(community),
                UdpTransportTarget((host, port)),
                ContextData(),
                ObjectType(ObjectIdentity(oid)),
            )
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
