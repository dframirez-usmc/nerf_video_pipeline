#!/usr/bin/python
"""
DOCSTRING
"""

import argparse
import pathlib
import nerfstudio_easy

parser = argparse.ArgumentParser(description="Takes 1 mandatory inputs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('motion', help="Camera motion file location")
#parser.add_argument('model', help="NeRFacto model file location")
args = parser.parse_args()
config = vars(args)
print(config)

# TODO Validate motion file and path
# TODO Validate model file and path
# TODO Get NeRFacto model type from model file

# Get project workspace full path for passing into docker run
project_path = pathlib.Path(__file__).parent.resolve()
print("Project Path: "+str(project_path))

# Initilize nerfstudio stuff for easier execution
my_nerfstudio = nerfstudio_easy()

# Wipe render/* directory?
#nerfstudio_easy.cleanup('data')

# Setup nerfstudio execution command
cmd_steps = [['ns-render', '--load-config', 'outputs/config.yml']]

step_info = 'INFO: Each step of the process can take 30+ minutes to complete successfully.'

for step_index in range(len(cmd_steps)):
    cmd_step = cmd_steps[step_index]
    print('----------------------------')
    print(cmd_step)
    print(step_info)
    nerfstudio_easy.run(cmd_step)