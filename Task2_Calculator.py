def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def division(num1,num2):
    if num2==0:
        return "error division by zero is not allowed!"
    else:
        return num1/num2


while True:
    print("===========Calculator menu from codsoft==========")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")

    try:
        choice=int(input("enter your choice:"))

        if choice==1:
            print("eneter your two numbers:")
            num1=float(input("enter first number:"))
            num2=float(input("enter second number:"))
            print(f"{num1}+{num2}={add(num1,num2)}")

        elif choice==2:
            print("eneter your two numbers:")
            num1=float(input("enter first number:"))
            num2=float(input("enter second number:"))
            print(f"{num1}-{num2}={subtract(num1,num2)}")

        elif choice==3:
            print("eneter your two numbers:")
            num1=float(input("enter first number:"))
            num2=float(input("enter second number:"))
            print(f"{num1}*{num2}={multiply(num1,num2)}")

        elif choice==4:
            print("eneter your two numbers:")
            num1=float(input("enter first number:"))
            num2=float(input("enter second number:"))
            print(f"{num1}/{num2}={division(num1,num2)}")

        elif choice==5:
            print("Thank you for using codsoft calculator! goodbye!")
            break
        else:
            print("Invalid choice! please enter a valid choice!")

    except ValueError:
        print("Invalid input! please enter valid numbers!")