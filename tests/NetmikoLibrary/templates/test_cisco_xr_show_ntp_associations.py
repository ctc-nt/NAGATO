import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_ntp_associations
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates/cisco_xr_show_ntp_associations.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_juniper_junos_show_chassis_environment():
    """Parse可能なこと"""

    output = re_table.ParseText(show_ntp_associations)
    print(f"\n{output=}")

    assert output == [[["~172.17.17.90 vrf MGMT", "*~172.17.17.248 vrf MGMT", "~172.17.17.254 vrf MGMT"]]]
