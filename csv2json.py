import csv
import json
import datetime

csvfile = open('covid19-belgium-latest.csv', 'r')
jsonfile = open('covid19-belgium.json', 'w')

fieldnames = ("date","daily_tests","daily_cases","cumul_tests","cumul_cases","icu","deceased")
reader = csv.DictReader( csvfile, fieldnames)

result = dict()
result["last_update"] = datetime.datetime.now().isoformat()
result["data"] = list()

for row in reader:
	result["data"].append(row)

json.dump(result, jsonfile)
jsonfile.write('\n')
