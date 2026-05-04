########################################################################
#
#   Program Name : Assignment17_2.py
#   Author       : Apurva Vilas Shinde
#   Description  : Write a program which accept one number and display below pattern.
#   Input        : 5           
#   Output       : *    *   *   *
#                  *    *   *   *
#                  *    *   *   *
#                  *    *   *   *
#   Date         : 04/05/2026
#
#######################################################################

def DisplayPattern(No):
    for i in range(No):
        for j in range(No):
            print("*", end="    ")
        print()

def main():
    Value = int(input("Enter number : "))
    DisplayPattern(Value)

if __name__ == "__main__":
    main()