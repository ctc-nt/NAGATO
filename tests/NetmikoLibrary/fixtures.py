import os
import pytest
import shutil
from os.path import join

if os.name == "posix":
    appdata_path = join(os.environ["HOME"], ".NAGATO")
elif os.name == "nt":
    appdata_path = join(os.environ["LOCALAPPDATA"], "NAGATO")

@pytest.fixture
def clear_environ():
    """clear environment variables relevant to NetmikoLibrary"""
    os.environ.pop("NET_TEXTFSM")

@pytest.fixture
def clear_nagato_appdata():
    shutil.rmtree(appdata_path)

