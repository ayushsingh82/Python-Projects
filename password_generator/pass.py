import random

characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%*"


while True:
    pass_length=int(input("enter the length of req. password: "))
    pass_count=int(input("enter the number of req. password: "))

    for i in range(0,pass_count):
        password=""
        for j in range(0,pass_length):
            pass_char=random.choice(characters)
            password=password+pass_char
        print("the generated password is: ", password) 
    repeat=input("Do you want to generate more passwords?")
    if repeat=="no" or repeat=="N0":
        break

print("Thank you")