import csv
import json
import datetime

csvfile = open('covid19-belgium.csv', 'r', encoding='utf-8-sig')
jsonfile = open('covid19-belgium.json', 'w')

reader = csv.DictReader( csvfile)

result = dict()
result["last_update"] = datetime.datetime.now().isoformat()
result["data"] = list()

for row in reader:
	result["data"].append(row)

json.dump(result, jsonfile)
jsonfile.write('\n')
