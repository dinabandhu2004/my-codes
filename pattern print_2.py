import time
def patternstar(n):
    for i in range(0,(n//2)+1):
        for j in range(0,i+1):
            print("*", end="")
        print("\r")
    for i in range((n//2)+1,n):
        for j in range(n-i):
            print ("*",end="")
        print("\r")

def declaration(n):
    if(num%2==0):
        print("The printed pattern will be un even.")
        print("\r")
    else:
        print ("The printed pattern will be even.")
        print("\r")

def decision_making(decision):
    if(decision.upper()== "YES"):
        print(patternstar(num))
    else:
        print("\033[1mprocess cancel\033[0m".center(170))

num=int(input("enter the number of maximum star:"))
print("\r")
declaration(num)
time.sleep(2)
print("would you really like see your pattern? make your answer below.")
time.sleep(2)
print("\r")
decision=str(input("Enter your dicision\033[1m(yes or no):\033[0m"))
print("\r")
decision_making(decision)