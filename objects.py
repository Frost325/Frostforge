import pygame
from colors import BLACK

# GameObject -- anything that renders into play -- SEEMS LIKE THIS MIGHT GET SCRAPPED OR SHELVED FOR LATER
class GameObject:
    def __init__(self, x=0, y=0, assetType=None, image=None, shape="rect", dimensions=(0,0), color=BLACK):
        self.x = x
        self.y = y
        self.assetType = assetType
        self.image = image
        self.shape = shape
        self.dimensions = dimensions
        self.color = color
    
    def render(self, screen):
        if self.assetType == None:
            return
        if self.assetType == "shape": # ADD MORE SHAPES AS NEEDED
            if self.shape == "rect":
                pygame.draw.rect(screen, self.color, (self.x, self.y, *self.dimensions))
            if self.shape == "circle":
                pygame.draw.circle(screen, self.color, (self.x, self.y), self.dimensions[0])
        
        # add here render image, or draw picture

class Template:
    def __init__(self, name="", image=None, shape="rect", size=100, color=BLACK):
        self.name = name
        self.image = image
        self.shape = shape
        self.size = size
        self.color = color