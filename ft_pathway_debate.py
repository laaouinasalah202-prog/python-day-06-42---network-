import alchemy.transmutation
from alchemy.transmutation import lead_to_gold, stone_to_gem
from alchemy.transmutation import philosophers_stone, elixir_of_life

print("\n=== Pathway Debate Mastery ===\n")

''' demostration of absolute import using
    from alchemy.transmutation import lead_to_gold, stone_to_gem
'''

print("Testing  AbsoluteImports (from basic.py):")
print(f"lead_to_gold(): {lead_to_gold()}")
print(f"stone_to_gem(): {stone_to_gem()}")

'''demostrating relative import using
    rom alchemy.transmutation import philosophers_stone, elixir_of_life
'''

print("\n# Testing Relative Imports (from advanced.py):")
print(f"philosophers_stone(): {philosophers_stone()}")
print(f"elixir_of_life(): {elixir_of_life()}")

''' demostrating the package access using
    import alchemy.transmutation
'''

print("\nTesting Package Access:")
print(
    "alchemy.transmutation.lead_to_gold():"
    f" {alchemy.transmutation.lead_to_gold()}"
    )
print(
    "alchemy.transmutation.philosophers_stone(): "
    f"{alchemy.transmutation.philosophers_stone()}"
    )

print("\nBoth pathways work! Absolute: clear, Relative: concise")
