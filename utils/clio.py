"""For running commands on the terminal"""
from subprocess import PIPE, run

def run_command(command: str) -> str:
    """Run command on google colab machine and get output"""
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout, result.stderr