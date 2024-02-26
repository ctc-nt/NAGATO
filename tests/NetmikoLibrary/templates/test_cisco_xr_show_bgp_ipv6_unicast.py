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
def test_show_bgp_ipv6_unicast():
    """Parse可能なこと"""

    output = re_table.ParseText(show_bgp_ipv6_unicast)

    print(f"\n{output=}") 
    assert output == [['175:3::/96', '10:1:4::100', '200', 'EGP', '', '100', '']]
