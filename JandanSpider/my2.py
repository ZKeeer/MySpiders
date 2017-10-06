import json

page_list = []

for index in range(1, 169):
    page_list.append("http://jandan.net/ooxx/page-{}#comments".format(index))
print(page_list[-1], index)