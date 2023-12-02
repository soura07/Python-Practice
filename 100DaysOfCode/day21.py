def average(a,b):
    print("The average is ", (a+b)/2)

average(5,4)

def name(fname, mname ="john", lname= "sanket"):
    print("hello", fname, mname, lname)

name("Souradeep")

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

c = average(5,6,7,1)    
print(c)