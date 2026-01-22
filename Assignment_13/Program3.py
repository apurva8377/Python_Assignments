############################################################################################################
#
#   Program Name : Program3.py (Assignment_13)
#   Discription  : Write a program which accepts number and checks whether it is perfect or not
#   Function     : CheckPerfect()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
#############################################################################################################

#  Input  : 28
#  Output : 28 is a perfect number

def CheckPerfect(No):
    i = 0
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    if Sum == No:
        return True
    else:
        return False

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = CheckPerfect(Value)

    if Ret == True:
        print(Value,"is a perfect number")
    else:
        print(Value,"is not a perfect number")

if __name__  == "__main__":
    main()