from ._wrapper import NetmikoWrapper
from robot.api.deco import library

__all__ = ["NetmikoLibrary"]


@library(scope="SUITE", version="1.0.0")
class NetmikoLibrary(NetmikoWrapper):
    """NetmikoLibrary is a Robot Framework library that provides SSH/Telnet connections to network devices and enables operations on the CLI.

    This library uses the netmiko package.
    """

    pass
