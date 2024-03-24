n = int(input("Enter the number to find the factorial: "))
fact = 1
i = 1
while(i<=n):
    fact *= i
    i += 1
print("The Factorial of", n , " is: " , fact)