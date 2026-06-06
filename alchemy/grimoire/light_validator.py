#!/usr/bin/env python3
from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()
    if any(item.lower() in lower_ingredients for item in allowed):
        return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
