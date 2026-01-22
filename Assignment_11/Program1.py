############################################################################################################
#
#   Program Name : Program1.py (Assignment_11)
#   Discription  : Write a program which accepts one number from user and checks whether it is prime or not
#   Function     : Display()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
#############################################################################################################

#    Input : 11
#    Output : 11 is not a prime number

def CheckPrime(No):
    i = 0

    if No <= 1:
        return False
    
    for i in range(2, No):
        if No % i == 0:
            return False

    return True


def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")

    Value = int(input())

    Ret = CheckPrime(Value)

    if Ret == True:
        print(Value,"is a prime number")
    else:
        print(Value,"is not a prime number")

if __name__ == "__main__":
    main()