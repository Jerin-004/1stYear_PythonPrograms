n = int(input("Enter the number to check: "))
i = 2
flag = 0
while(i < n):
    if(n % i == 0):
        flag = 1
    i += 1

if(flag == 1):
    print("The given number",n,"is not a prime number")
else:
    print("The given number",n,"is a prime number")