import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_interfaces_brief
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates/cisco_xr_show_interfaces_brief.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_juniper_junos_show_chassis_environment():
    """Parse可能なこと"""

    output = re_table.ParseText(show_interfaces_brief)
    print(f"\n{output=}")

    assert output == [
        ["Lo0", "up", "up", "Loopback", "1500", "0"],
        ["Mg0/RSP0/CPU0/0", "up", "up", "ARPA", "1514", "1000000"],
        ["Te0/0/0/0", "up", "up", "ARPA", "1514", "10000000"],
        ["Te0/0/0/0.1", "up", "up", "802.1Q", "1518", "10000000"],
    ]
