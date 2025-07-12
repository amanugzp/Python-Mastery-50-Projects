seat_type = input("Enter the seat type (Sleeper/AC/General/Luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC,beds available")

    case "ac":
        print("AC - AC and beds available")

    case "luxury":
        print("Luxury - AC and beds with food is available.")  
    case "general":
        print("General - Only seat is available.")

    case _:
        print("Invalid seat type")              