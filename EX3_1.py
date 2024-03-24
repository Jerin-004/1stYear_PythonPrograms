print("URK23CS1101 Jerin_Stalin")
def palindrome(n):
    temp = n
    reverse = 0
    while temp > 0:
        reverse = (reverse * 10) + n%10
        temp //= 10
    if reverse == n:
        print("Palindrome")
    else:
        print("Not a palindrome")
    
palindrome(2242)