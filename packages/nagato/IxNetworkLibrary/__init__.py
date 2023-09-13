from ._wrapper import IxnNetworkRestpyWrapper
from robot.api.deco import library

__all__ = ["IxNetworkLibrary"]


@library(scope="SUITE", version="1.0.0")
class IxNetworkLibrary(IxnNetworkRestpyWrapper):
    """IxNetworkLibrary is a Robot Framework library that provides operations on IxNetwork.

    This library uses the ixnetwork-restpy package.

    This library supports versions 8.52 and up of the following servers:
    - Linux IxNetwork API Server
    - Windows IxNetwork GUI
    - Windows IxNetwork Connection Manager
    """
    pass
