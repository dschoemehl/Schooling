from Actor import Actor
from turtle import Vec2D
from math import cos, radians, sqrt, pow, fmod

class SchoolingActor(Actor):
    swarm = []

    def __init__(self,x,y,movespeed):

        Actor.__init__(self, x, y, movespeed)

        #self.up()
        #self.setheading(random.randrange(360))
        # self.down()
        self.newHead = None
        self.velocity = Vec2D(0, 0)
        self.vlimit = 2
        self.repulsionforce = 2
        self.minNieghborDist = 100
        self.neighbordist = 1000
        self.neighbors = []
        SchoolingActor.swarm.append(self)

    def moveAllBoidsToNewPositions(self):
        v1 = Vec2D(0, 0)
        v2 = Vec2D(0, 0)
        v3 = Vec2D(0, 0)
        v4 = Vec2D(0, 0)
        windV = Vec2D(0, 0)

        del self.neighbors[:]
        self.findNieghbors()

        v1 = self.rule1()
        #print 'v1 = ' + str(v1)
        v2 = self.rule2() * self.repulsionforce
        #v3 = self.rule3()
        #v4 = self.bound_position()

        self.velocity = self.velocity + v1 + v2 + v3 + v4 + windV

        if (self.mag(self.velocity) > self.vlimit):
            self.velocity = self.unit(self.velocity) * self.vlimit

        # self.color((int(self.pos()[0]%254),0,0), (int(self.pos()[0]%254),0,0))

        # self.color( (10, 0, 0), (10, 0, 0))
        #self.setheading(self.towards(self.pos() + self.velocity))
        #self.setpos(self.pos() + self.velocity)
        self.set_destination(self.position + self.velocity)

    def findNieghbors(self):
        for other in SchoolingActor.swarm:
            if self != other:
                if abs(self.position - other.position) < self.neighbordist:
                    self.neighbors.append(other)
        #print len(self.neighbors)

    def rule1(self):
        percievedCenter = Vec2D(0, 0)
        #print len(self.neighbors)
        if (len(self.neighbors)):
            for other in self.neighbors:
                if self != other:
                    percievedCenter += other.position
            percievedCenter = Vec2D(percievedCenter[0] / (int(len(self.neighbors))),
                                    percievedCenter[1] / (int(len(self.neighbors))))
            percievedCenter = (percievedCenter - self.position)
        return percievedCenter


    def rule2(self):
        repulsionVector = Vec2D(0, 0)
        for other in self.neighbors:
            if self != other:
                if abs(self.position - other.position) < self.minNieghborDist:
                    repulsionVector = -(other.position - self.position)
        return repulsionVector