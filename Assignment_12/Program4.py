############################################################################################################################
#
#   Program Name : Program4.py (Assignment_12)
#   Discription  : Write a program which accepts one numbers and prints that many numbers starting from 1
#   Function     : DisplayNumbers()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
############################################################################################################################

#    Input : 5
#    Output : 1   2   3   4   5

def DisplayNumbers(No):
    print("numbers from 1 to",No,"are : ")

    for i in range(1, No+1):
        print(i)
    
def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    DisplayNumbers(Value)

if __name__ == "__main__":
    main()