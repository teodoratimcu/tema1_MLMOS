import sys
import json
import subprocess
import os

with open("config.json", "r") as f:
    config = json.load(f)
    print "Config file:"
    print(config)

commands = [
    "hostnamectl set-hostname " + config["hostname"],
    "yum -y install git",
    "git --version",
]

for c in commands:
    print "Running command: " + c
    subprocess.call(c, shell=True)

if not os.path.exists("tema1_MLMOS"):
    print "Cloning git repository"
    subprocess.call("git clone https://github.com/teodoratimcu/tema1_MLMOS.git", shell=True)
else:
    print "Changing directory to tema1_MLMOS"
    os.chdir("tema1_MLMOS")
    print "Pulling git repository"
    subprocess.call("git pull", shell=True)
