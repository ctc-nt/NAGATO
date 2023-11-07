import os
import pytest
from textfsm import TextFSM

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_chassis_routing_engine

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates/juniper_junos_show_chassis_routing-engine.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_juniper_junos_show_chassis_routing_engine():
    """Parse可能なこと"""

    output = re_table.ParseText(show_chassis_routing_engine)
    print(f"\n{output=}")

    assert output == [['Slot 0', 'Master'], ['Slot 1', 'Backup'], ['Slot 10', 'Disable']]