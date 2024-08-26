import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_protocols_ipv6_ospf
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_protocols_ipv6_ospfv3.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_protocols_ipv6_ospf)
    print(f"\n{output=}")

    assert output == [
        ["1", "10.0.0.1", "110", "Enabled", "0", ["HundredGigE 0/2/0/2", "Loopback1"]],
        ["1", "10.0.0.1", "110", "Enabled", "1", ["Loopback2"]],
        ["2", "1.1.1.1", "110", "Disabled", "0", ["Loopback3"]],
    ]
