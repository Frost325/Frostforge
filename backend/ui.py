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
            for button in self.buttons:
                if button.is_clicked(mouse_pos):
                    self.selected = button.text
            # close the menu - even if one of the options wasn't clicked, means click was elsewhere
            self.open = False

            # MAYBE CHECK HERE TO PREVENT THINGS UNDERNEATH FROM BEING CLICKED???
        return self.selected


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

    def handle_key(self, event):
        pass

class Textbox:
    def __init__(self, x, y, width, height, color, typing_color, text="", text_color=BLACK, size_limit=None, num_only=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.typing_color = typing_color
        self.text = text
        self.text_color = text_color
        self.size_limit = size_limit
        self.num_only = num_only
        self.active = False
    
    def render(self, screen, font):
        if self.active:
            pygame.draw.rect(screen, self.typing_color, self.rect)
            text = self.text + "_"
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            text = self.text
        pygame.draw.rect(screen, BLACK, self.rect, min(self.width, self.height) // 20) # outline
        text_surface = font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center) # ADD OPTIONS HERE FOR LEFT OR CENTERED
        screen.blit(text_surface, text_rect)
        # ADD FOCUS LINE???

    def is_clicked(self, pos):
        if self.rect.collidepoint(pos):
            self.active = True
        else:
            if self.active:
                self.active = False
                return True
        return False
    
    def key_pressed(self, event):
        if self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.active = False
                return True
            elif self.num_only and not event.unicode.isdigit(): # alpha character for numbers only, ignore it
                pass
            else:
                if not self.size_limit or len(self.text) < self.size_limit:
                    self.text += event.unicode
        return False