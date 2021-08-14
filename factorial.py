print("The factorial of a number is the product of all the integers from 1 to that number.")
print("Find the factorial of a number by entering the number below:")

number=int(input("Enter a number:"))
factorial_num=1

i=1

if(number<0):
    print("Factorial does not exist for negative numbers")

elif(number==0):
    print("The factorial of 0 is 1")

else:
    while i<=number:
        factorial_num=factorial_num*i
        i=i+1

print("The factorial of " + str(number) + " is " + str(factorial_num))