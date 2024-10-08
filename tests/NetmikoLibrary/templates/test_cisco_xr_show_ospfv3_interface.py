import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_ospfv3_interface
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_ospfv3_interface.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_ospfv3_interface)
    print(f"\n{output=}")

    assert output == [
        ["TenGigE0/0/0/38", "fe80::4eec:fff:fee7:e3c6", "42", "0", "1", "0", "2.2.2.2", "10", "10000000", "10"],
        ["TenGigE0/0/0/39", "fe80::4eec:fff:fee7:e3c6", "42", "0", "1", "0", "1.1.1.1", "10", "10000000", "110"],
    ]
