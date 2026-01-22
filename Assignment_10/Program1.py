######################################################################################################################
#
#   Program Name : Program1.py (Assignment_10)
#   Discription  : Write a program which accepts one number from user and print multiplication of that number
#   Function     : Display()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
######################################################################################################################

# Input :   4
# Output :  4 8 12 16 20 24 28 32 36 40

def Display(No):
    Table = 0
    i = 1

    print("The table of",No,"is : ")

    while i <= 10:
        Table = No * i
        print(Table)
        i = i + 1


def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()