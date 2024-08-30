import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_lacp_io
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_lacp_io.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_lacp_io)
    print(f"\n{output=}")
    assert output == [
        ["1", ["TenGigE0/0/0/38", "TenGigE0/0/0/39"], ["30000", "30000"]],
        ["2", ["HundredGigE0/1/0/42"], ["1000"]],
    ]
