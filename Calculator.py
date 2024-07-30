
calculator=[]
a=int(input("Enter the range:"))
for i in range(1,a+1):
    b=int(input(f"Enter the value {i}:"))
    calculator.append(b)
print("List Value: ",calculator)

total=input("1.add \n2.sub \n3.mul \n4.div \nEnter the Operation: ")

if(total=="1"):
   sum=0
   for num in calculator:
       sum=sum+num
   print("Addition: ",sum)

elif(total=="2"):
    sub=calculator[0]
    for num in calculator[1:]:
        sub=sub-num
    print("Subraction: ",sub)
        
elif(total=="3"):
    mul=1
    for num in calculator:
        mul=mul*num
    print("Multiplication operation: ",mul)

elif(total=="4"):
    div=calculator[0]
    for num in calculator[1:]:
        div=div/num
    print("Division Operation: ",div)

else:
    print("invalid Operation")

