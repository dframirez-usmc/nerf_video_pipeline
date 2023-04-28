# Runs the NerfStudio Docker image. Takes in 1 argument: the full path to the project workspace directory
#!/bin/bash
echo "Path to project workspace $1"
USER_NAME=$(whoami)
docker run --gpus all \                                         # Give the container access to nvidia GPU (required).
            -v $1:/workspace/ \               # Mount a folder from the local machine into the container to be able to process them (required).
            -v /home/$USER_NAME/.cache/:/home/user/.cache/ \   # Mount cache folder to avoid re-downloading of models everytime (recommended).
            -p 7007:7007 \                                      # Map port from local machine to docker container (required to access the web interface/UI).
            --rm \                                              # Remove container after it is closed (recommended).
            -it \                                               # Start container in interactive mode.
            --shm-size=12gb \                                   # Increase memory assigned to container to avoid memory limitations, default is 64 MB (recommended).
            dromni/nerfstudio:0.2.1                             # Docker image name if you pulled from docker hub.
#            <--- OR --->
#            nerfstudio                                          # Docker image tag if you built the image from the Dockerfile by yourself using the command from above. 

# docker run --gpus all -v $1 -v /home/$YOUR_USER/.cache/:/home/user/.cache/ -p 7007:7007 --rm -it --shm-size=12gb  # Parameters.
#             dromni/nerfstudio:<tag> \                           # Docker image name
#             ns-process-data video --data /workspace/video.mp4   # Smaple command of nerfstudio.
