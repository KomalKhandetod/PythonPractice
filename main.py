def addition(a,b):
    addition_ans=a+b
    return addition_ans

def multiplication(a,b):
    multiplication_ans=a*b
    return multiplication_ans

def main():
    str1 = input("Enter the first value")
    str2 = input("Enter the second value")
    a=int(str1)
    b=int(str2)
    result1 = addition(a,b)
    result2 = multiplication(a,b)
    print("Addition of %s and %s is %d" %(str1,str2,result1))
    print("Multiplication of %s and %s is %d" %(str1,str2,result2))
 
main()