# Your task is to:
# 1. Take a string as input from the user
# 2. Exclude the case where the character is 'a' and print a list of preceding characters in string.


a = input()
s=""
for i in a:
    if i!="a":
        s+=chr(ord(i)-1)

b = []
for i in s:
    b.append(i)
print(b)            