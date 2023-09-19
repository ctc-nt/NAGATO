from .IxNetworkLibrary import IxNetworkLibrary
from .NetmikoLibrary import NetmikoLibrary
from .NetworkUtils import NetworkUtils
from robot.api.deco import library
import ntc_templates
import os
import shutil

@library(scope="SUITE", version="1.0.0")
class NAGATO(IxNetworkLibrary, NetmikoLibrary, NetworkUtils):
    pass