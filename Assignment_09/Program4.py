##################################################################################################
#
#   Program Name : Program4.py
#   Discription  : Write a program which accepts one number and prints cube of that number
#   Function     : Cube()
#   Author       : Apurva Vilas Shinde
#   Date         : 18/01/2026
#
###################################################################################################

#   Input  :  5
#   Output :  125

def Cube(No):
    Ans = No ** 3
    # Ans = No * No * No

    return Ans

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = Cube(Value)

    print("Cube of ",Value," is : ",Ret)

if __name__ == "__main__":
    main()