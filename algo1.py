
from queue import Queue
from knot import Knot
import path_finding
class Djaktra1:
    """ The first algorithm"""
    def __init__(self,frame):
        """ We used dictionary for visited point and currently working point
            so i need only constant time to check the status of the neighborhood.
            Further more we also need a list ( you can also use queue) to add the neighbor """
        self.frame : path_finding.My_Image = frame
        self.start : tuple = Knot(self.frame.start)
        self.end : tuple = Knot(self.frame.end)
        self.working_point_list = []
        self.working_point_dict = {}
        self.path = []
    def run(self):
        """First set we mark the start at working point"""
        self.working_point_dict[self.start]=True
        self.working_point_list.append(self.start)
        while (self.working_point_list!=[] or not self.working_point_dict.get(self.end)):
            """ Take the first element in list and look for the neighborhood"""
            current_knot=self.working_point_list.pop(0)
            x,y = current_knot.point
            for i in range(2):
                self._next_point_for_neighborhood(x+(-1)**i,y,current_knot)

            for j in range(2):
                self._next_point_for_neighborhood(x,y+(-1)**j,current_knot)


    def _next_point_for_neighborhood(self,x,y,current_knot):
        """ check the neighborhood
            did we visited the neighborhood or not or is it on the field"""
        if y<0 or x<0 or y>31 or x>31:
            """ the field is a 31x31 matrix!"""
            return 
        if (self.working_point_dict.get(Knot((x,y))) or
                    self.frame.wall.get((x,y))):
            return 
        """ if the neighborhood is free we add this"""
        knot = Knot((x,y),current_knot)
        self.working_point_list.append(knot)
        self.working_point_dict[knot]=True
        """ this is for drawing"""
        if self.end != knot:
            self.frame.picture[x*30+1:x*30+29,y*30+1:y*30+29]=(125,125,125)
        if self.end==knot:
            self.end=knot

    def draw_shortest_path(self):
        """ backtracking to find the shortest path"""
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




















