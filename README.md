# Frostforge

A visual Reinforcement Learning Environment Builder and RL Sandbox.

Frostforge allows users to create custom grid-based environments through an intuitive visual editor. Rather than manually programming environments from scratch, users can define reusable templates, place them within a grid world, and eventually export and train reinforcement learning agents directly within the platform.

The long-term vision is to create a bridge between environment design and reinforcement learning experimentation, providing a workflow similar to a game editor but focused on RL research, education, and rapid prototyping.

---

## Features (v0.2)

### Environment Editor

* Grid-based environment creation
* Cell selection and inspection
* Template placement
* Template deletion

### Template System

* Create new templates
* Rename templates
* Select active placement template
* Edit template properties
* Reusable template architecture

### Template Properties

Currently supported:

* Name
* Shape

  * Rectangle
  * Circle
* Color (RGB)
* Size

Planned:

* Images
* Collision settings
* Reward values
* Agent flags
* Goal flags
* Custom metadata

### Save & Load

* Save environments to disk
* Load saved environments
* Persist templates and grid layouts
* Restore selected template and editor state

### Custom UI Framework

Frostforge currently includes custom-built:

* Buttons
* Dropdown menus
* Textboxes
* Page system

---

## Screenshots

*Screenshots coming soon.*

---

## Project Structure

```text
Frostforge/
│
├── main.py
│
├── backend/
│   ├── colors.py
│   ├── objects.py
│   ├── ui.py
│   └── save.py
│
├── pages/
│   ├── templatepage.py
│   └── settingspage.py
│
```

---

## Running Frostforge

### Requirements

* Python 3.10+
* Pygame 2.6.1

### Installation

```bash
git clone <repository-url>
cd Frostforge

pip install pygame
```

### Launch

```bash
python main.py
```

---

## Current Workflow

1. Create or select a template.
2. Modify template properties.
3. Select a cell in the environment grid.
4. Place or delete objects.
5. Save the environment.
6. Load environments for future editing.

---

## Vision

Frostforge originally began as a game engine project before evolving into a dedicated RL environment builder.

The goal is to provide a visual workflow for creating environments, defining behaviors, exporting environments, and training reinforcement learning agents without requiring users to build every component from scratch.

By combining environment design tools with reinforcement learning workflows, Frostforge aims to become a sandbox for experimentation, education, and rapid RL prototyping.

---

## Current Status

Frostforge is currently in active development.

Version **0.2** focuses on establishing the core editor experience, including environment creation, template management, and save/load functionality.

Future development will expand toward environment logic, export systems, simulation tools, and integrated reinforcement learning workflows.
