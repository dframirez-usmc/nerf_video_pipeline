# Run this Bash Shell Script after installing Nvidia and Docker requirements.
#!/bin/bash
# Ubuntu Check
echo "Check Ubuntu Versions"
echo "Note: Previously tested on Linux 20.04 LTS"
echo "Note: Previously tested on Linux Kernel 5.15.0-69-generic"
uname -r
uname -m && cat /etc/*release
# Nvidia/CUDA Drivers Check
echo "Check CUDA Driver Versions"
echo "Note: Previously tested on NVIDIA Drivers 530.30.02"
echo "Note: Previously tested on CUDA 11.8.0-520.61.05-1"
echo "Note: Previously tested on GCC 9.4.0"
cat /proc/driver/nvidia/version
gcc --version
# Docker Desktop Launch
echo "Starting Docker Desktop..."
systemctl --user start docker-desktop
# Docker Check
echo "Check Docker Versions"
echo "Note: Previously tested on Docker 23.0.5, build bc4487a"
echo "Note: Previously tested on Docker Desktop 4.19.0 (106363)"
echo "Note: Previously tested on Docker Engine 23.0.5"
echo "Note: Previously tested on Docker Compose v2.17.3"
docker --version
docker version
docker compose version
# Download NerfStudio Docker Image
echo "Downloading NerfStudio Docker Image..."
docker pull dromni/nerfstudio:0.2.1