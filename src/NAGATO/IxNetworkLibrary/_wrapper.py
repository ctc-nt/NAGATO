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

import os
import time

from ixnetwork_restpy import Files, SessionAssistant, TestPlatform
from robot.api import logger
from robot.api.deco import keyword


class IxNetworkRestpyWrapper:
    """IxNetworkRestpy Wrapper Class"""

    def __init__(self):
        self.session_assistant: SessionAssistant = None

    @keyword
    def connect_to_test_server(self, api_server_ip: str, port: str, log_filename: str):
        """Connect to test server.

        `api_server_ip` is the IP address of the server to connect to where test sessions will be created or connected to.

        `port` is the rest port of the test server to connect to.

        `log_filename` is the name of the logger log filename.

        Example:
        | `Connect To API Server` = | api_server_ip=192.168.0.1 | port=443 | log_filename=ixia_api.log |
        """
        self.session_assistant = SessionAssistant(
            IpAddress=api_server_ip,
            RestPort=port,
            ClearConfig=True,
            LogLevel="all",
            LogFilename=log_filename,
        )

        self.IxNetwork = self.session_assistant.Ixnetwork

    @keyword
    def disconnect_from_test_server(self):
        """Disconnect from test server.

        Example:
        | `Disconnect To API Server` |
        """
        if self.session_assistant.TestPlatform.Platform != "windows":
            self.session_assistant.Session.remove()

    @keyword
    def load_config(self, config_file: str):
        """Executes the loadConfig operation on the server.

        Load an existing configuration file.

        `config_file` is the ixconfig file to be loaded.

        Example:
        | `Load Config` | test.ixconfig |
        """
        self.IxNetwork.LoadConfig(Files(config_file, local_file=True))
        logger.write(f"Loaded {config_file} successfully.")

    @keyword
    def assign_ports(self, port_list: list):
        portMap = self.session_assistant.PortMapAssistant()
        vport_list = self.IxNetwork.Vport.find()
        if len(port_list) == len(vport_list):
            for index, port in enumerate(port_list):
                if len(port) == 3:
                    portName = vport_list[index].Name
                    portMap.Map(IpAddress=port[0], CardId=port[1], PortId=port[2], Name=portName)
                else:
                    raise AssertionError("Port variable does not have 3 components.")

            portMap.Connect(ForceOwnership=False)

        else:
            raise AssertionError("Lengths of given ports_list and Vport_list do not match.")

    @keyword
    def release_ports(self):
        for vport in self.IxNetwork.Vport.find():
            vport.ReleasePort()

    @keyword
    def start_all_protocols(self):
        self.IxNetwork.StartAllProtocols(Arg1="sync")

        self.IxNetwork.info("Verify protocol sessions\n")
        protocolSummary = self.session_assistant.StatViewAssistant("Protocols Summary")
        protocolSummary.CheckCondition("Sessions Not Started", protocolSummary.EQUAL, 0)
        self.IxNetwork.info(protocolSummary)

    @keyword
    def stop_all_protocols(self):
        self.IxNetwork.info("Stopped Packet Protocol.")
        self.IxNetwork.StopAllProtocols()

    @keyword
    def apply_traffic(self):
        self.IxNetwork.Traffic.Apply()

    @keyword
    def start_all_traffic(self):
        self.IxNetwork.Traffic.StartStatelessTrafficBlocking()

    @keyword
    def stop_all_traffic(self):
        self.IxNetwork.Traffic.StopStatelessTrafficBlocking()

    @keyword
    def get_statistics(self, view: str, index: int = 0):
        trafficItemStatistics = self.session_assistant.StatViewAssistant(view)

        # 取得したstatic viewのStatisticsを返す
        rows = trafficItemStatistics.Rows[index]
        self.IxNetwork.info(rows)
        return rows

    @keyword
    def download_traffic_csv_file(self, caption: str, file_name: str, output_dir: str, api_server_ip: str, seconds: int):
        view = self.IxNetwork.Statistics.View.find(Caption=caption)

        remote_csv_filename = "%s/%s" % (self.IxNetwork.Statistics.CsvFilePath, view.CsvFileName)
        local_csv_filename = "%s/%s.csv" % (output_dir, file_name)

        # traffic印加statsを指定した秒数の間、取得する
        view.update(EnableCsvLogging=True)
        time.sleep(seconds)
        self.IxNetwork.Statistics.EnableCsvLogging = False

        test_platform = TestPlatform(api_server_ip).Sessions.find()[0]
        test_platform.DownloadFile(remote_csv_filename, local_csv_filename)

    @keyword
    def take_snapshot_and_download(self, caption: str, name: str, output_dir: str):
        # snapshotに必要なインスタンス生成
        self.session = self.session_assistant.Session
        self.statistics = self.IxNetwork.Statistics
        self.csvsnapshot = self.statistics.CsvSnapshot

        # csvsnapshotインスタンスの持つ情報の更新
        self.csvsnapshot.update(
            CsvName=name,
            CsvLocation=self.statistics.CsvFilePath,
            SnapshotViewCsvGenerationMode="overwriteCSVFile",
            SnapshotViewContents="allPages",
            Views=self.statistics.View.find(Caption=caption),
        )

        self.IxNetwork.info(self.csvsnapshot)

        self.csvsnapshot.TakeCsvSnapshot()
        file_name = name + ".csv"

        # ダウンロード元ファイルとダウンロード先ファイルを指定し、ダウンロードを実行
        remote_filename = os.path.normpath(os.path.join(self.statistics.CsvFilePath, file_name))
        local_filename = os.path.normpath(os.path.join(output_dir, file_name))
        self.session.DownloadFile(remote_filename, local_filename)

    @keyword
    def start_capture(self):
        self.IxNetwork.info("Started Packet Capture.")
        self.IxNetwork.StartCapture()

    @keyword
    def stop_capture(self):
        self.IxNetwork.info("Stopped Packet Capture.")
        self.IxNetwork.StopCapture()

    @keyword
    def select_captured_vport(self, index: int, vport_name: str):
        # indexによりvportを指定する
        vport = self.IxNetwork.Vport.find()[index]

        # remote上で保存されるcaptureファイルはvport.Nameから命名されるため、指定したNameにupdate
        vport.update(Name=vport_name)

        # trafficDataをcaptureするための設定
        vport.RxMode = "captureAndMeasure"
        vport.Capture.HardwareEnabled = True

        self.IxNetwork.info("Configured Vport for Packet Capture.")

    @keyword
    def save_capture_file(self):
        # リモート上のファイル保存先をインスタンスから取得するため、生成
        self.statistics = self.IxNetwork.Statistics
        self.csvsnapshot = self.statistics.CsvSnapshot

        # 指定したリモートパスにpcapファイルを保存
        self.IxNetwork.SaveCaptureFiles(self.csvsnapshot.CsvLocation)

        self.IxNetwork.info("Saved pcap file.")

    @keyword
    def download_capture_file(self, vport_name: str, file_name: str, output_dir: str):
        # downloadに必要なインスタンス生成
        self.session = self.session_assistant.Session
        self.statistics = self.IxNetwork.Statistics
        self.csvsnapshot = self.statistics.CsvSnapshot

        local_filename = os.path.normpath(os.path.join(output_dir, file_name))
        # HardwareEnabled = Trueによりdataのcaptureが可能になっており,HWがリモートのファイル名に付与されるため、"_HWを追加"
        self.session.DownloadFile(f"{self.csvsnapshot.CsvLocation}/{vport_name}_HW.cap", local_filename)

        self.IxNetwork.info("Downloaded the pcap file.")

    @keyword
    def start_specified_traffic_item(self, index: int):
        """
        indexによって指定したTrafficItemを流します。
        """

        traffic_item = self.IxNetwork.Traffic.TrafficItem.find()[index]
        traffic_item.StartStatelessTrafficBlocking()

    @keyword
    def stop_specified_traffic_item(self, index: int):
        """
        indexによって指定したTrafficItemを停止します。
        """

        traffic_item = self.IxNetwork.Traffic.TrafficItem.find()[index]
        traffic_item.StopStatelessTrafficBlocking()
