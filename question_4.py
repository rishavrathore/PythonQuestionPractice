# Take a NXN matrix,and print it.

# If you found 1 at any of the ith row and jth column in the matrix, then pair up i and j as a 
# tuple (i,j) and insert the tuple in the resultant list.

# Print the resultant list where each element is a tuple containing (i,j) coordinate where the 
# shell value is 1

n=int(input())
l1=[]
l2=[]
for i in range(n):
    l3=[]
    for j in range(n):
        d=int(input())
        l3.append(d)
        if d==1:
            l1.append((i,j))
    l2.append(l3)
[print(i) for i in l2]
print(l1)            