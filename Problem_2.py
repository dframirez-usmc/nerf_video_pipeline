#!/usr/bin/python
"""
DOCSTRING
"""

import argparse
import pathlib
import nerfstudio_runner as ns

# Parse python args at runtime
parser = argparse.ArgumentParser(description="Create a video render from a NeRF and a motion path.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('config_yml', help="Relative path to config.yml NeRF model")
parser.add_argument('-m', '--motion',
                    default="camera_path.json", 
                    help="Camera motion file location")
#parser.add_argument('model', help="NeRFacto model file location")
args = parser.parse_args()
config = vars(args)
print(config)

# TODO Validate config.yml file and path
# TODO Validate motion file

# Get project workspace full path for passing into docker run
project_path = pathlib.Path(__file__).parent.resolve()
print("Project Full Path: "+str(project_path))

# Initilize nerfstudio_runner for easier execution
ns_runner = ns.runner(project_path)

# Wipe render/* directory
# TODO Validate if exists or create
ns_runner.cleanup('renders')

# Execute nerfstudio process to render new video
# TODO Test adjustable nerf-type arg
ns_runner.render(args.config_yml, args.motion)

print('Problem 2 script execution complete.')

# TODO __main__ function
