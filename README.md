# a Nerf Video Pipeline
Takes in video, calculates a NeRF using nerfstudio, and generates novel view videos.

## Files Included
- setup.sh : shell script to test setup and to pull Docker image
- Problem_1.py : Python script to train NeRF from video
- Problem_2.py : Python script to use a NeRF to generate novel view video
- Problem_3.py : Python script to re-train a NeRF adding text instruction editing
- Run_All_Notebook.ipynb : Jupyter notebook to optionally run problems
- launch_docker.sh : convenient shell script to launch Docker with custom path mount

## Setup Instructions:
(Ubuntu 20.04 LTS)

### Install latest Nvidia Drivers
https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html#ubuntu-lts

### Install CUDA 11.8 (optional)
The CUDA runtime is baked into the Docker image and should not be required on the host machine.

https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html

https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_local 

### Install Docker Engine (NOT Docker Decktop)
Docker Desktop allows for multiple contex and launching Docker through a remote machine. These multiple context will cause errors when requiring local admin privileges (through `sudo`) to enable local GPU access.

https://docs.docker.com/desktop/install/ubuntu/

### Install Nvidia Container Runtime
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html

### Get NeRF Studio
This repo requires use of NeRF Studio through Docker image. It will not work with NeRF Studio pulled from another source.

https://docs.nerf.studio/en/latest/quickstart/installation.html#use-docker-image 

`docker pull dromni/nerfstudio:0.2.1`

## Tested System Configuration:
- Ubuntu OS:
    - Linux 20.04 LTS
    - Kernal: 5.15.0-69-generic
- Nvidia Hardware + Drivers
    - GeForce RTX 2060
    - CUDA Compute Capability: 7.5 
    - CUDA arch: 75
    - NVIDIA Drivers: 530.30.02
    - GCC: 9.4.0
    - CUDA: 11.8.0-520.61.05-1
- Docker
    - Docker: 23.0.6, build ef23cbc
    - Docker Engine: 23.0.6
    - Docker Compose: v2.17.3
