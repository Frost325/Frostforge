import pygame
from colors import *

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

class TemplatesPage(Page):
    def __init__(self, x, y, width, height, body, title, border, templates):
        super().__init__(x, y, width, height, body, title, border)

        # left side template selection
        self.list_header = title.render(f"Templates", True, BLACK)
        self.list_gap = self.list_header.get_width() //  8
        self.template_list = pygame.Rect(x, y, self.list_header.get_width() + 2 * self.list_gap, height)
        self.header_underline = pygame.Rect(x, y + self.list_header.get_height() + self.list_gap, self.template_list.width, border // 10)
        self.right_border = pygame.Rect(x + self.template_list.width, y, border // 10, height)
        
        # template buttons
        self.templates = templates
        self.template_buttons = []
        self.button_y = self.header_underline.y + self.header_underline.height
        self.button_height = (self.header_underline.y - y) * 3 // 4
        for name in templates.keys():
            button = Button(x, self.button_y, self.template_list.width, self.button_height, name, ICE_BLUE, FROST_BLUE)
            self.template_buttons.append(button)
            self.button_y += self.button_height
    
    def render(self, screen):
        super().render(screen)

        pygame.draw.rect(screen, LESS_DARK_GRAY, self.template_list)
        screen.blit(self.list_header, (self.x + self.list_gap, self.y + self.list_gap // 2))
        pygame.draw.rect(screen, PURPLE, self.header_underline)
        pygame.draw.rect(screen, PURPLE, self.right_border)

        # template buttons
        for button in self.template_buttons:
            button.render(screen, self.body)
    
    def handle_click(self, pos):
        super().handle_click(pos)

        for button in self.template_buttons:
            if button.is_clicked(pos):
                SELECTED_TEMPLATE = button.text



        return self.templates, SELECTED_TEMPLATE