#!/usr/bin/python

import argparse
import subprocess
import pathlib

parser = argparse.ArgumentParser(description="Takes 2 mandatory inputs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('motion', help="Camera motion file location")
parser.add_argument('model', help="NeRFacto model file location")

args = parser.parse_args()
config = vars(args)
print(config)

# TODO Validate motion file and path

# TODO Validate model file and path

# TODO Get NeRFacto model type from model file

# Get project workspace full path for passing into docker run
project_path = pathlib.Path(__file__).parent.resolve()
print("Project Path: "+str(project_path))

# Launch NerfStudio Docker Image
with open("/tmp/output.log", "a") as output:
    subprocess.call("launch_docker.sh "+str(project_path), shell=True, stdout=output, stderr=output)
    subprocess.call('echo "RUN ALL THE THINGS"')
    # TODO 