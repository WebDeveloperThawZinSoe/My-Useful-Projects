import math

Green = '\033[92m'
Red = '\033[31m'
Rest = '\033[0m'


print(f"{Green}Welcome Thaw's From Simple Python Calculator. {Rest}")
print(f"{Red}Enter First Number , Enter Second Number , Enter Operation (+,-,*,%). {Rest}")
while True:
    first_number = float(input(f"{Green}Enter First Number : {Rest}"))
    second_number = float(input(f"{Green}Enter Second Number : {Rest}"))
    operator = input(f"{Green}Enter Operator : {Rest}")
    result = ""
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "%":
        result = first_number % second_number
    elif operator == "E" or operator == "e":
        break
    else:
        print(f"{Red} Please Choice (+,*,%,/){Rest}")

    print(result)



