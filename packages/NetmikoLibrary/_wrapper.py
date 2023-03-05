import os
from functools import wraps
from typing import Iterator, Sequence, TextIO, Union, Any

from .apresia.apresia_amios import AmiosSSH, AmiosTelnet
from netmiko import BaseConnection, ConnectHandler
from robot.api import logger
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError

CLASS_MAPPER_BASE_ALT = dict()
CLASS_MAPPER_BASE_ALT["apresia_amios"] = AmiosSSH

# Also support keys that end in _ssh
new_mapper = dict()
for key, value in CLASS_MAPPER_BASE_ALT.items():
    new_mapper[key] = value
    alt_key = key + "_ssh"
    new_mapper[alt_key] = value
CLASS_MAPPER_ALT = new_mapper

# add telnet driver
CLASS_MAPPER_ALT["apresia_amios_telnet"] = AmiosTelnet

platforms_alt = list(CLASS_MAPPER_ALT.keys())
platforms_alt.sort()
platforms_base_alt = list(CLASS_MAPPER_BASE_ALT.keys())
platforms_base_alt.sort()
platforms_alt_str = "\n".join(platforms_base_alt)
platforms_alt_str = "\n" + platforms_alt_str


def robot_log(func):
    """戻り値をRobot Frameworkのlog.htmlにLogとして表示させるデコレータ"""

    @wraps(func)
    def _robot_log(*args, **kwargs):
        output = func(*args, **kwargs)
        logger.write(msg=output, level="INFO")

        return output

    return _robot_log


def host_specify(func):
    """引数hostを指定していない場合、hostに ``self.cursor`` を渡すデコレータ

    ``self.cursor`` にはシナリオ実行時に最初に接続したデバイスのaliasが格納されている
    """

    @wraps(func)
    def _host_specify(*args, **kwargs):
        self = args[0]
        if "host" in kwargs:
            return func(*args, **kwargs)
        else:
            return func(*args, host=self.cursor, **kwargs)

    return _host_specify


class NetmikoWrapper:
    """Netmiko Wrapper Class"""

    def __init__(self):
        self.cursor: str = ""
        self.connections: dict[str, BaseConnection] = {}

    @keyword
    def connect(
        self,
        device_type: str,
        host: str,
        alias: str,
        username: str,
        password: str,
        port: int = None,
        session_log: str = None,
        **kwargs,
    ):
        """与えられた接続情報を元にSSH/Telnet接続を行います。

        ``alias`` にはこの接続を識別する一意の名前を与えてください。
        ``alias`` は各キーワードのオプション引数 ``host`` として指定することで、実行対象のデバイスを指定することができます。

        Example:
        | `Connect` | device_type=cisco_xr | host=192.168.1.1 | alias=Cisco8000 | username=cisco | password=C1sco123! | port=22 |
        """

        if not self.cursor:
            self.cursor = alias

        if not session_log:
            try:
                session_log = os.path.join(
                    BuiltIn().get_variable_value("${OUTPUT DIR}"), f"{alias}.log"
                )
            except RobotNotRunningError:
                session_log = None

        if (not port) and ("telnet" in device_type):
            port = 23
        elif not port:
            port = 22

        logger.write(
            msg=f"""接続情報:
            {host=}
            {alias=}
            {username=}
            {password=}
            {port=}
            {device_type=}
            {session_log=}""",
            level="INFO",
        )

        try:
            self.connections[alias] = ConnectHandler(
                device_type=device_type,
                host=host,
                username=username,
                password=password,
                port=port,
                session_log=session_log,
                **kwargs,
            )

        except ValueError as error:
            # 指定したdevice_typeがNetmikoがサポートするplatformの中に存在しない場合、CLASS_MAPPER_ALTから探す

            if device_type not in platforms_alt:
                message = "".join((*error.args, "\n\nAnd: ", platforms_alt_str))
                raise ValueError(message)

            self.connections[alias] = CLASS_MAPPER_ALT[device_type](
                device_type=device_type,
                host=host,
                username=username,
                password=password,
                port=port,
                session_log=session_log,
                **kwargs,
            )

    @keyword
    @host_specify
    def disconnect(self, host: str = ""):
        """コネクションの切断処理を行います。

        Example:
        | `Disconnect` | host=Cisco8000 |
        """

        self.connections[host].disconnect()

    @keyword
    def disconnect_all(self):
        """全てのコネクションに対し、切断処理を行います。

        Example:
        | `Disconnect All` |
        """

        for connection in self.connections.values():
            connection.disconnect()

    @keyword
    @host_specify
    @robot_log
    def send_command(self, command_string: str, host: str = "", *args, **kwargs):
        """``command_string`` に指定したコマンドを送信し、CLIの出力を返します。

        このキーワードはnetmikoパッケージの ``send_command`` メソッドをラップしています。
        このキーワードに与えられる引数は同パッケージの ``send_command`` メソッドに準拠します。

        Example:
        | ${output} = | `Send Command` | show ip interface brief | host=Cisco8000 |
        | Log | ${output} |
        """

        output = self.connections[host].send_command(
            command_string=command_string, *args, **kwargs
        )

        return output

    @keyword
    @host_specify
    @robot_log
    def send_config_set(
        self,
        config_commands: Union[str, Sequence[str], Iterator[str], TextIO, None] = None,
        host: str = "",
        **kwargs,
    ) -> str:
        """``config_commands`` に指定した設定コマンドを送信し、その間のCLIの表示を返します。

        ``config_commands`` には、送信する設定コマンドを複数格納したIterableオブジェクトを指定可能です。（通常それはlist型です）
        Iterableオブジェクトを指定した場合、設定コマンドは順番に送信、実行されます。

        Configurationモードへの移行が必要な場合は自動的に移行し、設定コマンドの送信の終了後は自動的にConfigurationモードを終了します。

        Example:
        | @{commands} = | Create List | interface Gi1/1 |
        | ... | | ip address 192.168.1.1 255.255.255.0 |
        | ${output} = | `Send Config Set` | ${commands} | host=Cisco8000 |
        """

        return self.connections[host].send_config_set(
            config_commands=config_commands, **kwargs
        )

    @keyword
    @host_specify
    def write_channel(self, out_data: str, host: str = ""):
        """``out_data`` の値を通信チャネルに送信します。

        送信する値には、明示しない限り改行コードが含まれません。
        コマンド実行には、実行を示す制御コード(\\nなど)を値に含める必要があります。

        Example:
        | `Write Channel` | shutdown -h now\\n |
        """

        self.connections[host].write_channel(out_data=out_data)

    @keyword
    @host_specify
    @robot_log
    def read_channel(self, host: str = ""):
        """通信チャネルを読み込みます。その後、読み込んだ文字列を返します。

        Example:
        | ${output} = | `Read Channel` | host=Cisco8000 |
        | Should Be Equal | ${output} | press return to get started |
        """

        return self.connections[host].read_channel()

    @keyword
    @host_specify
    @robot_log
    def read_until_pattern(self, pattern: str, host: str = "", *args, **kwargs) -> str:
        """``pattern`` に指定した値が検出されるまで、通信チャネルを読み込みます。
        その後、pattenの値を含めた、それまでに読み込んだ文字列を返します。

        Example:
        | ${output} = | `Read Until Pattern` | pattern=login: |
        | `Establish Connection` | host=Cisco8000 |
        """

        return self.connections[host].read_until_pattern(
            pattern=pattern, *args, **kwargs
        )

    @keyword
    @host_specify
    @robot_log
    def read_until_prompt(self, host: str = "", *args, **kwargs) -> str:
        """プロンプトが検出されるまで、通信チャネルを読み込みます。
        その後、プロンプトを含めた、それまでに読み込んだ文字列を返します。

        Example:
        | ${output} = | `Read Until Prompt` |
        """

        return self.connections[host].read_until_prompt(*args, **kwargs)

    @keyword
    @host_specify
    @robot_log
    def serial_login(self, host: str = "", *args, **kwargs) -> str:
        """シリアル通信におけるCLIのログイン操作を行います。

        Example:
        | `Serial Login` | host=Cisco8000 |
        """

        return self.connections[host].serial_login(*args, **kwargs)

    @keyword
    @host_specify
    @robot_log
    def telnet_login(self, host: str = "", *args, **kwargs) -> str:
        """Telnet通信におけるCLIのログイン操作を行います。

        Example:
        | `Telnet Login` | host=Cisco8000 |
        """

        return self.connections[host].telnet_login(*args, **kwargs)

    @keyword
    @host_specify
    def session_preparation(self, host: str = ""):
        """コネクション確立後のCLI操作の準備を行います。

        通常、このキーワードは以下を実行します。
        - プロンプトを検出する
        - ターミナルの幅をデフォルトの値にセットする
        - ターミナルの改ページを無効にする

        Example:
        | `Establish Connection` | host=Cisco8000 |
        | `Session Preparation` | host=Cisco8000 |
        """

        self.connections[host].session_preparation()

    @keyword
    @host_specify
    def establish_connection(self, host: str = ""):
        """``host`` に指定した接続先に対し、コネクションの確立させます。

        コネクションの確立に使用される情報は、`Connect`から与えられたものを使用します。

        Example:
        | `Connect` | device_type=cisco_xr | host=192.168.1.1 | alias=Cisco8000 | username=cisco | password=C1sco123! | port=22 |
        | `Disconnect` | host=Cisco8000 |
        | `Establish Connection` | host=Cisco8000 |
        """

        self.connections[host].establish_connection()

    @keyword
    @host_specify
    @robot_log
    def enable(self, host: str = "", *args, **kwargs) -> str:
        """特権モードへ移行し、移行後のプロンプト表示を返します。

        特権モード移行の際にパスワード入力が必要な場合、 `Connect` 呼び出し時にキーワード引数 ``secret`` の値としてパスワードを与える必要があります。

        Example:
        | ${output} = | `Enable` | host=Cisco8000 |
        | Should Contain | ${output} | # |
        """

        return self.connections[host].enable(*args, **kwargs)

    @keyword
    @host_specify
    @robot_log
    def exit_enable_mode(self, host: str = "", *args, **kwargs):
        """特権モードから退出し、移行後のプロンプト表示を返します。

        Example:
        | `Enable` | host=Cisco8000 |
        | ${output} = | `Send Command` | command_string=show running-config | host=Cisco8000 |
        | `Exit Enable Mode` | host=Cisco8000 |
        """

        return self.connections[host].exit_enable_mode(*args, **kwargs)

    @keyword
    @host_specify
    @robot_log
    def call(self, method: str, host: str = "", *args, **kwargs) -> Any:
        """``method`` に与えた関数を実行し、その戻り値を返します。

        与える関数はnetmikoが実行可能なものに限られます。

        Example:
        | ${output} = | `Call` | send_command | command_string=show ip interface brief | host=Cisco8000 |
        | Log | ${output} |
        """

        return eval("self.connections[host]." + method + "(*args, **kwargs)")
