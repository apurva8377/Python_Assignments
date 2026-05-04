########################################################################
#
#   Program Name : Assignment17_3.py
#   Author       : Apurva Vilas Shinde
#   Description  : Write a program which accept one number from user and return its factorial.
#   Input        : 5          
#   Output       : 120
#   Date         : 04/05/2026
#
#######################################################################

def Factorial(No):
    if No < 0:
        return("Invalid input")

    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    Ret = 0

    Value = int(input("Enter number : "))
    
    Ret = Factorial(Value)
    if(Ret == "Invalid input"):
        print("Invalid input")
    else:
        print("Factorial of",Value,"is : ",Ret)

if __name__ == "__main__":
    main()