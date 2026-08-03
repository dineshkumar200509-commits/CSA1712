# Vacuum Cleaner Problem using Simple Reflex Agent

def vacuum_cleaner():
    rooms = {
        "A": "Dirty",
        "B": "Dirty"
    }

    current_room = "A"

    print("Initial Room Status:")
    print(rooms)
    print()

    while True:
        if rooms[current_room] == "Dirty":
            print(f"Vacuum is in Room {current_room}.")
            print("Room is Dirty -> Cleaning...")
            rooms[current_room] = "Clean"
        else:
            print(f"Room {current_room} is already Clean.")

        # Check if all rooms are clean
        if all(status == "Clean" for status in rooms.values()):
            print("\nAll rooms are clean.")
            break

        # Move to the other room
        if current_room == "A":
            print("Moving to Room B...\n")
            current_room = "B"
        else:
            print("Moving to Room A...\n")
            current_room = "A"

    print("\nFinal Room Status:")
    print(rooms)

# Driver Code
vacuum_cleaner()