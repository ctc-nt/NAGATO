import os
import pytest
from textfsm import TextFSM

# cli_outputs.pyからテストデータを取得
# 将来, AMIOSのバージョンアップに伴ってCLIの出力が変わった場合に, 変更するファイルが1つだけで済むようにする
from _cli_outputs import show_ethernet_oam_event_log

# テスト対象テンプレートファイル
template_path = os.path.join(os.getcwd(), "src/NAGATO/templates", "cisco_xr_show_ethernet_oam_event-log.textfsm")

# テンプレートファイルを読み込む
with open(template_path, mode="r") as f:
    re_table = TextFSM(f)


@pytest.mark.textfsm
def test_show_ip():
    """Parse可能なこと"""

    output = re_table.ParseText(show_ethernet_oam_event_log)
    print(f"\n{output=}")

    assert output == [['TenGigE0/0/0/38','Mon Dec 04 11:26:38 JST', 'Dying gasp'],['TenGigE0/0/0/38', 'Mon Dec 04 11:26:38 JST', 'Frame fail'],['TenGigE0/0/0/39', 'Mon Dec 04 11:26:38 JST', 'Frame']]