"""
Final Project: Missile Command (Wizard's Fire)
Author: Sean
Credit: Tutorials
Assignment: Create an old-school Missile Command Game
"""

from ggame import App, RectangleAsset, CircleAsset, Sprite, LineStyle, Color
import math
import random

class MissileTail(Sprite):
    # Create asset
    black = Color(0,1)
    noline = LineStyle(0,black)
    rect = RectangleAsset(1, 1, noline, black)
    
    def __init__(self, position):
        super().__init__(MissileTail.rect, position)
        self.age = 0
        #self.maxage = maxage
        
    def step(self):
        self.age +=1
        
class MissileHead(Sprite):
    # Create asset
    black = Color(0,1)
    red = Color(0xff0000, 1.0)
    noline = LineStyle(0,black)
    #rect = RectangleAsset(2, 2, noline, black)
    circ = CircleAsset(2, noline, red)
    
    def __init__(self, gamewidth, speed):
        super().__init__(MissileHead.circ, (-20,-20))
        self.speed = speed
        self.x = random.randint(0, gamewidth)
        self.y = 0
        self.fxcenter = self.fycenter = 0.25
        self.rotation = random.randint(180, 360) * math.pi / 180
        self.vy = -self.speed * math.sin(self.rotation)
        self.vx = self.speed * math.cos(self.rotation)
        self.length = 1
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        MissileTail((self.x, self.y))
        
class MissileCommandGame(App):
    def __init__(self):
        super().__init__()
        self.count = 1
        MissileHead(self.width, self.count)
        
    def step(self):
        for head in self.getSpritesbyClass(MissileHead):
            head.step()
            if head.x < 0 or head.x > self.width or head.y > self.height:
                head.destroy()
                print("Destroy")
            
        for tail in self.getSpritesbyClass(MissileTail):
            tail.step()
            if tail.age > 100:
                tail.destroy()
                
myapp = MissileCommandGame()
myapp.run()