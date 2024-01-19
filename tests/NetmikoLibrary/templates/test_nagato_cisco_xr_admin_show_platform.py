import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import admin_show_platform
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "nagato_cisco_xr_admin_show_platform.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(admin_show_platform)
    print(f"\n{output=}")
    expect_output = [
        ["0/0", "A9K-4HG-FLEX-SE", "OPERATIONAL", "OPERATIONAL", "NSHUT"],
        ["0/1", "A9K-4HG-FLEX-SE", "OPERATIONAL", "OPERATIONAL", "NSHUT"],
        ["0/RSP0", "A9K-RSP5-SE", "OPERATIONAL", "OPERATIONAL", "NSHUT"],
        ["0/RSP1", "A9K-RSP5-SE", "OPERATIONAL", "OPERATIONAL", "NSHUT"],
        ["0/FT0", "ASR-9906-FAN", "OPERATIONAL", "N/A", "NSHUT"],
        ["0/FT1", "ASR-9906-FAN", "OPERATIONAL", "N/A", "NSHUT"],
        ["0/PT0", "A9K-AC-PEM-V3", "OPERATIONAL", "N/A", "NSHUT"],
    ]
    assert output == expect_output
