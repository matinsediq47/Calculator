
try:
    loop = True
    while loop:
        x = input('Please enter "Start" to start the calculator:  ').upper()
        while x == "START":
            y = input("""
Please enter the operation you want:
+ for Addition
- for Subtraction
* for Multiplication
/ for Division
'quit' to Quit:
""")
            if y == "+":
                a = int(input("Enter your first number: "))
                b = int(input("Enter your second number: "))
                c = a + b
                print(f"{a} + {b} = {c}")
            elif y == "-":
                a = int(input("Enter your first number: "))
                b = int(input("Enter your second number: "))
                c = a - b
                print(f"{a} - {b} = {c}")
            elif y == "*":
                a = int(input("Enter your first number: "))
                b = int(input("Enter your second number: "))
                c = a * b
                print(f"{a} * {b} = {c}")
            elif y == "/":
                a = int(input("Enter your first number: "))
                b = int(input("Enter your second number: "))
                c = a / b
                d = a % b
                print(f"{a} / {b} = {c}")
                print(f"The remaining of division is: {d}")
            elif y == "quit":
                loop = False
                break
            else:
                print("Wrong input!")
except Exception as e:
    print(f"Error occured: {e}")