import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_access_lists
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_access-lists.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_access_lists)
    print(f"\n{output=}")

    assert output == [["Test-ACL_1", "10 deny ipv4 host 172.17.17.20 any"], ["Test-ACL_1", "20 permit ipv4 172.17.17.0 0.0.0.255 any"], ["Test-ACL_2", "10 permit tcp any 172.16.0.0 0.0.255.255 eq telnet"], ["Test-ACL_2", "20 deny tcp any any"]]
