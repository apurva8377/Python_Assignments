############################################################################################################################
#
#   Program Name : Program5.py (Assignment_12)
#   Discription  : Write a program which accepts one numbers and prints that many numbers in reverse order
#   Function     : DisplayReverseNumbers()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
############################################################################################################################

#    Input : 5
#    Output : 1   2   3   4   5

def DisplayReverseNumbers(No):
    print("numbers from",No,"to 1 are : ")

    for i in range(No, 0, -1):
        print(i)
    
def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    DisplayReverseNumbers(Value)

if __name__ == "__main__":
    main()