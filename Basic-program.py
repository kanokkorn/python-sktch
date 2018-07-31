print("********************"+"\nThis is a basic calculator"+"\n********************")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
func = str(input("Choose what to do next \ntype add sub mul div :"))
if func == "add":
    print("Answer is "+str(a+b))
if func == "sub":
    print("Answer is "+str(a-b))
if func == "mul": 
    print("Answer is "+str(a*b))
if func == "div": 
    print("Answer is "+str(a/b))
