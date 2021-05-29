#prime number
n=int(input('enter number'))
i=1
count=0
while(i<=n//2):
    print(i)
    if(n%i==0):
        count+=1
        i+=1
    if(count==1):
        print('%d is a prime number'%(n))
    else:
            print('%d is not a prime number'%(n))
...output
enter number5
5 is a prime number
