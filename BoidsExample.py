__author__ = 'david.schoemehl'

from turtle import Turtle, Screen, Vec2D
import random
from math import cos, radians, sqrt, pow, fmod

class Schooler(Turtle):
    swarm = []

    def __init__(self):
        Turtle.__init__(self)
        self.up()
        self.setheading(random.randrange(360))
        self.setpos(random.randrange(-200,200),random.randrange(-200,200))
        #self.down()
        self.newHead = None
        self.velocity = Vec2D(0,0)
        self.neighbordist = 50
        self.neighbors = []
        Schooler.swarm.append(self)

    def moveAllBoidsToNewPositions(self):
        v1 = Vec2D(0,0)
        v2 = Vec2D(0,0)
        v3 = Vec2D(0,0)
        v4 = Vec2D(0,0)
        windV = Vec2D(0,0)

        del self.neighbors[:]
        self.findNieghbors()

        v1 = self.rule1()
        v2 = self.rule2()
        v3 = self.rule3()
        v4 = self.bound_position()

        #limit the max velocity
        vlimit = 2


        self.velocity = self.velocity + v1 + v2 + v3 + v4 + windV

        if (self.mag(self.velocity) > vlimit):
            self.velocity = self.unit(self.velocity) * vlimit

        #self.color( self.pos()[0]%255,0,0)
        self.setheading(self.towards(self.pos() + self.velocity))
        self.setpos(self.pos() + self.velocity)

    def findNieghbors(self):
        for other in Schooler.swarm:
            if self != other:
                if abs(self.pos() - other.pos()) < self.neighbordist:
                    self.neighbors.append(other)
        print len(self.neighbors)

    def rule1(self):
        percievedCenter = Vec2D(0,0)
        print len(self.neighbors)
        if(len(self.neighbors)):
            for other in self.neighbors:
                if self != other:
                    percievedCenter += other.pos()
            percievedCenter = Vec2D(percievedCenter[0]/(int(len(self.neighbors))), percievedCenter[1]/(int(len(self.neighbors))))
            percievedCenter = (percievedCenter - self.pos())
        return percievedCenter * .01

    def rule2(self):
        repulsionVector = Vec2D(0,0)
        for other in self.neighbors:
            if self != other:
                if abs(self.pos() - other.pos()) < 40:
                    repulsionVector = repulsionVector - (other.pos() - self.pos())
        return repulsionVector

    def rule3(self):
        averageVelocity = Vec2D(0,0)
        for other in self.neighbors:
            if self !=other:
                averageVelocity = averageVelocity + other.velocity

        averageVelocity = averageVelocity *(1/(len(Schooler.swarm) - 1))
        return averageVelocity

    def bound_position(self):
        xmin = -600
        xmax = 600
        ymin = -600
        ymax = 600
        xadj = 0
        yadj = 0

        if self.pos()[0] < xmin:
            xadj = 10
        if self.pos()[0] > xmax:
            xadj = -10
        if self.pos()[1] < ymin:
            yadj = 10
        if self.pos()[1] > ymax:
            yadj = -10

        #print xadj, yadj
        return Vec2D(xadj,yadj)

    def mag(self,vec):
        return sqrt( pow( vec[0],2) + pow(vec[1],2) )

    def unit(self,vec):
        magnitude = self.mag(vec)
        return Vec2D(vec[0]/magnitude, vec[1]/magnitude)

def main():
    swarmSize = 30
    t = Turtle()
    win = Screen()
    win.setworldcoordinates(-600,-600,600,600)
    t.speed(10)
    t.tracer(15)
    t.hideturtle()

    for i in range(swarmSize):
        Schooler()

    #for turn in range(1000):
    while True:
        try:
            for schooler in Schooler.swarm:
                schooler.moveAllBoidsToNewPositions()
        except KeyboardInterrupt:
            break

    win.exitonclick()

main()

