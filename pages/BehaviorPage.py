import pygame
from backend.ui import Button, Dropdown, Page, Textbox, Cycle
from backend.objects import Template
from backend.colors import *

class BehaviorPage(Page):
    def __init__(self, x, y, width, height, body, title, border, templates):
        super().__init__(x, y, width, height, body, title, border)
    
        self.button_width = width * 7 // 24
        self.button_height = width // 18
        self.vertical_gap = border // 2

        # AGENT
        self.agent_title = title.render("Agent", True, FROST_BLUE)
        self.agent_template = body.render("Template:", True, FROST_BLUE)
        self.agent_dropdown = Dropdown(x + 3 * border + self.agent_template.get_width(), y + border + self.agent_title.get_height() + self.vertical_gap, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, templates.keys())
        self.action_space = body.render("Action Space:", True, FROST_BLUE)
        self.action_cycle = Cycle(x + 3 * border + self.action_space.get_width(), self.agent_dropdown.rect.bottom + self.vertical_gap, self.button_width, self.button_height, ICE_BLUE, FROST_BLUE, ["Orthogonal", "Omnidirectional"])
        self.allow_stay = body.render("Allow Stay", True, FROST_BLUE )
        self.stay_checkbox = Button(x + 2 * border, self.action_cycle.rect.bottom + self.vertical_gap, self.button_height, self.button_height, "X", ICE_BLUE, FROST_BLUE)
        self.agent_underline = pygame.Rect(x + border, self.stay_checkbox.rect.bottom + border, width - 2 * border, border // 10)


    def render(self, screen):
        super().render(screen)

        # AGENT
        screen.blit(self.agent_title, (self.x + self.border, self.y + self.border))
        self.agent_dropdown.render(screen, self.body)
        screen.blit(self.agent_template, (self.x + 2 * self.border, self.agent_dropdown.rect.centery - self.agent_template.get_height() // 2))
        self.action_cycle.render(screen, self.body)
        screen.blit(self.action_space, (self.x + 2 * self.border, self.action_cycle.rect.centery - self.action_space.get_height() // 2))
        self.stay_checkbox.render(screen, self.body)
        screen.blit(self.allow_stay, (self.stay_checkbox.rect.right + self.border, self.stay_checkbox.rect.centery - self.allow_stay.get_height() // 2))
        pygame.draw.rect(screen, PURPLE, self.agent_underline)
    
    def handle_click(self, pos):
        return super().handle_click(pos)
    
    def handle_key(self, event):
        return super().handle_key(event)



# THIS PAGE IS WHERE THE BEHAVIOR OF TEMPLATES AND THE AGENT WILL BE DEFINED


# Agent Section: Agent Dropdown, Action Space (4, 8 - orthogonal/omindirectional), Stay (Togglable)

# Movement Table: Template List, Behavior List: Buttons cycle on click (static, random, towards, away), cyclable orthogonal/omindirectional

# Interactions: Coming Soon