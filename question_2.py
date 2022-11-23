#take an integer number as input from the user.
#Your task is to add the number with 2 and then write the pyton function to print the factorial of the resultant number.


def factorial (n):
    if n==1:
        return 1
    else:
        s = n*factorial(n-1)
        return(s)
n = int(input())
n += 2
print(factorial(n))        
