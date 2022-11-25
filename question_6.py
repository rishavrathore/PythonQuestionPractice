#There is a data of 8 stanadard students. Your task is to call the function Data()with the
#argument's name and standard. The default class of the students is 8 and take only the name as
#input from user. Print the result as "Student name is XXXX and He/she is studying class 8"

def Data(name,std=8):
    print("Student name is",name,"and He/she is studying class",std)
s = input("name: ")    
Data(s)