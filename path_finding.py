import numpy as np
import cv2 as cv
from PyQt5.QtGui import QImage
from algo1 import Djaktra1

class My_Image:
    def __init__(self,height,width) -> None:
        self.picture=np.zeros((height,width,3),dtype="uint8")
        self.picture[:,:,:]=255
        """draw field"""
        for i in range(1,32):
            self.picture[i*30-1:i*30+1,:,:]=[255,0,0]
            self.picture[:,i*30-1:i*30+1,:]=[255,0,0]
        """draw start and end point"""

        self.set_start_end((0,0),(950,950))
        self.cv2_image_to_qt()
        self.wall = {}



    def cv2_image_to_qt(self):
        self.image=QImage(self.picture.data,
                            self.picture.shape[1],
                            self.picture.shape[0],
                            self.picture.shape[1]*self.picture.shape[2],
                            QImage.Format_BGR888)

    def draw_wall(self,height,width):
        y=int(height/30)
        x=int(width/30)
        if not (x==0 and y==0) and not (x==31 and y==31):
            self.wall[(y,x)] = True
            self.picture[30*y:30*y+30,30*x:30*x+30]=np.array([0,0,0])
            self.cv2_image_to_qt()

    def set_start_end(self,start,end):
        self.start_y=int(start[1]/30)
        self.start_x=int(start[0]/30)
        self.end_y=int(end[1]/30)
        self.end_x=int(end[0]/30)
        self.picture[30*self.start_y:30*self.start_y+30,
                    30*self.start_x:30*self.start_x+30]=np.array([0,0,255])
        self.picture[30*self.end_y:30*self.end_y+30,
                    30*self.end_x:30*self.end_x+30]=np.array([0,255,255])
    

class Choice_of_Algorithm:
    def __init__(self,frame,start,end,choice=0) -> None:
        self.frame : np.array = frame
        self.choice = choice
        self.start = start
        self.end = end 
        self.solution = []

    def start_algorithm(self):
        my_soloution = Djaktra1(self.frame, self.start, self.end)
        my_soloution.run()
        my_soloution.draw_shortest_path()