from time import *
import random as r



def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest:
                error+=1
        except :
            error+=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e - time_s
    time_R=round(time_delay,2)
    speed =len(userinput)/time_R
    return round(speed)
    
if __name__=='__main__':
    while True:
        chk =input("ready to test : yes/no :")
        if chk =="yes":
                test=["I think I had the same problem , I think it's because one variable was called time",
                    "my name is Happy Singh",
                    "welcome to my websie"]
                    
                test1=r.choice(test)
                print("*****typing speed*****")
                print(test1)
                print()
                print()
                time_1=time()
                testinput=input("Enter:  ")
                time_2=time()

                print('Speed :',speed_time(time_1,time_2,testinput),"w/sec")
                print("error :",mistake(test1,testinput))

        elif chk=="no":
            print("thank you")
            break
        
        else:
            print("wrong input")