import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_chassis_environment
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates/juniper_junos_show_chassis_environment.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_juniper_junos_show_chassis_environment():
    """Parse可能なこと"""

    output = re_table.ParseText(show_chassis_environment)
    print(f"\n{output=}")

    assert output == [
        ["PEM 0", "OK"],
        ["PEM 1", "OK"],
        ["PEM 2", "Check"],
        ["PEM 3", "Check"],
        ["Routing Engine 0", "OK"],
    ]
