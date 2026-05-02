####################################################################################################
#
#   Program Name : Assignment16_10.py
#   Author       : Apurva Vials Shinde
#   Description  : Write a program which accept name from user and display length of its name.
#   Input        : Marvellous    
#   Output       : 10
#   Date         : 02/05/2026
#
####################################################################################################

def DisplayLength(Name):
    print("The length of",Name,"is",len(Name))

def main():
    Data = input("Enter the name : ")

    DisplayLength(Data)

if __name__ == "__main__":
    main()
