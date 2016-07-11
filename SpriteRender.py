from pyglet.sprite import Sprite
from pyglet.text import Label

class SpriteRender(Sprite):

    def __init__(self,image,batch,actor):

        super(SpriteRender, self).__init__(image, batch=batch)
        self.actor = actor
        self.set_position(self.actor.position[0],self.actor.position[1])
        self.label = Label('Fish',font_size=10,x=self.actor.position[0],y=self.actor.position[1],batch=batch,anchor_x='center',anchor_y='center')
        self.scale = .5
        self.opacity = 125
        self.min_scale = 1
        self.max_scale = 2
        self.pulse_per_sec = 10
        self.pulse_increment = 1.0/self.pulse_per_sec
        self.pulse = False
        #self.sprite.color = x,y,0


    def pulse_settings(self,min_scale,max_scale,pulse_per_sec):
        self.min_scale = min_scale
        self.max_scale = max_scale
        self.pulse_per_sec = pulse_per_sec
        self.pulse_increment = 1.0/self.pulse_per_sec
        self.scale = self.min_scale

    def tick(self):
        self.set_position(self.actor.position[0],self.actor.position[1])
        self.label.x = self.actor.position[0]
        self.label.y = self.actor.position[1]
        #self.color = self.actor.position[0],self.actor.position[1],0

        if self.pulse:
            self.scale += self.pulse_increment
            if self.scale > self.max_scale:
                self.scale = self.max_scale
                self.pulse_increment *= -1
            elif self.scale < self.min_scale:
                self.scale = self.min_scale
                self.pulse_increment *= -1


