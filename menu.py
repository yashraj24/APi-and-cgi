#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()
    
form = cgi.FieldStorage()
cmd = form.getvalue("ch")

if cmd == '1' :
    output = subprocess.getstatusoutput("pip3 install awscli --upgrade --user")
    if output[0] == 0:
        print(output[1])
        print("Successfully installed AWS CLI in your system")

    else:
        print("Error")

elif cmd == '2' :
    output = subprocess.getstatusoutput("aws --version")
    if output[0] == 0:
        print(output[1])

    else:
        print("aws not installed")    

