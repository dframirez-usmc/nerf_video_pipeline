#!/usr/bin/python

import docker
import getpass
import os, shutil

class nerfstudio_easy:
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
        # TODO Warn user data will be deleted
        # TODO Check dir exists
        dir_path = os.path.join(self.project_path, dir)
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
        volumes = [f'{self.project_path}:/workspace/', f'/home/{user_name}/.cache/:/home/user/.cache/']
        ports = {7007:7007}

        # Docker run command
        container = client.containers.run(image, 
                                    cmd_step, 
                                    auto_remove=True,
                                    device_requests=device_requests,
                                    ports=ports,
                                    volumes=volumes,
                                    shm_size='12g')

        # TODO stderr handling
        # TODO streaming logs HARD!

        # Print bulk logs when complete
        print(container) # On seceond thought, maybe don't...

        #input("Press Enter to continue...")