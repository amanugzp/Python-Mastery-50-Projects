ingredients = ["water","milk","black tea"]
ingredients.append("sugar")
print(f"Ingradients are: {ingredients}")
ingredients.remove("milk")
print(f"Ingradients are: {ingredients}")

spice_options =  ["ginger","cardamon"]
chai_ingredients = ["water","milk"]

chai_ingredients.extend(spice_options)
print(f"Chai: {chai_ingredients}")
chai_ingredients.insert(2,"black tea")
print(f"Chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"Chai: {chai_ingredients}")
chai_ingredients.reverse()
print(f"Chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"Chai: {chai_ingredients}")

suger_levels = [1,2,3,4,5]
print(f"Maximum suger level: {max(suger_levels)}")
print(f"Maximum suger level: {min(suger_levels)}")

base_liquid = ["water","milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix is {full_liquid_mix}")

strong_brew = ["black_tea","black Coffee"]*3
print(f"string brew: {strong_brew}")

raw_spice_data = bytearray(b"CHINNAMON")
raw_spice_data.replace(b"CHINNA",b"CARD")
print(f"Bytes:{raw_spice_data}")