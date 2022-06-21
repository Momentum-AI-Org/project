from utils.clio import run_command

class APIConfig():
    PROJECT_NAME = 'default'

def setup_script():
    assert APIConfig.PROJECT_NAME != 'default', (
        'Make sure to set the project name before running this setup script!'
    )
    print(f'Setting up project {APIConfig.PROJECT_NAME}...')
    run_command(f'pip install requirements_{APIConfig.PROJECT_NAME}.txt')


