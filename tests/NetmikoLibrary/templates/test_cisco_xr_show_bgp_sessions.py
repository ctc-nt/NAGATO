import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_bgp_sessions
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_bgp_sessions.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_bgp_sessions)
    print(f"\n{output=}")
    assert output == [['10.1.1.100', 'default', '0', '200', '0', '0', 'Established', 'None'], ['100.100.0.2', 'default', '0', '100', '0', '0', 'Established', 'None'], ['10:1:1::100', 'default', '0', '200', '0', '0', 'Idle', 'None'], ['100:100::2', 'default', '0', '100', '0', '0', 'Idle', 'None']]
