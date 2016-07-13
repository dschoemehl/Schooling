from math import cos, radians, sqrt, pow, fmod, acos, degrees
from turtle import Vec2D

class Actor():

    def __init__(self,x,y,movespeed):
        self.position = Vec2D(x,y)
        self.destination = Vec2D(0,0)
        self.movevector = Vec2D(0,0)
        self.movespeed = movespeed
        self.heading = 0.0

    def set_destination(self,dest):
        change = self.destination - self.position
        #print change
        self.destination = dest

        self.movevector = self.unit(change)

        #set heading
        dotprod = self.dot(Vec2D(0,1), self.movevector)
        self.heading = degrees(acos(dotprod))
        if(self.movevector[0] < 0):
            self.heading = -self.heading
        #print self.heading

        #print 'movevector[0]:' +str(self.movevector[0]) + 'movevector[1]:' +str(self.movevector[1])

    def update_position(self):
        for pos in range( len(self.position) ):
                  #if (abs(self.position[0] - self.destination[0]) > 1) or (abs(self.position[1] - self.destination[1]) > 1):
                      self.position += self.movespeed*self.movevector

    def mag(self, vec):
        return sqrt(pow(vec[0], 2) + pow(vec[1], 2))

    def unit(self, vec):
        magnitude = self.mag(vec)
        if (magnitude == 0):
            return 0
        else:
            return Vec2D(vec[0] / magnitude, vec[1] / magnitude)

    def dot(self, vec1, vec2):
        return (vec1[0]*vec2[0]) + (vec1[1]*vec2[1])
