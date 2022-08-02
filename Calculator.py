firstNum = input("What is the first number you want to calculate?\n")
operation = input("What is the operation you would like to?\n")
# 1+2
# ^^^
# var = Hello
# var.lower()
# var = hello
secondNum = input("What is the second number for your equation?\n")
if (operation == "+"):
    ansr = firstNum + secondNum
    print(ansr)
elif (operation == "-"):
    ansr = firstNum - secondNum
    print(ansr)