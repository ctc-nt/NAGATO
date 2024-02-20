from pyshark import FileCapture
from pyshark.packet.packet import Packet
from robot.api import logger
from robot.api.deco import keyword, library


@library(scope="SUITE", version="1.0.0")
class PcapFileReader:
    """PcapFileReaderはpcap形式のファイルを読み込み、データを取得するRobot Frameworkライブラリです。

    このライブラリはpysharkパッケージを利用しています。

    初めに`Read Pcap File`を使用し、pcap形式のファイルを読み込んでください。
    """

    def __init__(self):
        pass

    @keyword
    def read_pcap_file(self, filepath: str, **kwargs) -> FileCapture:
        """``filepath`` に指定した場所のpcapファイルを読み込みます。

        Example:
        | ${capture} = | `Read Pcap File` | /path/to/pcap/file.pcap |
        """

        return FileCapture(filepath, **kwargs)

    @keyword
    def get_packet_data(self, capture: FileCapture, number: int, *args: str) -> str:
        """読み込んだpcapファイルから ``number`` に指定した場所のパケットの情報を抜き出し、その中からデータを取得します。

        可変長引数には取得するデータを階層ごとに分けて指定します。データの指定はpysharkの指定方法に準拠しています。
        例えばpysharkで ``${var}.ip.src`` と表現される場合、可変長引数には ``ip`` , ``src`` の順に値を与えます。

        Example:
        | ${capture} = | `Read Pcap File` | /path/to/pcap/file.pcap |
        | ${ipaddr_src} = | `Get Packet Data` | ${capture} | ${1} | ip | src |
        | Should Be Equal | ${ipaddr_src} | 192.168.1.1 |
        """

        # Packetオブジェクトを取得
        packet: Packet = capture[number - 1]
        logger.write(packet.show(), level="INFO")

        # 可変長引数に与えられた文字列をdata_strに連結させる
        # 例えばip, srcを与えられた場合, packet.ip.srcとなる
        data_str = "packet"

        if args:
            for layer in args:
                data_str += f".{layer}"

        try:
            # eval関数で変数data_strの文字列を変数として扱い、packetオブジェクトの属性をstrで取得する
            return eval(f"str({data_str})")

        except AttributeError:
            logger.write(f"{data_str}は存在しません。", level="ERROR")
            raise

        except Exception:
            raise

    @keyword
    def count_total_packets(self, capture: FileCapture) -> int:
        """``filepath`` に指定した場所のpcapファイルを読み込み、パケットの総数をintで返します

        Example:
        | ${capture} = | `Read Pcap File` | /path/to/pcap/file.pcap |
        | ${packet_num} = | `Count Total Packets` | ${capture} |
        | Length Should Be | ${packet_num} | 10000 |
        """

        if capture is None:
            raise FileNotFoundError("pcapファイルが読み込まれていません")

        capture.load_packets()

        return len(capture)

    @keyword
    def expected_packet_should_exist(self, capture: FileCapture, **packet_info) -> None:
        """引数で渡された``key=value``を含むパケットが、pcapファイルに存在するか確認するキーワードです。

        データの指定はpysharkの指定方法に準拠していますが、本キーワードでは可変長引数のkeyには以下のように記述してください。
        ex) ip.src=192.168.1.1, icmp.type=8

        Example:
        | ${capture} = | `Read Pcap File` | /path/to/pcap/file.pcap |
        | `Expected Packet Should Exist` | ${capture} | ip.src=192.168.1.1 | ip.dst=172.16.1.1 |
        """

        capture.load_packets()

        for number, packet in enumerate(capture):

            # 引数によって指定されたパケットの条件数と``end_sign_count``の数が一致した場合、想定パケットは存在する
            # ここでは初期化を実施
            end_sign_count = 0
            for key, value in packet_info.items():
                try:
                    # 可変長引数に与えられた文字列をdata_strに連結させる
                    data_str = "packet"
                    if packet_info:
                        data_str += f".{key}"
                    # eval関数で変数data_strの文字列を変数として扱い、packetオブジェクトの属性をstrで取得する
                    output = eval(f"str({data_str})")

                    if output == value:
                        end_sign_count += 1

                except AttributeError:
                    # 可変長引数に与えられた条件に1つでも一致しなかった場合、次のパケットの確認に移る
                    continue

            if end_sign_count == len(packet_info):
                logger.write(f"packet number: {number+1}\n{packet}")
                # 可変長引数に与えられた条件に全て一致した場合、全ての処理を終了する
                return

        raise Exception("想定パケットがpcapファイルに存在しません")
