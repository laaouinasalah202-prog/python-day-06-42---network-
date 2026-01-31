import alchemy

print("=== Import Transmutation Mastery ===\n")
print("Method 1 - Full module import:")
print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

print("\nMethod 2 - Specific function import:")
from alchemy.elements import create_water

print(f"create_water(): {create_water()}")

print("\nMethod 3 - Aliased import:")
from alchemy.potions import healing_potion as heal

print(f"heal(): {heal()}")

print("\nMethod 4 - Multiple imports:")




# different import styles: import alchemy.elements
# • Specific imports: from alchemy.elements import create_fire
# • Aliased imports: from alchemy.potions import healing_potion as heal
# • Multiple imports: from alchemy.elements import create_fire, create_water
# • How each style affects your code differently