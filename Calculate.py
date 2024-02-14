def add(a,b):
    s = a+b
    return s

def sub(a,b):
    s = a-b
    return s

def mul(a,b):
    s = a*b
    return s

def div(a,b):
    s = a/b
    return s

def calculate(a,b,operation):
    s=''
    if(operation=="+"):
        s = add(a, b)
        print("Adding %d and %d returns %d" %(a,b,s))
    elif(operation=="-"):
        s = sub(a, b)
        print("Subtracting %d from %d returns %d" %(b,a,s))
    elif(operation=="*"):
        s = mul(a, b)
        print("Multiplying %d and %d returns %d" %(a,b,s))
    elif(operation=="/"):
        s = div(a, b)
        print("Dividing %d by %d returns %f" %(a,b,s))
    else:
        print("Invalid operation entered!!")
    return s

def main():
    a = int(input("Enter 1st Value"))
    b = int(input("Enter 2nd value"))
    operation = input("Enter +,-,*,/ to indicate the operation to be performed")
    result = calculate(a,b,operation)
    print("Your result is: ", result)
    
main()