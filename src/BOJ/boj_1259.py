def isPalindrome(number: int) -> bool:
    number = str(number)
    for i in range(len(number) // 2):
        if number[i] != number[len(number) - i - 1]:
            return False
    return True

while True:
    number = int(input())
    if number == 0:
        break
    if isPalindrome(number):
        print("yes")
    elif not isPalindrome(number):
        print("no")
