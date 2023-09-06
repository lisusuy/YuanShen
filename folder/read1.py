import os
import subprocess

def run_command(command):
    subprocess.call(command)

run_command('ls')
os.system('ls')
os.system('ls')