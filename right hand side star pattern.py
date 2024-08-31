def right_hand_star_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end ="")
        for j in range(i+1):
            print("*",end="")
        print ("\n")
num=int(input("Enter the number of rows:"))
print(right_hand_star_pattern(num))
print("To print the pattern the follwing code responsible.")
def right_hand_star_pattern_shortcode(number):
    for k in range (number):
        print(" "*(number-k-1)+"*"*(k+1))
    print("\n")
print(right_hand_star_pattern_shortcode(num))