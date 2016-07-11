#responsible for rendering the tasks and their information

#import TaskModel
import pyglet
from AquariumController import AquariumController
from SchoolingActor import SchoolingActor
from AquariumView import AquariumView
import random
from operator import attrgetter
import datetime
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

controller = AquariumController()

swarmSize = 30

for i in range(swarmSize):
    SchoolingActor( random.randrange(0, WINDOW_WIDTH),
                    random.randrange(0, WINDOW_HEIGHT),
                    .1)

window = AquariumView(WINDOW_WIDTH, WINDOW_HEIGHT, SchoolingActor.swarm)

def update(dt):
    #print 'update fish'
    for schooler in SchoolingActor.swarm:
        schooler.moveAllBoidsToNewPositions()
        schooler.update_position()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
