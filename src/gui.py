from enum import Enum
from tkinter import Tk, Button, Label, Frame, LEFT, RIGHT, TOP

class CameraStatus(Enum):
    '''
    Camera Status ENUM
    '''

    IDLE = 0
    ACTIVE = 1
    INACTIVE = 2

class GUI(Tk):
    '''
    Class to control the video app window GUI.

    :prop _title: window title

    :method stop_recording: stops camera from recording
    :method resume_recording: resumes camera recording
    '''

    _title = "Video App"
    _width = 480
    _height = 160
    _x = 0
    _y = 0

    status: CameraStatus = CameraStatus.IDLE

    def __init__ (self):
        super().__init__()

        # build gui

        self.title(self._title)

        self.frame = Frame()
        self.frame.pack(pady=20, padx=20)

        self.frame.statusLabel = Label(text=f"CAMERA STATUS: {self.status.name}")
        self.frame.statusLabel.pack(side=TOP)

        self.frame.resume = Button(text="Resume", command=self.resume_recording)
        self.frame.resume.pack(side=LEFT, padx=45)

        self.frame.stop = Button(text="Stop", command=self.stop_recording)
        self.frame.stop.pack(side=RIGHT, padx=45)

        self.wm_geometry(f"{self._width}x{self._height}+{self._x}+{self._y}")

    def stop_recording (self) -> None:
        self.status = CameraStatus.INACTIVE
        
        # stop camera from recording

        self._update_label()

    def resume_recording (self) -> None:
        self.status = CameraStatus.ACTIVE

        # resume recording on camera

        self._update_label()

    def _update_label (self) -> None:
        self.frame.statusLabel.config(text=f"CAMERA STATUS: {self.status.name}")

gui = GUI()
gui.mainloop()

