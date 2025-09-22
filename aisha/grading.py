marks=int(input("enter your marks:(0-100)\n"))
if marks>=90:
     grade= "\nA"
elif marks>=75 and marks<=90:
     grade= "\nB"
elif marks>=50 and marks<= 75:
     grade="\nC"
else: grade= "\nF"