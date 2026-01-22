############################################################################################################
#
#   Program Name : Program2.py (Assignment_12)
#   Discription  : Write a program which accepts one number and prints it's character
#   Function     : DisplayFactors()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
#############################################################################################################

#    Input : 12
#    Output : 1 2 3 4 6 12

def DisplayFactors(No):
    i = 0

    print("Factors of",No,"are : ")

    for i in range(1, No+1):
        if No % i == 0:
            print(i)
    

def main():
    Value = 0

    print("Enter the number : ")

    Value = int(input())

    DisplayFactors(Value)

if __name__ == "__main__":
    main()