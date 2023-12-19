import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_ospfv3_neighbor
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_ospfv3_neighbor.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_ospfv3_neighbor)
    print(f"\n{output=}")

    assert output == [["2.2.2.2", "1", "FULL/BDR", "192.168.1.2", "GigabitEthernet0/0/0/5", "1"], ["192.168.16.10", "5", "FULL/DR", "192.168.48.189", "GigabitEthernet 0/3/0/3", "1"]]
