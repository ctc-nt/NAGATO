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
import shutil
from os.path import join

import ntc_templates

import NAGATO


def set_templates():
    """copy ntc-templates and merge them with nagato's templates."""
    if not os.getenv("NET_TEXTFSM"):
        # set destination templates path
        if os.name == "posix":
            dest_templates_path = join(os.environ["HOME"], ".NAGATO", "templates")
        elif os.name == "nt":
            dest_templates_path = join(os.environ["LOCALAPPDATA"], "NAGATO", "templates")

        if not os.path.isdir(dest_templates_path):
            # get installed templates path
            ntc_templates_path = join(ntc_templates.__path__[0], "templates")
            nagato_templates_path = join(NAGATO.__path__[0], "templates")

            # copy all templates
            shutil.copytree(ntc_templates_path, dest_templates_path, ignore=shutil.ignore_patterns("index"))
            shutil.copytree(nagato_templates_path, dest_templates_path, ignore=shutil.ignore_patterns("index"), dirs_exist_ok=True)

            with open(join(ntc_templates_path, "index"), mode="r") as f:
                ntc_index_contents = f.readlines()
            with open(join(nagato_templates_path, "index"), mode="r") as f:
                nagato_index_contents = f.readlines()

            header_line = ntc_index_contents.index("Template, Hostname, Platform, Command\n")

            # insert nagato's index contents to ntc_templates' index
            ntc_index_contents[header_line + 1 : header_line + 1] = nagato_index_contents

            with open(join(dest_templates_path, "index"), mode="w") as f:
                f.writelines(ntc_index_contents)

        # set NET_TEXTFSM
        os.environ["NET_TEXTFSM"] = dest_templates_path
