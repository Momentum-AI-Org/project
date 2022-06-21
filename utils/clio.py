"""For running commands on the terminal"""
from subprocess import PIPE, run
from typing import Tuple

def run_command(command: str) -> Tuple[str, str]:
    """Run command on google colab machine and get output"""
    print(f'> {command}')
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.stdout, result.stderr