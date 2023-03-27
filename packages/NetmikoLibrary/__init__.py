from ._wrapper import NetmikoWrapper
from robot.api.deco import library

__all__ = ["NetmikoLibrary"]


@library(scope="SUITE", version="1.0.0")
class NetmikoLibrary(NetmikoWrapper):
    """NetmikoLibraryはネットワーク機器へSSH/Telnet接続を行い、CLI上の操作を可能にするRobot Frameworkライブラリです。

    このライブラリはnetmikoパッケージを利用しています。
    """

    pass
