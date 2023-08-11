# we are making a secret coding language having atleast 3 characters

# if the word is at least 3 character remove first letter append to the last
# now append three random characters at the starting or at the end

# else:
# simply reverse the String 

# Decoding:
# if the word contain less than 3 characters ,reverse it
# else:
#     remove 3 random character from start and end .Now remove last letter and
# append to the begining

# your program should ask u want to code or decode

st=input("Enter the mssg:")
words=st.split(" ")
coding=input("1 for Coding and 0 forDecoding:")
coding=True if(coding=="1") else False
coding=True
if(coding):
    nwords=[]
    for word in words:
      if(len(word)>=3):
        r1="dsf"
        r2="jkr"
        stnew=r1+word[1:]+word[0]+r2
        nwords.append(stnew)
      else:
        nwords.append(word[::-1]) # method to reverse string
        print(" ".join(nwords)) 

else:
   nwords=[]
   for word in words:
      if(len(word)>=3):
         stnew=word[3:-3]
         stnew=stnew[-1]+stnew[:-1]
         nwords.append(stnew)
      else:
         nwords.append(word[::-1])
         print(" ".join(nwords))      