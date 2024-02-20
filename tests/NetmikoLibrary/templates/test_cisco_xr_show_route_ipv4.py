import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_route_ipv4
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_route_ipv4.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_route_ipv4)
    print(f"\n{output=}")

    assert output == [
        ["S*", "0.0.0.0", "0", "1", "0", "1.0.0.1", "13:14:59", ""],
        ["O E2", "5.2.5.0", "24", "110", "20", "3.3.3.1", "00:04:20", "GigabitEthernet0/3/0/0"],
        ["O E2", "6.2.6.0", "24", "110", "20", "3.3.3.1", "00:04:20", "GigabitEthernet0/3/0/0"],
        ["O E2", "8.2.8.0", "24", "110", "20", "3.3.3.1", "00:04:20", "GigabitEthernet0/3/0/0"],
    ]
