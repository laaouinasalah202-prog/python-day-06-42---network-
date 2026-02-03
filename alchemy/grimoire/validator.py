def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = {"fire", "water", "earth", "air"}
    for i in valid_ingredients:
        if i in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
