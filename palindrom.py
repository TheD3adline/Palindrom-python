# The script with the function to check the numbers for being a palindrom or not
# Source https://www.mygreatlearning.com/blog/palindrome-in-python/
def palindrom(num):
    temp = num
    revNum = 0
    while num > 0:
        digit = num % 10
        revNum = revNum * 10 + digit
        num = num // 10
    if temp == revNum:
        print("Gegebene Zahl ist ein Palindrom ")
    elif temp != revNum:
        print("Gegebene Zahl ist kein Palindrom ")