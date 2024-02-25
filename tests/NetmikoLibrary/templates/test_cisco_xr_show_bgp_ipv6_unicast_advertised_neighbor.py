import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_bgp_ipv6_unicast_advertised_neighbor
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_bgp_ipv6_unicast_advertised_neighbor.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_bgp_ipv6_unicast_advertised_neighbor():
    """Parse可能なこと"""

    output = re_table.ParseText(show_bgp_ipv6_unicast_advertised_neighbor)

    print(f"\n{output=}")
    assert output == [['175:3::/96', '100:100::2', '10:1:1::100', '10:1:1::100', 'EGP', '200', '', '200', '', '', '100:100::1', 'EGP', '200', '', '200', '', ''], ['176:3::/96', '100:100::2', '10:1:1::100', '10:1:1::100', 'EGP', '200', '', '200', '', '', '100:100::1', 'EGP', '200', '', '200', '', ''], ['177:3::/96', '100:100::2', '10:1:1::100', '10:1:1::100', 'EGP', '200', '', '200', '', '', '100:100::1', 'EGP', '200', '', '200', '', ''], ['178:3::/96', '100:100::2', '10:1:1::100', '10:1:1::100', 'EGP', '200', '', '200', '', '', '100:100::1', 'EGP', '200', '', '200', '', ''], ['179:3::/96', '100:100::2', '10:1:1::100', '10:1:1::100', 'EGP', '200', '', '200', '', '', '100:100::1', 'EGP', '200', '', '200', '', '']]
