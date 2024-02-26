import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_route_ipv4_unicast
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_route_ipv4_unicast.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_route_ipv4_unicast)
    print(f"\n{output=}")

    assert output == [['C', '10.1.1.0', '24', '', '', '', '00:14:16', 'TenGigE0/0/0/0'], ['L', '10.1.1.1', '32', '', '', '', '00:14:16', 'TenGigE0/0/0/0'], ['C', '10.1.2.0', '24', '', '', '', '00:14:16', 'Loopback3'], ['L', '10.1.2.1', '32', '', '', '', '00:14:16', 'Loopback3'], ['C', '10.1.3.0', '24', '', '', '', '00:14:16', 'Loopback4'], ['L', '10.1.3.1', '32', '', '', '', '00:14:16', 'Loopback4'], ['L', '10.226.255.12', '32', '', '', '', '4d19h', 'Loopback0'], ['S', '40.0.0.0', '24', '1', '0', '10.1.1.100', '00:14:15', ''], ['S', '50.0.0.0', '24', '1', '0', '10.1.1.100', '00:14:15', ''], ['C', '100.100.0.0', '24', '', '', '', '00:14:11', 'TenGigE0/0/0/39'], ['L', '100.100.0.1', '32', '', '', '', '00:14:11', 'TenGigE0/0/0/39'], ['L', '124.245.240.16', '32', '', '', '', '4d19h', 'Loopback2'], ['O', '200.0.0.0', '24', '110', '1', '10.1.1.100', '00:14:06', 'TenGigE0/0/0/0'], ['O', '201.0.0.0', '24', '110', '1', '10.1.1.100', '00:14:06', 'TenGigE0/0/0/0']]
