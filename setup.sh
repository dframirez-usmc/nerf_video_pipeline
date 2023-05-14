# Run this Bash Shell Script after installing Nvidia and Docker requirements.
#!/bin/bash

# Ubuntu Check
echo "\nNOTE: Author has previously tested on:"
echo "Linux 20.04 LTS"
echo "Linux Kernel 5.15.0-69-generic"
echo "\nCHECK UBUNTU VERSIONS"
uname -r
uname -m && cat /etc/*release

# Nvidia/CUDA Drivers Check
echo "\nNOTE: Author has previously tested on:"
echo "NVIDIA Drivers 530.30.02"
echo "CUDA 11.8.0-520.61.05-1"
echo "GCC 9.4.0"
echo "\nCHECK NVIDIA VERSIONS"
cat /proc/driver/nvidia/version
gcc --version

# Docker Check
echo "\nNOTE: Author has previously tested on:"
echo "Docker 23.0.5, build bc4487a"
echo "Docker Engine 23.0.5"
echo "Docker Compose v2.17.3"
echo "\nCHECK DOCKER VERSIONS"
docker --version
docker version
docker compose version

# Download NerfStudio Docker Image
echo "\nDownloading NerfStudio Docker Image..."
docker pull dromni/nerfstudio:0.2.1
