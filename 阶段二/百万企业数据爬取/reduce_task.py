import json
member_num = 3
session = 0
source_file_json_prefix = "company_list"
total = []
for i in range(member_num):
    with open("task/"+source_file_json_prefix+str(i)+".json", 'r', encoding='utf-8') as fd:
        total += json.loads(fd.read())

with open("task/" + source_file_json_prefix + ".json", 'w', encoding='utf-8') as fd:
    fd.write(json.dumps(total, ensure_ascii=False))
