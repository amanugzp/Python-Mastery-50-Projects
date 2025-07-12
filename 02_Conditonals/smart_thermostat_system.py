device_status = "active"
temperature = int(input("Choose your city temperature: "))

if device_status == "active":
    if temperature >35:
        print("High temperature alert!")

    else:
        print("The temperature is normal")
else:
    print("Device is offline")