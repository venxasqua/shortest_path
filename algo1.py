import numpy as np
from queue import Queue
from knot import Knot
#from path_finding import My_Image
from PyQt5 import QtGui
class Djaktra1:
    def __init__(self,frame,start,end):
        self.frame = frame
        self.start : tuple = Knot(start)
        self.end : tuple = Knot(end)
        self.visited = {}
        self.working_point_list = []
        self.working_point_dict = {}
        self.path = []
    def run(self):
        self.working_point_dict[self.start]=True
        self.working_point_list.append(self.start)
        while (self.working_point_list!=[] or not self.working_point_dict.get(self.end)):
            current_knot=self.working_point_list.pop(0)

            x,y = current_knot.point
            for i in range(2):
                self._next_point_for_neighborhood(x+(-1)**i,y,current_knot)

            for j in range(2):
                self._next_point_for_neighborhood(x,y+(-1)**j,current_knot)


    def _next_point_for_neighborhood(self,x,y,current_knot):
        if y<0 or x<0 or y>31 or x>31:
            return 
        if (self.working_point_dict.get(Knot((x,y))) or
                    self.visited.get(Knot((x,y))) or
                    self.frame.wall.get((x,y))):
            return 
        knot = Knot((x,y),current_knot)
        self.working_point_list.append(knot)
        self.working_point_dict[knot]=True
        if self.end != knot:
            
            self.frame.picture[x*30+1:x*30+29,y*30+1:y*30+29]=(125,125,125)
        if self.end==knot:
            self.end=knot

    def draw_shortest_path(self):
        point=self.end
        path=[]
        while point.previous:
            path.append(point.previous.point)
            point=point.previous
        for point in path:
            if point ==(0,0):
                break
            x,y = point
            self.frame.picture[x*30+1:x*30+29,y*30+1:y*30+29]=(255,125,125)




















