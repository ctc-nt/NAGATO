from ._wrapper import NetmikoWrapper
from robot.api.deco import library
import os
import NAGATO

__all__ = ["NetmikoLibrary"]

nagato_templates_path = os.path.join(NAGATO.__path__[0], "templates")
os.environ["NET_TEXTFSM"] = nagato_templates_path

@library(scope="SUITE", version="1.0.0")
class NetmikoLibrary(NetmikoWrapper):
    """NetmikoLibraryはネットワーク機器へSSH/Telnet接続を行い、CLI上の操作を可能にするRobot Frameworkライブラリです。

    このライブラリはnetmikoパッケージを利用しています。
    """

    pass
