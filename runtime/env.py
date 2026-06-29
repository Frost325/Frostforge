import copy
import json

class FrostForgeEnv:
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.data = json.load(file)

        # static data
        self.initial_grid = self.data["grid"]
        self.templates = self.data["templates"]
        
        # settings
        self.settings = self.data["settings"]
        self.width = self.settings["width"]
        self.height = self.settings["height"]
        self.background_color = self.settings["background_color"]
        self.line_color = self.settings["line_color"]
        self.show_lines = self.settings["show_lines"]

        # runtime state
        self.grid = []
        self.steps = 0

        # call setup
        self.reset()

    def reset(self):
        self.grid = copy.deepcopy(self.initial_grid)
        self.steps = 0

        return self.grid, {} # observation, info -- replace grid with whatever observation is

    def step(self, action):
        raise NotImplementedError
        # return, observation, reward, terminated, truncated, info

    def render(self):
        raise NotImplementedError
    
    def close(self): # what to do here?
        raise NotImplementedError