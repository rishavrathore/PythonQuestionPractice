#The task to be performed infunction word()is:
#1. Take five integers as input from the user
#2. Return the integer by combining all the integers in the user-given sequence

def Digit(*args):
    s=""
    for i in args:
        s+=str(i)
    return s
a=int(input())        
b=int(input())
c=int(input())
d=int(input())
e=int(input())
print(Digit(a,b,c,d,e))