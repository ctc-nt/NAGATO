import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_ipv6_interface
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates/cisco_xr_show_ipv6_interface.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_juniper_junos_show_chassis_environment():
    """Parse可能なこと"""

    output = re_table.ParseText(show_ipv6_interface)
    print(f"\n{output=}")

    assert output == [
        ["TenGigE0/0/0/1", "enabled", "fe80::4eec:fff:fe16:aa61", "::ffff:192.168.100.2", "::ffff:192.168.100.2/128"]
    ]
