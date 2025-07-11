essential_spices = {"cardamon","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

all_spices = essential_spices|optional_spices
print(f"All spices is {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only essential is {only_in_essential}")

print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}")
print(f"Is 'cloves' in essential spices? {'cloves' in optional_spices}")
