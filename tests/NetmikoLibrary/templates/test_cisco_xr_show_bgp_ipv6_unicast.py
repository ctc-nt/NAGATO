import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_bgp_ipv6_unicast
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_bgp_ipv6_unicast.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_bgp_ipv6_unicast)
    print(f"\n{output=}")
    print(len(output))

    assert output == [["*>", "10:1:1::/64", "::"], ["*>", "10:1:2::/64", "::"], ["*>", "10:1:3::/64", "::"], ["*>", "40::/64", "10:1:1::100"], ["*>", "50::/64", "10:1:1::100"], ["*>", "200::/64", "fe80::211:1ff:fe00:1"], ["*>", "200:0:0:1::/64", "fe80::211:1ff:fe00:1"]]
