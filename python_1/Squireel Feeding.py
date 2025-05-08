# Simple squirrel feeding script

# Maximum feedings per day
MAX_FEEDINGS = 3
feeding_count = 0

print("Welcome to the Squirrel Feeder!")
print("You can feed the squirrels up to 3 times per day.")

while True:
    if feeding_count < MAX_FEEDINGS:
        user_input = input("Type 'feed' to feed the squirrels or 'exit' to quit: ").strip().lower()
        if user_input == "feed":
            feeding_count += 1
            print(f"Squirrels fed! Total feedings today: {feeding_count}")
        elif user_input == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please type 'feed' or 'exit'.")
    else:
        print("The kitchen is closed. You've already fed the squirrels 3 times today.")
        break
