#WAP to print  every integer btw 1 and n divisible by m also report whether the number divisible by m is even or odd

code:-
n= int(input("Enter n "))
m = int(input("Enter m "))
for i in range(1,n):
    if i%m == 0 :
        print(i,end=" ")
        if i%2==0:
            print("even")
        else:
            print("odd")
            
            
            
""" Output:-
  Enter n 12
Enter m 3
3 odd
6 even
9 odd"""
