#!/usr/bin/python
"""
DOCSTRING
"""

import argparse
import pathlib
import nerfstudio_runner as ns
import os, shutil

# Parse python args at runtime
parser = argparse.ArgumentParser(description="Create a NeRF from a video recording.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('video', help="Full path to video file")
parser.add_argument("-t", '--nerf-type', 
                    default="nerfacto", 
                    help="Define what type of NeRF model")
args = parser.parse_args()
config = vars(args)
print(config)

# TODO Validate video file and path
# TODO Validate nerf-type arg

# Get project workspace full path for passing into docker run
project_path = pathlib.Path(__file__).parent.resolve()
print("Project Full Path: "+str(project_path))

# Initilize nerfstudio_runner for easier execution
ns_runner = ns.runner(project_path)

# Wipe data/* directory
# TODO Validate if exists or create
ns_runner.cleanup('data')

# Copy video file to /workspace/data directory
print('Video relative path: '+args.video)
video_filename = os.path.basename(args.video)
video_data_path = os.path.join(project_path, "data", video_filename)
print('Video new path: '+video_data_path)
shutil.copy2(args.video,video_data_path)
# NOTE Video file will be assumed in /data/ directory for next step 

# Execute nerfstudio process to convert for nerf training
ns_runner.video_process(video_filename)

# Execute nerfstudio process to train nerf model
# TODO Test adjustable nerf-type arg
ns_runner.train(args.nerf_type)

print('Problem 1 script execution complete.')

# TODO __main__ function