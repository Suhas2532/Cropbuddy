# Define the correct PIN
correct_pin = "1234"

# Initialize the attempt counter
attempts = 0

# Set the maximum attempts
max_attempts = 3

while attempts < max_attempts:
    # Prompt the user to enter the PIN
    pin = input("Enter your PIN: ")

    # Check if the PIN is correct
    if pin == correct_pin:
        print("Access granted")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempts remaining.")

if attempts == max_attempts:
    print("Maximum attempts exceeded. Account locked.")