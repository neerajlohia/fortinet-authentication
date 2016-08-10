#!/usr/bin/env python
import ast
import requests
import re

reqobj = requests.get('http://www.google.com')
url = str(reqobj.url)

if "fgtauth" in url:
	magic = re.search('http.*\?',url).group()
	magic = url.replace(magic,"")
	fileobj = open("information.json","r")
	info = ast.literal_eval(fileobj.read())
	info["magic"] = magic
	reqobj = requests.post(url, data = info, timeout = (12.4, 5))
	fileobj.close()