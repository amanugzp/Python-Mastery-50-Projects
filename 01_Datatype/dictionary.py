chai_order = dict(type = "Masala Chai",size = "Large",sugar = 2)
print(f"Chai Order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe["base"]}")
del chai_recipe["liquid"]
print(f"Recipe : {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Masala Chai", "size": "Medium", "sugar": 1}

# print(f"Order details (Keys): {chai_order.keys()}")
# print(f"Order details (Values): {chai_order.values()}")
# print(f"Order details (Items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom":"crushed","ginger":"sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {extra_spices}")


customer_notes = chai_order.get("note","no note")
print(f"customer notes is {customer_notes}")