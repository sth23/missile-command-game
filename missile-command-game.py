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
    black = Color(0,1)
    blackline = LineStyle(1,black)
    line = LineAsset(100, 100, blackline)
    
    def __init__(self, position, vx, vy):
        super().__init__(MissileTail.line, position)
        self.x = position[0]
        self.y = position[1]
        self.vx = vx
        self.vy = vy
        self.fycenter = 1
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
class MissileHead(Sprite):
    # Create asset
    black = Color(0,1)
    red = Color(0xff0000, 1.0)
    noline = LineStyle(0,black)
    #rect = RectangleAsset(2, 2, noline, black)
    circ = CircleAsset(2, noline, red)
    
    def __init__(self, width, speed):
        super().__init__(MissileHead.circ, (random.randint(0, width), 0))
        self.speed = speed
        self.fxcenter = self.fycenter = 0.5
        self.rotation = random.random(0, 2 * math.pi)
        self.vy = self.speed * math.sin(self.rotation)
        self.vx = -self.speed * math.cos(self.rotation)
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        #MissileTail((self.x, self.y), self.vx, self.vy)
        
class MissileCommandGame(App):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.speed = 1
        self.level = 10
        
        
    def step(self):
        if self.count % (self.level * 10) == 0:
            MissileHead(self.width, self.speed)
        self.count += 1
        
        
        for head in self.getSpritesbyClass(MissileHead):
            head.step()
            if head.x < 0 or head.x > self.width or head.y > self.height:
                head.destroy()
                print("Destroy")
            
        for tail in self.getSpritesbyClass(MissileTail):
            tail.step()
                
myapp = MissileCommandGame()
myapp.run()
