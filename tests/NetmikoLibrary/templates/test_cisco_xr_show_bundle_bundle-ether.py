import os
import pytest
from textfsm import TextFSM

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_bundle_bundle_ether

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "Templates", "cisco_xr_show_bundle_bundle-ether.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_bundle_bundle_ether)
    print(f"\n{output=}")

    assert output == [[{'interface': 'Bundle-Ether10', 'status': 'Up', 'links': '1', 'port': ['Te0/0/0/38', 'Hu0/1/0/42'], 'device': 'Local', 'state': 'Active', 'port_id': '0x8000, 0x0000', 'b_w': '100000000'}]]