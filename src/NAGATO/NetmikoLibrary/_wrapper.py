import os
from functools import wraps
from typing import Any, Iterator, Sequence, TextIO, Union

from netmiko import BaseConnection, ConnectHandler
from robot.api import logger
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError

from .apresia.apresia_amios import AmiosSSH, AmiosTelnet

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
    """Decorator to display the return value as Log in Robot Framework's log.html."""

    @wraps(func)
    def _robot_log(*args, **kwargs):
        output = func(*args, **kwargs)
        logger.write(msg=output, level="INFO")

        return output

    return _robot_log


def host_specify(func):
    """Decorator that passes ``self.cursor`` to host if the ``host`` argument is not specified.

    ``self.cursor`` contains the alias of the first device connected during scenario execution.
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
        """SSH/Telnet connection based on the given connection information.

        ``alias``  is a a unique name that identifies this connection.
        The ``alias`` can be specified as an optional ``host`` argument for each keyword
        to specify the device to run on.

        Example:
        | `Connect` | device_type=cisco_xr | host=192.168.1.1 | alias=Cisco8000 | username=cisco | password=C1sco123! | port=22 |
        """

        if not self.cursor:
            self.cursor = alias

        if not session_log:
            try:
                session_log = os.path.join(BuiltIn().get_variable_value("${OUTPUT DIR}"), f"{alias}.log")
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
            # If the specified device_type does not exist in the platforms supported by Netmiko, look for it in CLASS_MAPPER_ALT.

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
        """Disconnects the connection.

        Example:
        | `Disconnect` | host=Cisco8000 |
        """

        self.connections[host].disconnect()

    @keyword
    def disconnect_all(self):
        """Disconnects all connections.

        Example:
        | `Disconnect All` |
        """

        for connection in self.connections.values():
            connection.disconnect()

    @keyword
    @host_specify
    @robot_log
    def send_command(self, command_string: str, host: str = "", *args, **kwargs):
        """Sends the command specified in ``command_string`` and returns CLI output.

        This keyword wraps the ``send_command`` method of the netmiko package.
        The arguments given to this keyword conform to the ``send_command`` method of the netmiko package.

        Example:
        | ${output} = | `Send Command` | show ip interface brief | host=Cisco8000 |
        | Log | ${output} |
        """

        output = self.connections[host].send_command(command_string=command_string, *args, **kwargs)

        return output

    @keyword
    @host_specify
    @robot_log
    def send_config_set(self, config_commands: Union[str, Sequence[str], Iterator[str], TextIO, None] = None, host: str = "", **kwargs) -> str:
        """Sends the configuration commands specified in ``config_commands`` and
        returns a display of the CLI during that time.

        The ``config_commands`` can be an iterable object containing multiple configuration commands to be sent.
        (Usually it is of type list.)
        If an Iterable object is specified, configuration commands are sent and executed in sequence.

        If it is necessary to shift to Configuration mode, it will do so automatically.
        The Configuration mode is automatically exited after the end of sending configuration commands.

        Example:
        | @{commands} = | Create List | interface Gi1/1 |
        | ... | | ip address 192.168.1.1 255.255.255.0 |
        | ${output} = | `Send Config Set` | ${commands} | host=Cisco8000 |
        """

        return self.connections[host].send_config_set(config_commands=config_commands, **kwargs)

    @keyword
    @host_specify
    def write_channel(self, out_data: str, host: str = ""):
        """Sends the value of ``out_data`` to the communication channel.

        The value to be sent does not include line feed codes unless explicitly stated.
        Command execution must include a control code (such as \\n) in the value to indicate execution.

        Example:
        | `Write Channel` | shutdown -h now\\n |
        """

        self.connections[host].write_channel(out_data=out_data)

    @keyword
    @host_specify
    @robot_log
    def read_channel(self, host: str = ""):
        """Reads the communication channel. Then returns the read string.

        Example:
        | ${output} = | `Read Channel` | host=Cisco8000 |
        | Should Be Equal | ${output} | press return to get started |
        """

        return self.connections[host].read_channel()

    @keyword
    @host_specify
    @robot_log
    def read_until_pattern(self, pattern: str, host: str = "", *args, **kwargs) -> str:
        """Reads the communication channel until the value specified in ``pattern`` is found.
        It then returns the string read up to that point, including the value of patten.

        Example:
        | ${output} = | `Read Until Pattern` | pattern=login: |
        | `Establish Connection` | host=Cisco8000 |
        """

        return self.connections[host].read_until_pattern(pattern=pattern, *args, **kwargs)

    @keyword
    @host_specify
    @robot_log
    def read_until_prompt(self, host: str = "", *args, **kwargs) -> str:
        """Read the communication channel until a prompt is detected.
        It then returns the string read up to that point, including prompts.

        Example:
        | ${output} = | `Read Until Prompt` |
        """

        return self.connections[host].read_until_prompt(*args, **kwargs)

    @keyword
    @host_specify
    @robot_log
    def serial_login(self, host: str = "", *args, **kwargs) -> str:
        """Performs CLI login operations in serial communications.

        Example:
        | `Serial Login` | host=Cisco8000 |
        """

        return self.connections[host].serial_login(*args, **kwargs)

    @keyword
    @host_specify
    @robot_log
    def telnet_login(self, host: str = "", *args, **kwargs) -> str:
        """Performs CLI login operations in Telnet communications.

        Example:
        | `Telnet Login` | host=Cisco8000 |
        """

        return self.connections[host].telnet_login(*args, **kwargs)

    @keyword
    @host_specify
    def session_preparation(self, host: str = ""):
        """Prepare for CLI operation after connection is established.

        This keyword performs the following
        - Find prompts
        - Set terminal width to default value
        - Disable page breaks in the terminal

        Example:
        | `Establish Connection` | host=Cisco8000 |
        | `Session Preparation` | host=Cisco8000 |
        """

        self.connections[host].session_preparation()

    @keyword
    @host_specify
    def establish_connection(self, host: str = ""):
        """Establishes a connection to the destination specified in ``host`` .

        The information used to establish the connection is that given by `Connect` .

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
        """Transfers to privileged mode and returns a prompt display after the transition.

        If password input is required for privileged mode transition,
        the password must be supplied as the value of the keyword argument ``secret`` when calling `Connect`.

        Example:
        | ${output} = | `Enable` | host=Cisco8000 |
        | Should Contain | ${output} | # |
        """

        return self.connections[host].enable(*args, **kwargs)

    @keyword
    @host_specify
    @robot_log
    def exit_enable_mode(self, host: str = "", *args, **kwargs):
        """Exits from privileged mode and returns a prompt display after transition.

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
        """Executes the function given as ``method`` and returns its return value.

        The functions given must be executable by netmiko.

        Example:
        | ${output} = | `Call` | send_command | command_string=show ip interface brief | host=Cisco8000 |
        | Log | ${output} |
        """

        return eval("self.connections[host]." + method + "(*args, **kwargs)")

    @keyword
    @host_specify
    @robot_log
    def enter_config_mode(self, host: str = "", *args, **kwargs):
        """Enters Configuration Mode.

        Example:
        | `Enter Config Mode` | host=Cisco8000 |
        """

        return self.connections[host].config_mode(*args, **kwargs)

    @keyword
    @host_specify
    @robot_log
    def exit_config_mode(self, host: str = "", *args, **kwargs):
        """Exits from Configuration Mode.

        Example:
        | `Exit Config Mode` | host=Cisco8000 |
        """

        return self.connections[host].exit_config_mode(*args, **kwargs)
