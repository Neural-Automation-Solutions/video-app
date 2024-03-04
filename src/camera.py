import os
import sys
import time
from enum import Enum
from datetime import datetime

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

class CameraAction (Enum):
    IDLE = 0
    RECORDING = 1
    PREVIEW = 2

class Camera (Picamera2):
    '''
    A wrapper class to control the camera.
    '''

    def __init__ (
            self,
            save_dir: str,
            ) -> None:
        '''
        Configure camera for video 
        '''
        super().__init__()

        self.save_dir = save_dir
        self.action = CameraAction.IDLE
        self._encoder = H264Encoder(10000000)

    def start_recording (self) -> None:
        if self.action == CameraAction.RECORDING:
            raise 'Already Recording'
        if self.action == CameraAction.PREVIEW:
            print('in here!')
            self.stop_preview()
        
        self.action = CameraAction.RECORDING

        config = self.create_video_configuration()
        self.configure(config)

        filename = str(datetime.now())[:-10].replace(' ', '_')
        path = os.path.join(
                self.save_dir,
                f'{filename}.mp4'
                )
        output = FfmpegOutput(path, audio=False)
        super().start_recording(self._encoder, output)

    def stop_recording (self) -> None:
        self.action = CameraAction.IDLE
        super().stop_recording()

    def _start_preview (self) -> None:
        if self.action == CameraAction.PREVIEW:
            raise 'Already in Preview Mode'
        if self.action == CameraAction.RECORDING:
            self.stop_recording()

        self.action = CameraAction.PREVIEW

        config = self.create_preview_configuration()
        self.configure(config)

        super().start_preview(Preview.QT)
        self.start()

    def stop_preview (self) -> None:
        self.action = CameraAction.IDLE
        super().stop_preview()
        self.stop()


if __name__ == '__main__':
    cam = Camera('.')
    cam._start_preview()
    time.sleep(5)
    #cam.stop_preview()
    cam.start_recording()
    time.sleep(5)
    cam.stop_recording()
