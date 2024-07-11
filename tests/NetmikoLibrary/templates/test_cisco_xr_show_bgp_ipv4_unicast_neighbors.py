import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_bgp_ipv4_unicast_neighbors
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_bgp_ipv4_unicast_neighbors.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_bgp_ipv4_unicast_neighbors)
    print(f"\n{output=}")

    assert output == [["10.1.1.100", "200", "100", "192.0.0.1", "Established", "NSR Ready", "30"], ["100.100.0.2", "100", "100", "10.226.255.13", "Established", "NSR Ready", "0"]]
