#calculator

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2st number: "))
operator = input("Enter the following operators to perform the operation ( + , - , / , x ): ")


if operator == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == 'x':
    print(f"{num1} x {num2} = {num1 * num2}")
elif operator == '/':
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid operator")