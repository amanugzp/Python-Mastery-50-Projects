flavours = ["Ginger","Out of Stock","Lemon","Discontinued","Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        print(f"{flavour} item found")
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} item found")


print("Out side of loop")



staff = [("Satym",15),("Aman",28),("Jaya",27),("Aanchal",25)]

for name , age in staff:
    if age >=18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("No one is eligible to manage the staff")