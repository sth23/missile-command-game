"""
Final Project: Missile Command (Wizard's Fire)
Author: Sean
Credit: Tutorials
Assignment: Create an old-school Missile Command Game
"""

from ggame import App, RectangleAsset, CircleAsset, LineAsset, Sprite, LineStyle, Color
import math
import random

class MissileTail(Sprite):
    # Create asset
    black = Color(0, 1)
    blackline = LineStyle(1,black)
    
    def __init__(self, position, rotation, vx, vy):
        super().__init__(LineAsset(vx * 100, vy * 100, MissileTail.blackline), position)
        self.vx = vx
        self.vy = vy
        self.fycenter = 1
        if self.vx < 0:
            self.fxcenter = 0
        elif self.vx > 0:
            self.fxcenter = 1
        else:
            self.fxcenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        
class MissileHead(Sprite):
    # Create asset
    red = Color(0xff0000, 1.0)
    noline = LineStyle(0, red)
    circ = CircleAsset(2, noline, red)
    
    def __init__(self, width, height, speed):
        super().__init__(MissileHead.circ, (random.randint(0, width), 0))
        self.speed = speed
        self.gamewidth = width
        self.gameheight = height
        self.fxcenter = self.fycenter = 0.5
        self.theta1 = (math.atan2(self.gameheight, self.x) / math.pi)
        self.theta2 = (math.pi - math.atan2(self.gameheight, self.gamewidth - self.x)) / math.pi
        self.random = random.random(0,1) * (self.theta2 - self.theta1) + self.theta1
        self.rotation = self.random * math.pi
        self.vy = self.speed * math.sin(self.rotation)
        self.vx = self.speed * math.cos(self.rotation)
        
        print(self.theta1)
        print(self.theta2)
        print(self.rotation)
        
        # Create missile tail
        self.tail = MissileTail((self.x, self.y), self.rotation, self.vx, self.vy)
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
class MissileCommandGame(App):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.speed = 1
        self.frequency = 200
        
    def step(self):
        if self.count % self.frequency == 0:
            MissileHead(self.width, self.height, self.count / 5000 + 1)
        self.count += 1
        if self.count % 250 == 0 and self.frequency > 0:
            self.frequency -= 10
        
        for head in self.getSpritesbyClass(MissileHead):
            head.step()
            if head.x < 0 or head.x > self.width or head.y > self.height:
                head.destroy()
            
        for tail in self.getSpritesbyClass(MissileTail):
            tail.step()
            if tail.x < -500 or tail.x > self.width + 500 or tail.y > self.height + 500:
                tail.destroy()
                
                # How to handle missile tail if head is destroyed...?
                
myapp = MissileCommandGame()
myapp.run()
