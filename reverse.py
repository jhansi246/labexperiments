#reverse number
n=int(input('enter number:'))
sum=0
temp=n
#stemp=0
#n=temp
while n!=0:
    r=n%10
    sum=sum*10+r
    n//=10
    print('reverse of %d is %d '%(temp,sum))
..,output

enter number:345
reverse of 345 is 5 
reverse of 345 is 54 
reverse of 345 is 543 
