num=int(input("enter the number" ))
iscom=0
for i in range(2,num):
    if(num%i==0):
        iscom=1
        break
if(iscom==1):
    print("number is composite")
else:
    print("number is prime")
