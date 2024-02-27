import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_route_ipv6_unicast
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_route_ipv6_unicast.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_route_ipv6_unicast)
    print(f"\n{output=}")

    assert output == [
        ["C", "10:1:2::", "64", "", "", "", "00:03:13", "Loopback3"],
        ["C", "10:1:3::", "64", "", "", "", "00:03:13", "Loopback4"],
        ["S", "40::", "64", "1", "0", "10:1:1::100", "00:03:13", ""],
        ["S", "50::", "64", "1", "0", "10:1:1::100", "00:03:13", ""],
        ["O", "200::", "64", "110", "1", "fe80::211:1ff:fe00:1", "00:03:10", "TenGigE0/0/0/0"],
        ["O", "200:0:0:1::", "64", "110", "1", "fe80::211:1ff:fe00:1", "00:03:10", "TenGigE0/0/0/0"],
    ]
