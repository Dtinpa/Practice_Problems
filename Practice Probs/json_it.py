#!/usr/bin/env python

import json

def json_iterate(jsn, search, path):
	for key in jsn:
		if isinstance(jsn[key], list):
			p = path + key + " -> "
			json_iterate(jsn[key], search, p)
		
		if jsn[key] == search:
			path += search + "\n"
			print path
			return
		print key

f = open("json.txt", "r")

json = json.load(f)

json_iterate(json, "dailyprogrammer", "")

