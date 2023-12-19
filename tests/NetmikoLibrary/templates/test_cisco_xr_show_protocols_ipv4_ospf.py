import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_protocols_ipv4_ospf
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_protocols_ipv4_ospf.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_protocols_ipv4_ospf)
    print(f"\n{output=}")

    assert output == [["OSPF 1", "55.55.55.55", "110", "Enabled", "Area 0", "MPLS/TE enabled"], ["OSPF 1", "55.55.55.55", "110", "Enabled", "Area 0", "GigabitEthernet 0/3/0/3"], ["OSPF 1", "55.55.55.55", "110", "Enabled", "Area 0", "Loopback0"]]
