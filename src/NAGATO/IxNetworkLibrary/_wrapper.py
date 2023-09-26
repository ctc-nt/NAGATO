from ixnetwork_restpy import Files, SessionAssistant
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
