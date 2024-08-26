import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_bgp_ipv4_unicast_advertised_neighbor
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(
    os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_bgp_ipv4_unicast_advertised_neighbor.textfsm"
)

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_bgp_ipv4_unicast_advertised_neighbor():
    """Parse可能なこと"""

    output = re_table.ParseText(show_bgp_ipv4_unicast_advertised_neighbor)

    print(f"\n{output=}")
    assert output == [
        [
            "175.3.0.0/24",
            "100.100.0.2",
            "10.1.1.100",
            "10.1.1.100",
            "EGP",
            "200",
            "120",
            "200",
            "",
            "",
            "100.100.0.1",
            "EGP",
            "200",
            "120",
            "200",
            "",
            "",
        ],
        [
            "176.3.0.0/24",
            "100.100.0.2",
            "10.1.1.100",
            "10.1.1.3",
            "EGP",
            "200",
            "",
            "200",
            "",
            "",
            "100.100.0.1",
            "EGP",
            "200",
            "",
            "100 200",
            "",
            "",
        ],
        [
            "177.3.0.0/24",
            "100.100.0.2",
            "10.1.1.100",
            "10.1.1.100",
            "EGP",
            "200",
            "",
            "200",
            "120",
            "",
            "100.100.0.1",
            "EGP",
            "200",
            "",
            "200",
            "120",
            "",
        ],
        [
            "178.3.0.0/24",
            "100.100.0.2",
            "10.1.1.100",
            "10.1.1.100",
            "EGP",
            "200",
            "",
            "200",
            "",
            "4713:10",
            "100.100.0.1",
            "EGP",
            "200",
            "",
            "200",
            "",
            "4713:10",
        ],
        [
            "179.3.0.0/24",
            "100.100.0.2",
            "10.1.1.100",
            "10.1.1.100",
            "IGP",
            "200",
            "",
            "200",
            "",
            "",
            "100.100.0.1",
            "IGP",
            "200",
            "",
            "200",
            "",
            "",
        ],
    ]
