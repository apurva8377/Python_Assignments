####################################################################################################
#
#   Program Name : Assignment16_9.py
#   Author       : Apurva Vials Shinde
#   Description  : Write a program which display first number of even numbers on screen.
#   Function     : DisplayEven(No)       
#   Input        : 10      
#   Output       : 2    4   6   8   10   12  14   16   18   20  
#   Date         : 02/05/2026
#
####################################################################################################

def DisplayEven(No):
    Count = 0
    Num = 2

    while Count < No:
        print(Num, end=" ")
        Num = Num + 2
        Count = Count + 1

    print()

def main():
    Value = int(input("Enter the number : "))

    DisplayEven(Value)

if __name__ == "__main__":
    main()
