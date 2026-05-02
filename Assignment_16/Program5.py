####################################################################################################
#
#   Program Name : Assignment16_5.py
#   Author       : Apurva Vials Shinde
#   Description  : Write a program which display 10 to 1 on screen.
#   Function     : Display(No)       
#   Input        : ---        
#   Output       : 10  9  8  7  6  5  4  3  2  1
#   Date         : 01/05/2026
#
####################################################################################################

def Display(No):
    for i in range(No,0,-1):
        print(i)

def main():
    Value = int(input("Enter the number : "))
    Display(Value)

if __name__ == "__main__":
    main()
