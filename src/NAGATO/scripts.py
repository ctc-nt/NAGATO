from pathlib import Path
import os
import shutil
import ntc_templates
import NAGATO

def copy_templates():
    """copy ntc-templates and merge it with nagato's templates."""

    ntc_templates_path = os.path.join(ntc_templates.__path__[0], "templates")
    nagato_templates_path = os.path.join(NAGATO.__path__[0], "templates")

    for file in os.listdir(ntc_templates_path):
        if ".textfsm" in file:
            shutil.copy(os.path.join(ntc_templates_path, file), nagato_templates_path)

        if file == "index":
            with open(os.path.join(ntc_templates_path, file)) as ntc_index:
                nagato_index = Path(os.path.join(nagato_templates_path, "index"))
                nagato_index_contents = nagato_index.read_text()
                ntc_index_contents = ntc_index.read()
                nagato_index.write_text(f"{ntc_index_contents}\n{nagato_index_contents}")

    # TODO: 環境変数NET_TEXTFSMを定義