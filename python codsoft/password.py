import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation1
    password = ''.join(random.choice(characters) for i in range(length))
    return password
def show_menu():
    print("\nPassword Generator")
    print("1. Generate Password")
    print("2. Exit")
while True:
    show_menu()
    choice = input("Choose an option (1-2): ")
    if choice == '1':
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length must be at least 1.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    elif choice == '2':
        print("Thank you for using the Password Generator!")
        break
    else:
        print("Invalid option. Please try again.") 