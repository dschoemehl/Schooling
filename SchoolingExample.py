__author__ = 'david.schoemehl'

from turtle import Turtle, Screen
import random
from math import cos, radians

class Schooler(Turtle):
    swarm = []

    def __init__(self):
        Turtle.__init__(self)
        self.up()
        self.setheading(random.randrange(360))
        self.setpos(random.randrange(-200,200),random.randrange(-200,200))
        self.down()
        self.newHead = None
        Schooler.swarm.append(self)

    def getNewHeading(self):
        minAngle = 999
        for other in Schooler.swarm:
            if self != other:
                head = self.towards(other) - self.heading()
                if cos(radians(head)) > 0:
                    if head < minAngle:
                        minAngle = head
        if minAngle == 999:
            self.newHead = self.heading()
        else:
            self.newHead = minAngle+self.heading()

    def setHeadingAndMove(self):
        self.setheading(self.newHead)
        self.newHead = None
        self.forward(10)


def main():
    swarmSize = 25
    t = Turtle()
    win = Screen()
    win.setworldcoordinates(-600,-600,600,600)
    t.speed(10)
    t.tracer(15)
    t.hideturtle()

    for i in range(swarmSize):
        Schooler()

    for turn in range(50):
        for schooler in Schooler.swarm:
            schooler.getNewHeading()

        for schooler in Schooler.swarm:
            schooler.setHeadingAndMove()

    win.exitonclick()

main()

