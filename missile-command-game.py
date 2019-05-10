"""
Final Project: Missile Command (Wizard's Fire)
Author: Sean
Credit: Tutorials
Assignment: Create an old-school Missile Command Game
"""

from ggame import App, RectangleAsset, CircleAsset, LineAsset, Sprite, LineStyle, Color
import math
import random

class Turret(Sprite):
    black = Color(0, 1)
    noline = LineStyle(0, black)
    rect = RectangleAsset(5, 40, noline, black)
    
    def __init__(self, width, height):
        self.gamewidth = width
        self.gameheight = height
        self.vr = 0
        self.maxspin = 0.1
        self.fxcenter = 0.5
        self.fycenter = 0
        super().__init__(Turret.rect, (self.gamewidth / 2, self.gameheight - 50))
        
        # Rotate right/left
        MissileCommandGame.listenKeyEvent("keydown", "left arrow", self.aimLeftOn)
        MissileCommandGame.listenKeyEvent("keyup", "left arrow", self.aimLeftOff)
        MissileCommandGame.listenKeyEvent("keydown", "right arrow", self.aimRightOn)
        MissileCommandGame.listenKeyEvent("keyup", "right arrow", self.aimRightOff)
        
    def aimRightOn(self, event):
        self.vr = self.maxspin
            
    def aimRightOff(self, event):
        self.vr = 0
        
    def aimLeftOn(self, event):
        self.vr = -self.maxspin
            
    def aimLeftOff(self, event):
        self.vr = 0
        
    def step(self):
        self.rotation += self.vr

class MissileTail(Sprite):
    # Create asset
    black = Color(0, 1)
    blackline = LineStyle(1,black)
    
    def __init__(self, position, vx, vy):
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
    circ = CircleAsset(3, noline, red)
    
    def __init__(self, width, height, speed):
        super().__init__(MissileHead.circ, (random.randint(0, width), 0))
        self.speed = speed
        self.gamewidth = width
        self.gameheight = height
        self.fxcenter = self.fycenter = 0.5
        
        # Randomly generate an angle that will direct missile to the ground (not off the screen)
        self.theta1 = math.atan2(self.gameheight, self.x)
        self.theta2 = math.pi - math.atan2(self.gameheight, self.gamewidth - self.x)
        self.random = random.random(0,1) * (self.theta2 - self.theta1) + self.theta1
        
        # Give missile x-speed and y-speed
        self.vy = self.speed * math.sin(self.random)
        self.vx = self.speed * math.cos(self.random - math.pi)
        
        # Create missile tail
        self.tail = MissileTail((self.x, self.y), self.vx, self.vy)
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
class MissileCommandGame(App):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.speed = 1
        self.frequency = 300
        
        self.turret = Turret(self.width, self.height)
        
    def step(self):
        # Creates missiles that gradually move faster and gradually come more frequently
        if self.count % self.frequency == 0:
            MissileHead(self.width, self.height, self.count / 5000 + 1)
        self.count += 1
        if self.count % 250 == 0 and self.frequency > 0:
            self.frequency -= 10
            
        self.turret.step()
        
        # Destroy MissileHead and MissileTail after they go off of screen
        for head in self.getSpritesbyClass(MissileHead):
            head.step()
            if head.x < -100 or head.x > self.width + 100 or head.y > self.height + 100:
                head.tail.destroy()
                head.destroy()
                
        for tail in self.getSpritesbyClass(MissileTail):
            tail.step()
                
myapp = MissileCommandGame()
myapp.run()
