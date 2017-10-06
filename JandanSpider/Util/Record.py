import json
import os
primary_level = "./Record/"
second_level = "./Record/record.json"

# "lastest_page_num":0, "lastest_page_url":None, "viewed":[]

def CheckPath(file_name=second_level):
    if not os.path.exists(primary_level):
        os.mkdir(primary_level)
    if not os.path.exists(file_name):
        with open(file_name, "w") as fw:
            fw.write(json.dumps({"lastest_page_num": 0, "lastest_page_url": None, "viewed": []}))

def Read(read_path=second_level):
    CheckPath(read_path)
    with open(read_path, "r") as fr:
        rec = json.loads(fr.read())
    return rec


def Write(data, write_path=second_level):
    CheckPath(write_path)
    with open(write_path, "w") as fw:
        fw.write(json.dumps(data))
