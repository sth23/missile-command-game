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
        self.fycenter = 1
        self.rotation = 0
        self.vx = vx
        self.vy = vy
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
class MissileHead(Sprite):
    # Create asset
    red = Color(0xff0000, 1.0)
    noline = LineStyle(0, red)
    circ = CircleAsset(2, noline, red)
    
    def __init__(self, width, speed):
        super().__init__(MissileHead.circ, (random.randint(0, width), 0))
        self.speed = speed
        self.fxcenter = self.fycenter = 0.5
        self.rotation = random.random(0, 1) * math.pi
        self.vy = self.speed * math.sin(self.rotation)
        self.vx = -self.speed * math.cos(self.rotation)
        
        self.tail = MissileTail((self.x, self.y), self.rotation, self.vx, self.vy)
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
class MissileCommandGame(App):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.speed = 1
        self.level = 10
        
    def step(self):
        if self.count % (self.level * 20) == 0:
            MissileHead(self.width, self.speed)
        self.count += 1
        
        
        for head in self.getSpritesbyClass(MissileHead):
            head.step()
            if head.x < 0 or head.x > self.width or head.y > self.height:
                head.destroy()
            
        for tail in self.getSpritesbyClass(MissileTail):
            tail.step()
                
myapp = MissileCommandGame()
myapp.run()
