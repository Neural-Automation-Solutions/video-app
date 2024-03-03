#!/usr/bin/python3

import json

from src import Camera, GUI

if __name__ == '__main__':

    with open('config.json', 'r') as file:
        config = json.load(file)

    cam = Camera(config['save_dir'])
    gui = GUI(cam)
    gui.mainloop()
