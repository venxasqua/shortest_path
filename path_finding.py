import numpy as np
from PyQt5.QtGui import QImage
from algo1 import Djaktra1

class My_Image:
    def __init__(self,height,width) -> None:
        self.picture=np.zeros((height,width,3),dtype="uint8")
        self.picture[:,:,:]=255
        """draw field
            30 is the size of each rectangle """
        for i in range(1,32):
            self.picture[i*30-1:i*30+1,:,:]=[255,0,0]
            self.picture[:,i*30-1:i*30+1,:]=[255,0,0]
        """draw start and end point so later we can remove this
            if we want to select the start and end point"""
        self.set_start_end((0,0),(950,950))
        self.cv2_image_to_qt()
        self.wall = {}



    def cv2_image_to_qt(self):
        """convert numpy array in Image for pyqt window"""
        self.image=QImage(self.picture.data,
                            self.picture.shape[1],
                            self.picture.shape[0],
                            self.picture.shape[1]*self.picture.shape[2],
                            QImage.Format_BGR888)

    def draw_wall(self,height,width):
        """ drawing wall on the label"""
        """ each rectangle on the label has 30x30 pixel size (notr that we do not count the pixel of the blue lines)"""
        y=int(height/30)
        x=int(width/30)
        if not (x==0 and y==0) and not (x==31 and y==31):
            self.wall[(y,x)] = True
            self.picture[30*y:30*y+30,30*x:30*x+30]=np.array([0,0,0])
            self.cv2_image_to_qt()

    def set_start_end(self,start,end):
        """drawing start and end point"""
        self.start_y = int(start[1]/30)
        self.start_x = int(start[0]/30)
        self.start = self.start_y, self.start_x
        self.end_y = int(end[1]/30)
        self.end_x = int(end[0]/30)
        self.end = self.end_y, self.end_x
        self.picture[30*self.start_y:30*self.start_y+30,
                    30*self.start_x:30*self.start_x+30]=np.array([0,0,255])
        self.picture[30*self.end_y:30*self.end_y+30,
                    30*self.end_x:30*self.end_x+30]=np.array([0,255,255])
    

class Choice_of_Algorithm:
    def __init__(self,frame,choice=0) -> None:
        """ we note that we can get the start and end point from self.frame 
            I will fix this """
        self.frame : My_Image = frame
        self.choice = choice

    def start_algorithm(self):
        my_soloution = Djaktra1(self.frame)
        my_soloution.run()
        my_soloution.draw_shortest_path()