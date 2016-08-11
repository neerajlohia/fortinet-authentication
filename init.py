import json
import os
import subprocess

username = input("Enter your username : ").strip()
password = input("Enter your password : ").strip()

fileobj = open("information.json","w")
info = {}
info["username"] = username
info["password"] = password
json.dump(info,fileobj)
fileobj.close()
subprocess.Popen("cp auth information.json /etc/network/if-up.d/", shell=True)
subprocess.Popen("chmod +x /etc/network/if-up.d/auth", shell=True)
outp = subprocess.Popen("ls /sys/class/net/", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out,err = outp.communicate()
out = out.decode("utf-8").split()
out = out.sort()
string = "\nauto " + out[-1] + "\npost-up /etc/network/if-up.d/auth"
fileobj = open("/etc/network/interfaces","a")
fileobj.write(string)
fileobj.close()