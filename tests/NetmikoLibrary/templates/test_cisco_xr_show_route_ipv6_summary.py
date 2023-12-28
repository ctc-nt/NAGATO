import os

import pytest

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_route_ipv6_summary
from textfsm import TextFSM

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_route_ipv6_summary.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_route_ipv6_summary)
    print(f"\n{output=}")

    assert output == [["local-iid sidmgr", "0"],
                      ["connected", "1"],
                      ["connected l2tpv3_xconnect", "0"],
                      ["local", "1"],
                      ["local-srv6 xtc_srv6", "0"],
                      ["static", "0"],
                      ["vxlan", "0"],
                      ["ospf 1", "0"],
                      ["ospf 2", "0"],
                      ["Total", "2"]]
