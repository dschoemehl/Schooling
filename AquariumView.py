import pyglet
import random
from pyglet import window
from SpriteRender import SpriteRender
from Actor import Actor
import datetime

def center_anchor(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

arrow = pyglet.image.load('assets\/arrow.png')
center_anchor(arrow)

#Responsible for handling mouse input and setting destinations on the tasks
# Mouse Handlers
class AquariumView(window.Window):

    def __init__(self,width,height,fish):
        # window.Window(self)
        super(AquariumView, self).__init__(width=width,height=height)
        self.label = pyglet.text.Label('Schooling')
        self.fish = fish
        self.renderableFish = []
        self.batch = pyglet.graphics.Batch()

        for fish in self.fish:
            #create a sprite renderable based on rules
            self.renderableFish.append(SpriteRender(arrow,self.batch,fish))

            #self.renderableTasks[-1].label.text = str(self.renderableTasks[-1].actor.title[:10]) + '...'
            priority = 1
            spriteColor = [[255,255,255],[0,255,0],[255,242,0],[255,127,39],[255,0,0]]
            self.renderableFish[-1].color =  spriteColor[priority][0],spriteColor[priority][1],spriteColor[priority][2]

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
        for fish in self.renderableFish:
            fish.tick()

        self.clear()
        self.batch.draw()
        self.label.draw()