import glob
import os
from os.path import join

import ntc_templates
from fixtures import appdata_path, clear_environ, clear_nagato_appdata

import NAGATO
from NAGATO import NetmikoLibrary


def test_NetmikoLibrary():
    NetmikoLibrary()


def test_set_templates(clear_environ, clear_nagato_appdata):
    assert not os.path.exists(appdata_path)

    NetmikoLibrary()

    file_num_ntc = len(glob.glob("*.textfsm", root_dir=join(ntc_templates.__path__[0], "templates")))
    file_num_nagato = len(glob.glob("*.textfsm", root_dir=join(NAGATO.__path__[0], "templates")))
    file_num_app = len(glob.glob("*.textfsm", root_dir=join(appdata_path, "templates")))

    assert os.path.exists(appdata_path)
    assert file_num_app == (file_num_ntc + file_num_nagato)
