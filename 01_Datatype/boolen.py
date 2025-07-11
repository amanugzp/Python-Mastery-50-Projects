is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling  # upcasting
print(f"Total Actions: {total_actions}")

milk_present = 0 # No milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True 
coffee_added = False

can_server = water_hot and coffee_added
print(f"Can serve Coffee? {can_server}")