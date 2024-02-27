import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_route_vrf_all_ipv4
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_route_vrf_all_ipv4.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_route_vrf_all_ipv4)
    print(f"\n{output=}")

    assert output == [
        ["MGMT", "C", "172.17.17.0/24", "MgmtEth0/RSP0/CPU0/0", ""],
        ["MGMT", "L", "172.17.17.91/32", "MgmtEth0/RSP0/CPU0/0", ""],
        ["MGMT", "C", "172.31.0.0/24", "MgmtEth0/RSP1/CPU0/0", ""],
        ["MGMT", "L", "172.31.0.104/32", "MgmtEth0/RSP1/CPU0/0", ""],
        ["test1", "C", "50.10.100.0/24", "Loopback1001", ""],
        ["test1", "L", "50.10.100.1/32", "Loopback1001", ""],
        ["test1", "B", "50.10.200.0/24", "Loopback1002", "test2"],
        ["test2", "B", "50.10.100.0/24", "Loopback1001", "test1"],
        ["test2", "C", "192.0.0.0/8", "EINT0/RSP0/CPU0", ""],
        ["test2", "C", "192.0.0.0/8", "EINT0/RSP1/CPU0", ""],
    ]
