############################################################################################################
#
#   Program Name : Program1.py (Assignment_12)
#   Discription  : Write a program which accepts one character from user and checks whether it is vowel or not
#   Function     : CheckVowel()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
#############################################################################################################

#    Input : a
#    Output : Vowel

def CheckVowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        return True
    else:
        return False

def main():
    ch = '0/'

    Ret = '0/'

    print("Enter the character : ")

    ch = input()

    Ret = CheckVowel(ch)

    if Ret == True:
        print(ch,"is a vowel")
    else:
        print(ch,"is not a vowel")

if __name__ == "__main__":
    main()