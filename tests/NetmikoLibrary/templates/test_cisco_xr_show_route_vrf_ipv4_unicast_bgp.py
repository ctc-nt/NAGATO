import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_route_vrf_ipv4_unicast_bgp
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_route_vrf_ipv4_unicast_bgp.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_route_vrf_ipv4_unicast_bgp)
    print(f"\n{output=}")
    assert output == [
        ["B", "110.1.0.0/24", "10.1.110.100"],
        ["B", "110.1.1.0/24", "10.1.110.100"],
        ["B", "110.1.2.0/24", "10.1.110.100"],
        ["B", "110.1.3.0/24", "10.1.110.100"],
        ["B", "110.1.4.0/24", "10.1.110.100"],
        ["B", "110.1.5.0/24", "10.1.110.100"],
    ]
