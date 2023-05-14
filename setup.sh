# Run this Bash Shell Script after installing Nvidia and Docker requirements.
#!/bin/bash

# Ubuntu Check
echo -e "\nNOTE: Author has previously tested on:"
echo -e "Linux 20.04 LTS"
echo -e "Linux Kernel 5.15.0-69-generic"
echo -e "\nCHECK UBUNTU VERSIONS"
uname -r
uname -m && cat /etc/*release

# Nvidia/CUDA Drivers Check
echo -e "\nNOTE: Author has previously tested on:"
echo -e "NVIDIA Drivers 530.30.02"
echo -e "CUDA 11.8.0-520.61.05-1"
echo -e "GCC 9.4.0"
echo -e "\nCHECK NVIDIA VERSIONS"
cat /proc/driver/nvidia/version
gcc --version

# Docker Check
echo -e "\nNOTE: Author has previously tested on:"
echo -e "Docker 23.0.5, build bc4487a"
echo -e "Docker Engine 23.0.5"
echo -e "\nCHECK DOCKER VERSIONS"
docker --version
docker version

# Download NerfStudio Docker Image
echo -e "\nDownloading NerfStudio Docker Image..."
docker pull dromni/nerfstudio:0.2.1
