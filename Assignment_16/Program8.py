####################################################################################################
#
#   Program Name : Assignment16_8.py
#   Author       : Apurva Vials Shinde
#   Description  : Write a program which accept number from user and print that number of “*” on screen.
#   Function     : DisplayPattern(No)       
#   Input        : 5      
#   Output       : *    *   *   *   *
#   Date         : 01/05/2026
#
####################################################################################################

def DisplayPattern(No):
    for i in range(No):
        print("*", end=" ")
    print()

def main():
    Value = int(input("Enter the number : "))

    DisplayPattern(Value)

if __name__ == "__main__":
    main()
