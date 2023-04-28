# a Nerf Video Pipeline
Takes in video, calculates a NeRF using nerfstudio, and generates novel view videos.

### Files Included (TODO)
- setup.sh : shell script for setup and to pull/build Docker image
- launch_docker.sh : shell script to launch Docker with custom path mount
- Problem_1.py : Python script to train NeRF from video, producing 3d model
- Problem_2.py : Python script to run NeRF to generate novel view video
- Problem_3.py : TODO Whole lotta something
- Run_All_Notebook.ipynb : Jupyter notebook to optionally run problems

### Problem 1 
`train_nerf(input_video, nerf_type) → nerfacto_model`
    `get_video_metadata(input_video) → motion_path, camera_intrinsics?`
        `get_skydio_motion(input_video) → motion_path`
    `infer_video(motion_path, nerfacto_model, video_type=”rgb”) → rgb_video`
    `calc_3d_model(nerfacto_model) → 3d_mesh`
### Problem 2
`infer_new_videos(motion_path, nerfacto_model)`
    `infer_video(novel_motion_path, nerfacto_model, video_type=”both”) → rgb_video, depth_video`

### Setup Instructions:
#### Install CUDA 11.8
https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html
https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_local 
#### Install Docker Desktop (not Docker Engine)
https://docs.docker.com/desktop/install/ubuntu/
#### Instal NeRF Studio
https://docs.nerf.studio/en/latest/quickstart/installation.html#use-docker-image 

`docker pull dromni/nerfstudio:0.2.1`


### Tested System Configuration:
- Nvidia Hardware + Drivers
    - GeForce RTX 2060
    - CUDA Compute Capability: 7.5 
    - CUDA arch: 75
    - NVIDIA Drivers: 530.30.02
    - CUDA: 11.8.0-520.61.05-1
    - GCC: 9.4.0
- OS:
    - Linux 20.04 LTS
    - Kernal: 5.15.0-69-generic
- Docker
    - Docker Compose: v2.17.3
    - Docker: 23.0.5, build bc4487a
    - Docker Desktop: 4.19.0 (106363)
    - Docker Engine: 23.0.5

### Sources Cited:
https://stackoverflow.com/questions/44862100/need-to-run-docker-run-command-inside-python-script
