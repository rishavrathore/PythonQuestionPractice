#Take two integers x and y as input from the user. 
# Your task is to define three functions to perform Arthemetic Operations(%,//,**)on the given inputs x and y.
# At the end call the three function and print to the console.

x = int(input())
y = int(input())
def mod(x,y):
    print(x%y)
mod(x,y)

def div(x,y):
    print(x//y)
div(x,y)

def expo(x,y):
    print(x**y)
expo(x,y)    
