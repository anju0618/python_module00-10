# Python OOP - Garden Simulation

This repository contains a series of Python exercises focused on Object-Oriented Programming (OOP) concepts. The project simulates a garden environment to demonstrate classes, encapsulation, inheritance, and advanced class features.

## Exercises

### 1. `ft_garden_security.py`
Demonstrates basic class structure and encapsulation.
- Defines a base `Plant` class.
- Implements getters and setters to protect instance attributes (e.g., preventing negative heights and ages).

### 2. `ft_plant_types.py`
Demonstrates class inheritance and method overriding.
- Expands the garden with `Flower`, `Tree`, and `Vegetable` classes that inherit from `Plant`.
- Uses `super().__init__()` for delegation.
- Overrides the `show()` method to include specific attributes (color, trunk diameter, harvest season, and nutritional value).

### 3. `ft_garden_analytics.py`
Demonstrates advanced class mechanics, static typing, and nested classes.
- Includes a `@staticmethod` to evaluate plant age.
- Includes a `@classmethod` as a factory to generate anonymous plants.
- Implements a nested `Stats` class within `Plant` (and an inherited one in `Tree`) to internally track method calls (`grow`, `age`, `show`, `produce_shade`).
- Fully compliant with `flake8` (PEP 8) and strictly type-checked using `mypy`.

## Requirements
- Python 3.x
- `flake8` (for style checking)
- `mypy` (for static type checking)

## Usage

Run each script directly from the terminal to see the execution and outputs of the garden simulation:

```bash
python3 ft_garden_security.py
python3 ft_plant_types.py
python3 ft_garden_analytics.py
