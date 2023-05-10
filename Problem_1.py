#!/usr/bin/python

"""
DOCSTRING
"""

import argparse
import pathlib
import nerfstudio_easy
import os, shutil

# Parse python runtime args
parser = argparse.ArgumentParser(description="Takes 2 mandatory inputs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('video', help="Full path to video file")
parser.add_argument("-t", '--nerf-type', default="nerfacto", help="Define what type of NeRF model")
args = parser.parse_args()
config = vars(args)
print(config)

# TODO Validate video file and path
# TODO Validate nerf-type params

# Get project workspace full path for passing into docker run
project_path = pathlib.Path(__file__).parent.resolve()
print("Project Full Path: "+str(project_path))

# Initilize nerfstudio stuff for easier execution
my_nerfstudio = nerfstudio_easy()

# Wipe data/* directory
nerfstudio_easy.cleanup('data')

# Copy video file to /workspace/data directory
print('Video Full Path: '+args.video)
video_filename = os.path.basename(args.video)
print('Video File Name: '+video_filename)
video_data_path = os.path.join(project_path, "data", video_filename)
shutil.copy2(args.video,video_data_path)

# Setup nerfstudio execution command
nerf_type = 'nerfacto'

cmd_steps = [['ns-process-data', 'video', '--data', f'data/{video_filename}', '--output-dir', 'data'],
             ['ns-train', f'{nerf_type}', '--data', 'data'],
             ['ns-render', '--load-config', 'outputs/config.yml']]

step_info = 'WARNING: Each step of the process can take 30+ minutes to complete successfully.'

for step_index in range(len(cmd_steps)):
    cmd_step = cmd_steps[step_index]
    print('----------------------------')
    print(cmd_step)
    print(step_info)
    nerfstudio_easy.run(cmd_step)