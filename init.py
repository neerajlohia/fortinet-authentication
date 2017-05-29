import json
import os
import subprocess

username = raw_input("Enter your username : ").strip()
password = raw_input("Enter your password : ").strip()

fileobj = open("login","w")
info = {}
info["username"] = username
info["password"] = password
temp = "#!/usr/bin/env python\n\ninfo = " + str(info) + "\n\n"
fileobj.write(temp)
fileobj.close()

fileobj = open("login","a")
fileobj2 = open("auth","r")
temp = fileobj2.read()
fileobj.write(temp)
fileobj.close()
fileobj2.close()

outp = subprocess.Popen("cp login /etc/network/if-up.d/;chmod +x /etc/network/if-up.d/login", shell=True)
outp.wait()
subprocess.Popen("rm login", shell=True)
outp = subprocess.Popen("ls /sys/class/net/", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out,err = outp.communicate()
out = out.decode("utf-8").split()
out.sort()
string = "\nauto " + out[-1]
fileobj = open("/etc/network/interfaces","a")
fileobj.write(string)
fileobj.close()
