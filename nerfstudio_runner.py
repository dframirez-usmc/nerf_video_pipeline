#!/usr/bin/python

import docker
import getpass
import os, shutil

class runner:
    """
    DOCSTRING
    """

    def __init__(self, project_path):
        # TODO Typing for inputs
        self.project_path = project_path

    def cleanup(self, dir):
        """
        DOCSTRING
        """
        # TODO Typing for inputs
        # TODO Check dir exists

        # TODO Warn user data will be deleted
        input(f"Press Enter to cleanup nerfstudio {dir} directory...")
        dir_path = os.path.join(self.project_path, dir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete: {}; Reason: {}'.format(file_path, e))
        print('Cleanup complete for directory: '+str(dir))

    def run(self, cmd_step):
        """
        DOCSTRING
        """
        # TODO Typing for inputs

        # Setup Docker client with context of local computer
        client = docker.from_env()
        
        # Setup Docker run command
        image = 'dromni/nerfstudio:0.2.1'
        device_requests=[docker.types.DeviceRequest(count=-1, capabilities=[['gpu']])]
        user_name = getpass.getuser()
        volumes = [f'{self.project_path}:/workspace/', 
                   f'/home/{user_name}/.cache/:/home/user/.cache/']
        ports = {7007:7007}

        #  TODO Launch web browser with viewer

        # Docker run command
        container = client.containers.run(image, 
                                    cmd_step, 
                                    auto_remove=True,
                                    device_requests=device_requests,
                                    ports=ports,
                                    volumes=volumes,
                                    shm_size='12g')

        # Print bulk logs when complete
        #print(container) # On seceond thought, maybe don't...
        # TODO streaming logs HARD!
        # TODO stderr handling

        #input("Press Enter to continue...")

    def video_process(self, video_filename):
        """
        DOCSTRING
        """
        warn = 'WARNING: Step 1 Processing can take 30+ minutes!'
        print(warn)
        ns_command = ['ns-process-data', 'video', 
                      '--data', f'data/{video_filename}', 
                      '--output-dir', 'data']
        self.run(ns_command)
        print('STEP 1 Video Processing COMPLETE!')


    def train(self, nerf_type):
        """
        DOCSTRING
        """
        warn = 'WARNING: Step 2 Training can take 30+ minutes!'
        print(warn)
        ns_command = ['ns-train', f'{nerf_type}', 
                      '--data', 'data', 
                      '--viewer.quit-on-train-completion', 'True']
        self.run(ns_command)
        print('Step 2 NeRF Training COMPLETE!')


    def render(self, config_path, traj_path):
        """
        DOCSTRING
        """
        warn = 'WARNING: Step 3 Render can take 30+ minutes!'
        print(warn)
        ns_command = ['ns-render', 
                      '--traj', 'spiral', #'filename',
                      #'--camera-path-filename', f'{traj_path}',
                      '--load-config', f'{config_path}']
        # TODO config.yml file location looks incorrect
        self.run(ns_command)
        print('Step 3 Video Render COMPLETE!')

