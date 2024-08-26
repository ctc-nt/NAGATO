import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_bgp_vrf_all_ipv6_unicast_summary
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(
    os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_bgp_vrf_all_ipv6_unicast_summary.textfsm"
)

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_bgp_vrf_all_ipv6_unicast_summary)
    print(f"\n{output=}")
    assert output == [
        ["Test_01", "Active", "10:1:110::100", "0", "110", "106", "8", "603", "0", "0", "100"],
        ["Test_01", "Active", "10:2:110::100", "0", "210", "106", "8", "603", "0", "0", "100"],
        ["Test_02", "Active", "10:1:120::100", "0", "120", "107", "8", "603", "0", "0", "100"],
        ["Test_02", "Active", "10:2:120::100", "0", "220", "107", "8", "603", "0", "0", "100"],
    ]
