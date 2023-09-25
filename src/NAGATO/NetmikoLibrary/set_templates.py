import os
import shutil
import ntc_templates
import NAGATO

# copy ntc-templates and merge it with nagato's templates.

if not os.getenv("NET_TEXTFSM"):

    # get installed templates path
    ntc_templates_path = os.path.join(ntc_templates.__path__[0], "templates")
    nagato_templates_path = os.path.join(NAGATO.__path__[0], "templates")

    # set destination templates path
    if os.name == "posix":
        nagato_data_path = os.path.join(os.environ["HOME"], ".NAGATO")
    if os.name == "nt":
        nagato_data_path = os.path.join(os.environ["LOCALAPPDATA"], "NAGATO")
    merged_template_path = os.path.join(nagato_data_path, "templates")

    if not os.path.isdir(merged_template_path):
        # copy all ntc_templates
        shutil.copytree(ntc_templates_path, merged_template_path)

        # merge nagato_templates
        for file in os.listdir(nagato_templates_path):
            if ".textfsm" in file:
                shutil.copy(os.path.join(nagato_templates_path, file), merged_template_path)

            # merge index of nagato
            if file == "index":
                with open(os.path.join(merged_template_path, "index"), mode='a') as ntc_index:
                    with open(os.path.join(nagato_templates_path, "index")) as nagato_index:
                        nagato_index_contents = nagato_index.read()
                        ntc_index.write(f"\n{nagato_index_contents}")

    # set NET_TEXTFSM
    os.environ["NET_TEXTFSM"] = merged_template_path