def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
def show_menu():
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
while True:
    show_menu()
    choice = input("Choose an operation (1-5): ")
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == '1':
            result = add(num1, num2)
            print(f"The result of addition: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of subtraction: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of multiplication: {num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of division: {num1} / {num2} = {result}")
    elif choice == '5':
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid option. Please try again.")
