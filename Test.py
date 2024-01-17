import os
import subprocess


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print("Command output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print("Command output:")
        print(e.output)


command_to_run = r'"C:\Users\sesa744271\Documents\TestComplete 15 Projects\Analyse_Build\Analyse_Build.pjs"/run'
print(command_to_run)
run_command(command_to_run)
print("Hello World")
