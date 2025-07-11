Coffee_type = "Black Coffee"
customer_name = "Jaya"

print(f"Order for {customer_name} : {Coffee_type} Plase!")

coffee_description = "Cold and Chocolate"
print(f"First word: {coffee_description[0:4]}")
print(f"last word: {coffee_description[9:]}")
print(f"First word: {coffee_description[::-1]}")

label_text = "Coffee Spécial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded lable: {label_text}")
print(f"Encoded lable: {ecoded_label}")
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label is {decoded_label}")