# Runs the NerfStudio Docker image. 
# Takes in 1 argument: 
# 1st arg: The full path to the project directory
#!/bin/bash
echo "Full path to project workspace: $1"
USER_NAME=$(whoami)
sudo docker run --gpus all \
-v $1:/workspace/ \
-v /home/$USER_NAME/.cache/:/home/user/.cache/ \
-p 7007:7007 \
--rm \
-it \
--shm-size=12gb \
dromni/nerfstudio:0.2.1