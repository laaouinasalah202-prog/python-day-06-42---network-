import alchemy.elements
from alchemy.elements import create_water
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion
from alchemy.potions import healing_potion as heal

print("\n=== Import Transmutation Mastery ===\n")
print("Method 1 - Full module import:")

''' using the import style : import package'''

print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

print("\nMethod 2 - Specific function import:")

''' using the import style : from package import func '''

print(f"create_water(): {create_water()}")

print("\nMethod 3 - Aliased import:")

''' using the import style : from package import func as f'''

print(f"heal(): {heal()}")

print("\nMethod 4 - Multiple imports:")

''' using the import style : from package import func1, func2 '''

print(f"create_earth(): {create_earth()}")
print(f"create_fire(): {create_fire()}")
print(f"strength_potion(): {strength_potion()} and {create_fire()}")

print("\nAll import transmutation methods mastered!")
