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
        pygame.draw.rect(screen, BLACK, self.rect, min(self.width, self.height) // 20) # outline
        
        # Draw Text
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

class Dropdown:
    def __init__(self, x, y, width, height, color, hover_color, options, selected=None, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.options = options
        self.selected = selected
        self.text_color = text_color
        self.open = False
        self.buttons = []
        button_y = y + height
        for option in options:
            button = Button(x, button_y, width, height, option, color, hover_color)
            self.buttons.append(button)
            button_y += height
    
    def render(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, min(self.width, self.height) // 20) # outline

        # Draw Text
        if self.selected:
            text = self.selected + " v"
        else:
            text = " v"
        text_surface = font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        # draw dropdown if open
        if self.open:
            for button in self.buttons:
                button.render(screen, font)

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            # if the dropdown itself is clicked open/close the options menu
            self.open = not self.open
        elif self.open:
            # if the options menu is open check if one is clicked
            if True:
                pass
            # close the menu - even if one of the options wasn't clicked, means click was elsewhere
            self.open = False

            # MAYBE CHECK HERE TO PREVENT THINGS UNDERNEATH FROM BEING CLICKED???


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