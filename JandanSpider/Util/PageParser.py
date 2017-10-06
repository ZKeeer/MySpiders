import re


def parser(page_content, RegEx):
    result_list = []
    for item in re.findall(RegEx,page_content):
        result_list.append(item)
    return result_list



