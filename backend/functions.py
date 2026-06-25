import json
from backend.objects import Template

def save(grid, templates, selected_template):
    data = {
        "grid": [], # ADD GRID SIZE LATER
        "templates": {},
        "selected_template": selected_template
    }

    # save grid
    for row in grid:
        save_row = []
        for cell in row:
            if cell:
                save_row.append(cell.name)
            else:
                save_row.append(None)
        data["grid"].append(save_row)

    # save templates
    for name, template in templates.items():
        data["templates"][name] = template.to_dict()
    
    with open("backend/save.json", "w") as file:
        json.dump(data, file, indent=4)

def load():
    with open("backend/save.json", "r") as file:
        data = json.load(file)
    
    # load templates
    templates = {}
    for name, template_data in data["templates"].items():
        templates[name] = Template.from_dict(template_data)

    # load grid
    grid = []
    for row in data["grid"]:
        grid_row = []
        for cell in row:
            if cell:
                grid_row.append(templates[cell])
            else:
                grid_row.append(None)
        grid.append(grid_row)

    return grid, templates, data["selected_template"]

def change_grid_size(grid, new_width, new_height):
    width = len(grid[0])
    height = len(grid)
    if new_width:
        new_grid = [[None for _ in range(new_width)] for _ in range(height)]
        width = min(width, new_width)
    elif new_height:
        new_grid = [[None for _ in range(width)] for _ in range(new_height)]
        height = min(height, new_height)

    # transfer templates to new grid
    for r in range(height):
        for c in range(width):
            new_grid[r][c] = grid[r][c]
    return new_grid, len(new_grid[0]), len(new_grid)