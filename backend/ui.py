import pygame
from backend.colors import *

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
    
    def render(self, screen, font, selected=False):
        # Draw Button
        mouse_pos = pygame.mouse.get_pos()
        if selected:
            current_color = ARCANE_PURPLE
        elif self.rect.collidepoint(mouse_pos):
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
    def __init__(self, x, y, width, height, body, title, border):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.body = body
        self.title = title
        self.border = border
  
    def render(self, screen):
        pass

    def handle_click(self, pos):
        pass