from math import cos, radians, sqrt, pow, fmod
from turtle import Vec2D

class Actor():

    def __init__(self,x,y,movespeed):
        self.position = Vec2D(x,y)
        self.destination = Vec2D(0,0)
        self.movevector = Vec2D(0,0)
        self.movespeed = movespeed

    def set_destination(self,dest):
        change = self.destination - self.position
        #print change
        self.destination = dest

        #dx = self.destination[0] - self.position[0]
        #dy = self.destination[1] - self.position[1]

        #print 'dx:' + str(dx) + ', dy:' + str(dy)
        #length = math.sqrt(dx*dx + dy*dy)
        #length = mag(change)
        #print str(length)

       # self.movevector[0] = dx/length
       # self.movevector[1] = dy/length

        self.movevector = self.unit(change)

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