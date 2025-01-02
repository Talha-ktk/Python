import math

def calculator():
    while(True):
        print("!*!Python Calculator!*!")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Square Root")
        print("8. Cube")
        print("9. Exit")

        try:
            choice=int(input("Enter number between 1-9: "))
        except ValueError:
            print("Invalid Input,enter number etween 1 and 9 ...")
            continue

        if choice==9:
            print("Exiting,Gooodbye")
            break
        if choice in [1,2,3,4,5,6]:
            try:
                num1=float(input("Enter the first number : "))
                num2=float(input("Enter the second number : "))
            except ValueError:
                print("Invalid Input")
                continue
        
        if choice == 1: 
            print(f"Result : {num1}+{num2}={num1+num2}")
        elif choice == 2:
            print(f"Result : {num1}-{num2}={num1-num2}")
        elif choice == 3:
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == 4:
            if num1==0:
                print("Enter number rather than 0...")
            elif num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        elif choice == 5:
            print(f"Result: {num1} % {num2} = {num1 % num2}")
        elif choice == 6:
            print(f"Result: {num1} ^ {num2} = {num1 ** num2}")
        elif choice == 7:
            try:
                num = float(input("Enter the number for square root: "))
                if num < 0:
                    print("Error: Square root of a negative number is not defined in real numbers.")
                else:
                    print(f"Result: Square root of {num} = {math.sqrt(num)}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == 8:
            try:
                num = float(input("Enter the number to cube: "))
                print(f"Result: Cube of {num} = {num ** 3}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Invalid choice. Please select a number between 1 and 9.")

    
calculator()

