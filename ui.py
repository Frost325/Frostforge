import pygame
from colors import *

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=(0,0,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
    
    def render(self, screen, font):
        # Draw Button
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            current_color = self.hover_color
        else:
            current_color = self.color
        pygame.draw.rect(screen, current_color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, min(self.width, self.height) // 20)
        
        # Draw Text
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

class Dropdown:
    pass

class Page: # tab or page for eventual tabbed menu
    pass
