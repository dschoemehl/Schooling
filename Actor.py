import math

class Actor():

    def __init__(self,x,y,movespeed):
        self.position = [x,y]
        self.destination = [0,0]
        self.movevector = [0,0]
        self.movespeed = movespeed

    def set_destination(self,x,y):
        self.destination = [x,y]

        dx = self.destination[0] - self.position[0]
        dy = self.destination[1] - self.position[1]
        #print 'dx:' + str(dx) + ', dy:' + str(dy)
        length = math.sqrt(dx*dx + dy*dy)
        #print str(length)

        self.movevector[0] = dx/length
        self.movevector[1] = dy/length

        #print 'movevector[0]:' +str(self.movevector[0]) + 'movevector[1]:' +str(self.movevector[1])

    def update_position(self):
        for pos in range( len(self.position) ):
                  if (abs(self.position[0] - self.destination[0]) > 1) or (abs(self.position[1] - self.destination[1]) > 1):
                      self.position[pos] += self.movespeed*self.movevector[pos]




