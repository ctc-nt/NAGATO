from os.path import abspath, dirname, join

import pytest
from pyshark import FileCapture

from NAGATO import PcapFileReader

filepath = dirname(abspath(__file__))
pcapfile = "http.pcap"
packet_index = 18
packet_amount = 43
ip_src = "145.254.160.237"
ip_dst = "65.208.228.223"


def test_PcapFileReader():
    PcapFileReader()


def test_read_pcap_file():
    pfr = PcapFileReader()
    capture = pfr.read_pcap_file(join(filepath, pcapfile))

    assert isinstance(capture, FileCapture)


def test_get_packet_data():
    pfr = PcapFileReader()
    capture = pfr.read_pcap_file(join(filepath, pcapfile))

    packet = pfr.get_packet_data(capture, packet_index)
    packet_http = pfr.get_packet_data(capture, packet_index, "http")

    assert isinstance(packet, str)
    assert isinstance(packet_http, str)


def test_get_packet_data_error():
    pfr = PcapFileReader()
    capture = pfr.read_pcap_file(join(filepath, pcapfile))

    with pytest.raises(AttributeError) as e:
        pfr.get_packet_data(capture, packet_index, "udp")

    assert str(e.value) == "No attribute named udp"


def test_count_total_packets():
    pfr = PcapFileReader()
    capture = pfr.read_pcap_file(join(filepath, pcapfile))

    assert pfr.count_total_packets(capture) == packet_amount


def test_expected_packet_should_exist():
    pfr = PcapFileReader()
    capture = pfr.read_pcap_file(join(filepath, pcapfile))

    packet_info = {"ip.src": ip_src, "ip.dst": ip_dst}

    pfr.expected_packet_should_exist(capture, **packet_info)
