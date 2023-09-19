from .SNMP import SNMP
from robot.api.deco import library

__all__ = ["NetworkUtils"]

@library(scope="SUITE", version="1.0.0")
class NetworkUtils(SNMP):
    """NetworkUtils is a Robot Framework library that enables various processes 
    
    from the terminal required for network test.
    """

    pass