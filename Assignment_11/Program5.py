###############################################################################################################
#
#   Program Name : Program5.py (Assignment_11)
#   Discription  : Write a program which accepts one number from user and check whether it is palindrome or not
#   Function     : Display()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
###############################################################################################################

#    Input  : 123
#    Output : 321

def Checkpalindrome(No):
    temp = No
    Rev = 0
    Digit = 0

    while No > 0:
        Digit = No % 10
        Rev = (Rev * 10) + Digit
        No = No // 10

    if Rev == temp:
        return True
    else:
        return False

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")

    Value = int(input())

    Ret = Checkpalindrome(Value)

    if Ret == True:
        print(Value,"is palindrome number")
    else:
        print(Value,"is not a palindrome number")

if __name__ == "__main__":
    main()