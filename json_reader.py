import json

with open('test_manifest.json') as jsonfile:
	json_obj = json.load(jsonfile)
	print(json_obj['title'])