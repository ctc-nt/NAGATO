import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_bfd_ipv4_session_detail
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_bfd_ipv4_session_detail.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_bfd_ipv4_session_detail():
    """Parse可能なこと"""

    output = re_table.ParseText(show_bfd_ipv4_session_detail)
    print(f"\n{output=}")
    assert output == [["ospf-1", "100", "10", "100", "10"]]
