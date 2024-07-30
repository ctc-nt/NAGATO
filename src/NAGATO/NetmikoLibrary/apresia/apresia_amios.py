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

import time
from typing import Any, Dict, Iterator, List, Optional, Sequence, TextIO, Union

from netmiko import BaseConnection


class Amios(BaseConnection):
    """Apresia AMIOS's class"""

    def disable_paging(
        self,
        command: str = "configure terminal lines 0",
        delay_factor: Optional[float] = None,
        cmd_verify: bool = True,
        pattern: Optional[str] = None,
    ) -> str:
        return super().disable_paging(command, delay_factor, cmd_verify, pattern)

    def send_command(
        self,
        command_string: str,
        expect_string: Optional[str] = None,
        read_timeout: float = 10,
        delay_factor: Optional[float] = None,
        max_loops: Optional[int] = None,
        auto_find_prompt: bool = True,
        strip_prompt: bool = True,
        strip_command: bool = True,
        normalize: bool = True,
        use_textfsm: bool = False,
        textfsm_template: Optional[str] = None,
        use_ttp: bool = False,
        ttp_template: Optional[str] = None,
        use_genie: bool = False,
        cmd_verify: bool = True,
    ) -> Union[str, List[Any], Dict[str, Any]]:
        # プロンプト+コマンドの文字数が80以上となった場合、cmd_verify=Falseにする
        if len(self.base_prompt + command_string) > 78:
            cmd_verify = False

        return super().send_command(
            command_string,
            expect_string,
            read_timeout,
            delay_factor,
            max_loops,
            auto_find_prompt,
            strip_prompt,
            strip_command,
            normalize,
            use_textfsm,
            textfsm_template,
            use_ttp,
            ttp_template,
            use_genie,
            cmd_verify,
        )

    def send_config_set(
        self,
        config_commands: Union[str, Sequence[str], Iterator[str], TextIO, None] = None,
        *,
        exit_config_mode: bool = False,
        read_timeout: Optional[float] = None,
        delay_factor: Optional[float] = None,
        max_loops: Optional[int] = None,
        strip_prompt: bool = False,
        strip_command: bool = False,
        config_mode_command: Optional[str] = None,
        cmd_verify: bool = True,
        enter_config_mode: bool = False,
        error_pattern: str = "%",
        terminator: str = r"#",
        bypass_commands: Optional[str] = None,
    ) -> str:
        # configモードへの遷移を行わず、"configure"から始まるコマンドで設定を投入することを想定するため、
        # exit_config_mode, enter_config_modeのデフォルトはFalseとする
        return super().send_config_set(
            config_commands,
            exit_config_mode=exit_config_mode,
            read_timeout=read_timeout,
            delay_factor=delay_factor,
            max_loops=max_loops,
            strip_prompt=strip_prompt,
            strip_command=strip_command,
            config_mode_command=config_mode_command,
            cmd_verify=cmd_verify,
            enter_config_mode=enter_config_mode,
            error_pattern=error_pattern,
            terminator=terminator,
            bypass_commands=bypass_commands,
        )

    def serial_login(
        self,
        pri_prompt_terminator: str = r":#\s*$",
        alt_prompt_terminator: str = r":>\s*$",
        username_pattern: str = r"login",
        pwd_pattern: str = r"assword",
        delay_factor: float = 1,
        max_loops: int = 20,
    ) -> str:
        return super().serial_login(
            pri_prompt_terminator,
            alt_prompt_terminator,
            username_pattern,
            pwd_pattern,
            delay_factor,
            max_loops,
        )

    def session_preparation(self) -> None:
        # プロンプトを表示させるため改行コードを送信する
        self.write_channel(self.RETURN)
        time.sleep(0.5)

        return super().session_preparation()


class AmiosSSH(Amios):
    pass


class AmiosTelnet(Amios):
    pass
