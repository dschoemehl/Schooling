import pyglet
import random
from pyglet import window
from SpriteRender import SpriteRender
from Actor import Actor
import datetime

def center_anchor(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

circle = pyglet.image.load('assets\circle.png')
center_anchor(circle)
triangle = pyglet.image.load('assets\/triangle.png')
center_anchor(triangle)
square = pyglet.image.load('assets\square.png')
center_anchor(square)




#Responsible for handling mouse input and setting destinations on the tasks
# Mouse Handlers
class TaskView(window.Window):

    def __init__(self,width,height,tasks,contexts,folders,controller):
        # window.Window(self)
        super(TaskView, self).__init__(width=width,height=height)
        self.label = pyglet.text.Label('TaskViz')
        self.tasks = tasks
        self.contexts = contexts
        self.folders = folders
        self.controller = controller
        self.renderableTasks = []
        self.renderableContexts = []
        self.renderableFolders = []
        self.batch = pyglet.graphics.Batch()

        for task in self.tasks:
            #create a sprite renderable based on rules
            self.renderableTasks.append(SpriteRender(circle,self.batch,task))

            #self.renderableTasks[-1].label.text = str(self.renderableTasks[-1].actor.title[:10]) + '...'
            priority = self.renderableTasks[-1].actor.priority + 1
            spriteColor = [[255,255,255],[0,255,0],[255,242,0],[255,127,39],[255,0,0]]
            self.renderableTasks[-1].color =  spriteColor[priority][0],spriteColor[priority][1],spriteColor[priority][2]

            #pulse overdue tasks
            if task.duedate < datetime.date.today() and task.duedate != datetime.date(1969,12,31):
                #print 'pulse one'
                self.renderableTasks[-1].pulse_settings(random.randrange(1,2)/5,random.randrange(1,2),random.randrange(20,40))
                self.renderableTasks[-1].pulse = True

        for context in contexts:
           self.renderableContexts.append(SpriteRender(triangle,self.batch,context))
           self.renderableContexts[-1].label.text = str(self.renderableContexts[-1].actor.name)
           #self.renderableContexts[-1].actor.position = [random.randint(0,400),random.randint(0,400)]
           self.renderableContexts[-1].color = 255,0,0

        for folder in folders:
           self.renderableFolders.append(SpriteRender(square,self.batch,folder))
           self.renderableFolders[-1].label.text = str(self.renderableFolders[-1].actor.name)
           #self.renderableFolders[-1].actor.position = [random.randint(50,700),random.randint(50,500)]
           self.renderableFolders[-1].color = 0,255,0

    def on_mouse_press(self,x, y, button, modifiers):
        self.controller.on_mouse_press(x, y, button, modifiers)
        pass

    def on_mouse_release(self,x, y, button, modifiers):
        self.controller.on_mouse_release(x, y, button, modifiers)
        pass

    def on_mouse_drag(self,x, y, dx, dy, buttons, modifiers):
        self.controller.on_mouse_drag(x, y, dx, dy, buttons, modifiers)
        pass

    def on_draw(self):
        for task in self.renderableTasks:
            task.tick()

        for context in self.renderableContexts:
            context.tick()

        for folder in self.renderableFolders:
            folder.tick()

        self.clear()
        self.batch.draw()
        self.label.draw()