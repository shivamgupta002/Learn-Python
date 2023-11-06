# ---------------------- If-else statement  -------------------------------------------

age=input("What is your age : ")
if (int(age) > 18) and (int(age) <60) :
    print("You are Young")
elif int(age)>=60:
    print("You are old")
elif(int(age)>0) and(int(age) <18):
    print("You are kid")
else:
    print("Not Valid age")