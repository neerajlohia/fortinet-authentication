import json

username = input("Enter your username : ").strip()
password = input("Enter your password : ").strip()

fileobj = open("information.json","w")
info = {}
info["username"] = username
info["password"] = password
json.dump(info,fileobj)
fileobj.close()