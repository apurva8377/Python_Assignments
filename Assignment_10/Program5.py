#################################################################################################
#
#   Program Name : Program5.py (Assignment_10)
#   Discription  : Write a program which accepts one number and prints odd numbers till that number
#   Function     : DisplayEven()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
#################################################################################################

# Input :  10 
# Output : 1    3   5   7   9

def DisplayOdd(No):
    Fact = 1
    i = 0

    print("Odd numbers are : ")

    for i in range(1, No+1):
        if i % 2 != 0:
            print(i)

def main():
    Value = 0
    
    print("Enter the number : ")
    Value = int(input())

    DisplayOdd(Value)

if __name__ == "__main__":
    main()