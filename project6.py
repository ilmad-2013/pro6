
print("================================")
print("         FUNCTION CALCULATOR")
print("================================")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a % b

while True:
    print("\n========== MENU ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Remainder")
    print("7. Exit")

    choice = input("Choose an operation: ")

    if choice == "7":
        print("Calculator closed. Goodbye!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice. Try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        answer = add(num1, num2)

    elif choice == "2":
        answer = subtract(num1, num2)

    elif choice == "3":
        answer = multiply(num1, num2)

    elif choice == "4":
        answer = divide(num1, num2)

    elif choice == "5":
        answer = power(num1, num2)

    elif choice == "6":
        answer = remainder(num1, num2)

    print("Your answer is:", answer)

    print("--------------------------")
