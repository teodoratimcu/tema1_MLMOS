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

if os.path.exists("tema1_MLMOS"):
    print "Removing tema1_MLMOS"
    subprocess.call("rm -rf tema1_MLMOS", shell=True)

print "Cloning git repository"
subprocess.call("git clone https://github.com/teodoratimcu/tema1_MLMOS.git", shell=True)
os.chdir("tema1_MLMOS")

print "Setting permissions for bootstrap.sh"
subprocess.call("chmod 777 bootstrap.sh", shell=True)

print "Starting bootstrap.sh"

bootstrap_log = open("/var/log/system-bootstrap.log", "w")

subprocess.call("./bootstrap.sh", shell=True, stdout=bootstrap_log, stderr=bootstrap_log)