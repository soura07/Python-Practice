num = int (input("Enter the value: "))

if(num < 0):
    print("Number is negetive")
elif(num > 0):
    print("Number is positive")
else:
    print("Number is equal")
# subject gread prolem

marks = int(input("Enter your marks in 500: "))

if(marks>=450):
    print("You got A")
elif(marks >=400):
    print("You got B gread")
elif(marks >=350):
    print("You got C gread")
else:
    print("You got D gread")


#IF YOUR AGE IS 22 to 30 you can drive a car
#If Your Age is 18 to 22 then you drive bike
#If your Age is less than 18 then you can drive a Cycle

age = int(input("Enter your age "))
if(age >=22 and age <= 30):
    print("You can drive a CAR")
elif(age >=18 and age <=22):
    print("You can drive Bike")
elif(age < 18 and age>5):
    print("You can Cycling")
else:
    print("Ghore dudu khao")