factorial = 1 
num =5 
if num<0:
    print("No Factorial exist for the number which is less than zero")
elif num==0:
    print("The Factorial of Zero is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i 
    print("The factorial of",num,"is",factorial)
