from setuptools import setup
import os
import shutil

# netmikoのtextfsmを参照するパスを設定
# os.environ["NET_TEXTFSM"] = "templates"
print(f"パスは{os.getcwd()}です。")
setup()

import ntc_templates
# get ntc_templates path
templates_path = os.path.join(ntc_templates.__path__[0], "templates")

# 内容をコピーしてこっちのtemplatesディレクトリにもってくる
# .textfsmはそのままコピー
for file, i in os.listdir(templates_path):
    if ".textfsm" in file:
        new_path = shutil.move(templates_path[i], "templates")
    if file == "index":
        with open(templates_path[i], mode='a') as remote_index:
            with open("index", mode='a') as local_index:
                # indexは末尾に追記する
                remote_index.write(local_index)