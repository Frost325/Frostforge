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
    
    def move(self, rect):
        self.rect = rect
        self.x = rect.x
        self.y = rect.y
        self.width = rect.width
        self.height = rect.height

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
        self.scroll = 0
        self.button_rects = [pygame.Rect(x, y + height, width, height), pygame.Rect(x, y + 2 * height, width, height), pygame.Rect(x, y + 3 * height, width, height)]
        self.scroll_rect = pygame.Rect(x, y + height, width, 3 * height)
    
    def render(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, min(self.width, self.height) // 20) # outline

        # Draw Text
        text = self.selected if self.selected else ""
        text_surface = font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        # Dropdown Arrow
        arrow_size = self.height // 5
        cx = self.rect.right - self.height // 2
        cy = self.rect.centery
        pygame.draw.polygon(screen, self.text_color, [(cx - arrow_size, cy - arrow_size // 2), (cx + arrow_size, cy - arrow_size // 2), (cx, cy + arrow_size // 2)])

        # draw dropdown if open
        if self.open:
            if len(self.buttons) < 4:
                for button in self.buttons:
                    button.render(screen, font)
            else:
                for i, button in enumerate(self.buttons[self.scroll:self.scroll + 3]):
                    button.move(self.button_rects[i])
                    button.render(screen, font)
                arrow_size = self.height // 6
                cx = self.rect.right - self.height // 2
                if self.scroll > 0:
                    cy = self.button_rects[0].centery
                    pygame.draw.polygon(screen, self.text_color, [(cx - arrow_size, cy + arrow_size), (cx, cy - arrow_size), (cx + arrow_size, cy + arrow_size)])
                if self.scroll < len(self.buttons) - 3:
                    cy = self.button_rects[2].centery
                    pygame.draw.polygon(screen, self.text_color, [(cx - arrow_size, cy - arrow_size), (cx + arrow_size, cy - arrow_size), (cx, cy + arrow_size)])


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
        return self.selected, self.open # return open so we can prevent things underneath from being clicked
    
    def set_options(self, options):
        self.options = options
        self.buttons = []
        button_y = self.y + self.height
        for option in options:
            button = Button(self.x, button_y, self.width, self.height, option, self.color, self.hover_color)
            self.buttons.append(button)
            button_y += self.height
        self.scroll = 0

    def is_scrolled(self, mouse_pos, scroll_up):
        if self.scroll_rect.collidepoint(mouse_pos):
            if scroll_up:
                self.scroll = max(self.scroll - 1, 0)
            else:
                self.scroll = min(self.scroll + 1, len(self.buttons) - 3)

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

    def handle_click(self, mouse_pos):
        pass

    def handle_key(self, event):
        pass

    def handle_scroll(self, mouse_pos, scroll_up):
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

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
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

class Cycle():
    def __init__(self, x, y, width, height, color, hover_color, options=[None], selected=0, text_color=BLACK):
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
    
    def render(self, screen, font):
        # Draw Cycle Button
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            current_color = self.hover_color
        else:
            current_color = self.color
        pygame.draw.rect(screen, current_color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, min(self.width, self.height) // 20) # outline
        
        # Draw Text
        text_surface = font.render(self.get_selected(), True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        # Dropdown Arrow
        arrow_size = self.height // 3
        cx = self.rect.right - self.height // 2
        cy = self.rect.centery
        pygame.draw.polygon(screen, self.text_color, [(cx - arrow_size // 2, cy - arrow_size // 2), (cx + arrow_size // 2, cy), (cx - arrow_size // 2, cy + arrow_size // 2)])
    
    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.selected += 1
            if self.selected >= len(self.options):
                self.selected = 0
    
    def get_selected(self):
        return self.options[self.selected]

class Checkbox():
    def __init__(self, x, y, width, height, color, hover_color, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button = Button(x, y, width, height, "X", color, hover_color, text_color)
        self.checked = True

    def render(self, screen, font):
        self.button.render(screen, font)
    
    def is_clicked(self, mouse_pos):
        if self.button.is_clicked(mouse_pos):
            self.checked = not self.checked
            self.button.text = "X" if self.checked else ""
    
    def get_state(self):
        return self.checked
    
    def set_state(self, state):
        self.checked = state
        self.button.text = "X" if self.checked else ""