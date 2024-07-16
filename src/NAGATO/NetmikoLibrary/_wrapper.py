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
from functools import wraps
from os import PathLike
from typing import Any, Iterator, Sequence, TextIO, Union

from netmiko import BaseConnection, ConnectHandler, redispatch
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
    """Displays the return value as a log in Robot Framework's log.html."""

    @wraps(func)
    def _robot_log(*args, **kwargs):
        output = func(*args, **kwargs)
        logger.write(msg=output, level="INFO")

        return output

    return _robot_log


def connection_specify(func):
    """Passes ``self.cursor`` to the connection if the ``alias`` argument is not specified."""

    @wraps(func)
    def _connection_specify(*args, **kwargs):
        self = args[0]
        if "alias" in kwargs:
            return func(*args, **kwargs)
        else:
            return func(*args, alias=self.cursor, **kwargs)

    return _connection_specify


class NetmikoWrapper:
    """Netmiko Wrapper Class"""

    def __init__(self):
        self.cursor: str = ""
        self.connections: dict[str, BaseConnection] = {}

    @keyword
    def connect(self, alias: str, device_type: str, host: str, username: str, password: str, port: int = None, session_log: str = None, **kwargs) -> None:
        """Creates an SSH or Telnet connection based on the given arguments.

        ``alias`` is a unique name that identifies this connection.
        The ``alias`` can be specified as an optional ``alias`` argument for each keyword to specify the connection to run on.

        Example:
        | `Connect` | alias=Cisco8000 | device_type=cisco_xr | host=192.168.1.1 | username=cisco | password=C1sco123! | port=22 |
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
            msg=f"""Connection info:{alias=}\n{device_type=}\n{host=}\n{username=}\n{password=}\n{port=}\n{session_log=}""",
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
            # If the given device_type does not exist in the platforms supported by Netmiko, look for it in CLASS_MAPPER_ALT.

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
    @connection_specify
    def disconnect(self, alias: str = ""):
        """Disconnects the connection.

        Example:
        | `Disconnect` | alias=Cisco8000 |
        """

        self.connections[alias].disconnect()

    @keyword
    def disconnect_all(self):
        """Disconnects all connections.

        Example:
        | `Disconnect All` |
        """

        for connection in self.connections.values():
            connection.disconnect()

    @keyword
    @connection_specify
    @robot_log
    def send_command(self, command_string: str, alias: str = "", *args, **kwargs):
        """Sends the command specified in ``command_string`` and returns CLI output.

        This keyword wraps the ``send_command`` method of the netmiko package.
        The arguments given to this keyword conform to the ``send_command`` method of the netmiko package.

        Example:
        | ${output} = | `Send Command` | show ip interface brief | alias=Cisco8000 |
        | Log | ${output} |
        """

        output = self.connections[alias].send_command(command_string=command_string, *args, **kwargs)

        return output

    @keyword
    @connection_specify
    @robot_log
    def send_config_set(self, config_commands: Union[str, Sequence[str], Iterator[str], TextIO, None] = None, alias: str = "", **kwargs) -> str:
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
        | ${output} = | `Send Config Set` | ${commands} | alias=Cisco8000 |
        """

        return self.connections[alias].send_config_set(config_commands=config_commands, **kwargs)

    @keyword
    @connection_specify
    @robot_log
    def send_config_from_file(self, config_file: Union[str, bytes, "PathLike[Any]"], alias: str = "", **kwargs) -> str:
        """Sends configuration commands down the SSH channel from a file.
        The file is processed line-by-line and each command is sent down the SSH channel.

        **kwargs are passed to send_config_set method.

        Example:
        | ${output} = | `Send Config From File` | config_file=./configs.txt | alias=Cisco8000 |
        """
        return self.connections[alias].send_config_from_file(config_file=config_file, **kwargs)

    @keyword
    @connection_specify
    def write_channel(self, out_data: str, alias: str = ""):
        """Sends the value of ``out_data`` to the communication channel.

        The value to be sent does not include line feed codes unless explicitly stated.
        Command execution must include a control code (such as \\n) in the value to indicate execution.

        Example:
        | `Write Channel` | shutdown -h now\\n |
        """

        self.connections[alias].write_channel(out_data=out_data)

    @keyword
    @connection_specify
    @robot_log
    def read_channel(self, alias: str = ""):
        """Reads the communication channel. Then returns the read string.

        Example:
        | ${output} = | `Read Channel` | alias=Cisco8000 |
        | Should Be Equal | ${output} | press return to get started |
        """

        return self.connections[alias].read_channel()

    @keyword
    @connection_specify
    @robot_log
    def read_until_pattern(self, pattern: str, alias: str = "", *args, **kwargs) -> str:
        """Reads the communication channel until the value specified in ``pattern`` is found.
        It then returns the string read up to that point, including the value of patten.

        Example:
        | ${output} = | `Read Until Pattern` | pattern=login: |
        | `Establish Connection` | alias=Cisco8000 |
        """

        return self.connections[alias].read_until_pattern(pattern=pattern, *args, **kwargs)

    @keyword
    @connection_specify
    @robot_log
    def read_until_prompt(self, alias: str = "", *args, **kwargs) -> str:
        """Read the communication channel until a prompt is detected.
        It then returns the string read up to that point, including prompts.

        Example:
        | ${output} = | `Read Until Prompt` |
        """

        return self.connections[alias].read_until_prompt(*args, **kwargs)

    @keyword
    @connection_specify
    @robot_log
    def serial_login(self, alias: str = "", *args, **kwargs) -> str:
        """Performs CLI login operations in serial communications.

        Example:
        | `Serial Login` | alias=Cisco8000 |
        """

        return self.connections[alias].serial_login(*args, **kwargs)

    @keyword
    @connection_specify
    @robot_log
    def telnet_login(self, alias: str = "", *args, **kwargs) -> str:
        """Performs CLI login operations in Telnet communications.

        Example:
        | `Telnet Login` | alias=Cisco8000 |
        """

        return self.connections[alias].telnet_login(*args, **kwargs)

    @keyword
    @connection_specify
    def session_preparation(self, alias: str = ""):
        """Prepare for CLI operation after connection is established.

        This keyword performs the following
        - Find prompts
        - Set terminal width to default value
        - Disable page breaks in the terminal

        Example:
        | `Establish Connection` | alias=Cisco8000 |
        | `Session Preparation` | alias=Cisco8000 |
        """

        self.connections[alias].session_preparation()

    @keyword
    @connection_specify
    def establish_connection(self, alias: str = ""):
        """Establishes a connection to the destination specified in ``alias`` .

        The information used to establish the connection is that given by `Connect` .

        Example:
        | `Connect` | device_type=cisco_xr | alias=192.168.1.1 | alias=Cisco8000 | username=cisco | password=C1sco123! | port=22 |
        | `Disconnect` | alias=Cisco8000 |
        | `Establish Connection` | alias=Cisco8000 |
        """

        self.connections[alias].establish_connection()

    @keyword
    @connection_specify
    @robot_log
    def enable(self, alias: str = "", *args, **kwargs) -> str:
        """Transfers to privileged mode and returns a prompt display after the transition.

        If password input is required for privileged mode transition,
        the password must be supplied as the value of the keyword argument ``secret`` when calling `Connect`.

        Example:
        | ${output} = | `Enable` | alias=Cisco8000 |
        | Should Contain | ${output} | # |
        """

        return self.connections[alias].enable(*args, **kwargs)

    @keyword
    @connection_specify
    @robot_log
    def exit_enable_mode(self, alias: str = "", *args, **kwargs):
        """Exits from privileged mode and returns a prompt display after transition.

        Example:
        | `Enable` | alias=Cisco8000 |
        | ${output} = | `Send Command` | command_string=show running-config | alias=Cisco8000 |
        | `Exit Enable Mode` | alias=Cisco8000 |
        """

        return self.connections[alias].exit_enable_mode(*args, **kwargs)

    @keyword
    @connection_specify
    @robot_log
    def call(self, method: str, alias: str = "", *args, **kwargs) -> Any:
        """Executes the function given as ``method`` and returns its return value.

        The functions given must be executable by netmiko.

        Example:
        | ${output} = | `Call` | send_command | command_string=show ip interface brief | alias=Cisco8000 |
        | Log | ${output} |
        """

        return eval("self.connections[alias]." + method + "(*args, **kwargs)")

    @keyword
    @connection_specify
    @robot_log
    def enter_config_mode(self, alias: str = "", *args, **kwargs):
        """Enters Configuration Mode.

        Example:
        | `Enter Config Mode` | alias=Cisco8000 |
        """

        return self.connections[alias].config_mode(*args, **kwargs)

    @keyword
    @connection_specify
    @robot_log
    def exit_config_mode(self, alias: str = "", *args, **kwargs):
        """Exits from Configuration Mode.

        Example:
        | `Exit Config Mode` | alias=Cisco8000 |
        """

        return self.connections[alias].exit_config_mode(*args, **kwargs)

    @keyword
    @connection_specify
    def redispatch(self, device_type: str, alias: str = "", session_prep: bool = True):
        """Dynamically change Netmiko object's class to proper class.
        Generally used with terminal_server device_type when you need to redispatch after interacting
        with terminal server.

        Example:
        | `Redispatch` | alias=Cisco8000 | device_type=cisco_xr | session_prep=True |
        """

        redispatch(self.connections[alias], device_type, session_prep)
