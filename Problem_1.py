#!/usr/bin/python

import argparse
import subprocess
import pathlib

parser = argparse.ArgumentParser(description="Takes 2 mandatory inputs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('video', help="Video source file location")
parser.add_argument("-t", '--nerf-type', help="Define what type of NeRF model, either THIS or THAT, default is THIS")

args = parser.parse_args()
config = vars(args)
print(config)

# TODO Validate nerf-type param

# TODO Validate video file and path

# TODO Validate video as Skydio type or nah

# Get project workspace full path for passing into docker run
project_path = pathlib.Path(__file__).parent.resolve()
print("Project Path: "+str(project_path))

# Launch NerfStudio Docker Image
with open("/tmp/output.log", "a") as output:
    subprocess.call("launch_docker.sh "+str(project_path), shell=True, stdout=output, stderr=output)
    subprocess.call('echo "RUN ALL THE THINGS"')
    # TODO 