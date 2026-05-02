####################################################################################################
#
#   Program Name : Assignment16_4.py
#   Author       : Apurva Vials Shinde
#   Description  : Write a program which display 5 times Marvellous on screen
#   Function     : Display(No)       
#   Input        : 5           
#   Output       : Marvellous
#                  Marvellous
#                  Marvellous
#                  Marvellous
#                  Marvellous
#   Date         : 01/05/2026
#
####################################################################################################

def Display(No):
    for i in range(No):
        print("Marvelous")

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()
