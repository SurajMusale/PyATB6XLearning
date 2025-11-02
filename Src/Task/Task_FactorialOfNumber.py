num=int(input("Enter a number which factorial you want: ").strip())

fact=1

if(num<0):
    print("Factorial is not defined")
if(num<=0):
    print("Fact= ",fact)
else:
    for i in range(1,num+1):
        fact*=i
        print("Factorial of number is: ",fact)
