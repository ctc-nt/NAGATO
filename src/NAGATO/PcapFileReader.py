"""
Copyright 2024 ITOCHU Techno-Solutions Corporation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

from pyshark import FileCapture
from pyshark.packet.packet import Packet
from robot.api import logger
from robot.api.deco import keyword, library

from NAGATO.version import get_version


@library
class PcapFileReader:
    """PcapFileReader is a Robot Framework library for packet capture file verification.

    This library uses pyshark package. Therefore it needs tshark installed on a machine.
    """

    ROBOT_LIBRARY_SCOPE = "SUITE"
    ROBOT_LIBRARY_VERSION = get_version()

    def __init__(self):
        pass

    @keyword
    def read_pcap_file(self, source: str, **kwargs) -> FileCapture:
        """Read the given pcap file and parse into FileCapture structure.

        Example:
        | ${capture} = | `Read Pcap File` | source=/path/to/pcap/file.pcap |
        """

        return FileCapture(source, **kwargs)

    @keyword
    def get_packet_data(self, capture: FileCapture, number: int, *args: str) -> str:
        """Return the given ``number`` packet data in ``capture`` .

        In the variable arguments, give the value to retrieve separately for each hierarchy.
        The value format follows the pyshark expression.
        For example, when expressed as ``packet.ip.src`` in pyshark, the variable arguments are given values in the order of ``ip`` and ``src``.

        Example:
        | ${capture} = | `Read Pcap File` | /path/to/pcap/file.pcap |
        | ${ipaddr_src} = | `Get Packet Data` | ${capture} | ${1} | ip | src |
        | Should Be Equal | ${ipaddr_src} | 192.168.1.1 |
        """

        packet: Packet = capture[number - 1]
        logger.write(packet.show(), level="INFO")

        # concatenate values given to variable arguments to data_str
        data_str = "packet"

        if args:
            for layer in args:
                data_str += f".{layer}"

        try:
            # Treat the value of data_str as Packet object
            return eval(f"str({data_str})")

        except AttributeError:
            logger.write(f"{data_str} does not exist.", level="ERROR")
            raise

        except Exception:
            raise

    @keyword
    def count_total_packets(self, capture: FileCapture) -> int:
        """Return amount of packet in ``capture`` .

        Example:
        | ${capture} = | `Read Pcap File` | /path/to/pcap/file.pcap |
        | ${packet_num} = | `Count Total Packets` | ${capture} |
        | Length Should Be | ${packet_num} | 10000 |
        """

        capture.load_packets()

        return len(capture)

    @keyword
    def packet_should_exist(self, capture: FileCapture, **packet_info):
        """Fails if there is no packet in ``capture`` that matches the conditions given to ``packet_info`` .

        In the ``packet_info`` , give the any conditions to verify. Conditions are expressed as pyshark format.

        ex.) ip.src=192.168.1.1, icmp.type=8

        Note: Python code cannot give keyword including periods as keyword arguments. Use dictionary unpacking instead.

        Example:
        | ${capture} = | `Read Pcap File` | /path/to/pcap/file.pcap |
        | `Packet Should Exist` | ${capture} | ip.src=192.168.1.1 | ip.dst=172.16.1.1 |
        """

        capture.load_packets()

        for number, packet in enumerate(capture):

            end_sign_count = 0
            for key, value in packet_info.items():
                try:
                    data_str = "packet"
                    if packet_info:
                        data_str += f".{key}"

                    output = eval(f"str({data_str})")

                    if output == value:
                        end_sign_count += 1

                except AttributeError:
                    continue

            if end_sign_count == len(packet_info):
                logger.write(f"packet number: {number+1}\n{packet}")
                return

        raise AssertionError("There are no packets matching the given conditions.")
