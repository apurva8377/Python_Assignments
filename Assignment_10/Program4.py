#################################################################################################
#
#   Program Name : Program.py (Assignment_02)
#   Discription  : Write a program which accepts one number and prints even number till that number
#   Function     : DisplayEven()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
#################################################################################################

# Input :  10 
# Output : 2    4   6   8   10

def DisplayEven(No):
    Fact = 1
    i = 0

    for i in range(1, No+1):
        if i % 2 == 0:
            print(i)

def main():
    Value = 0
    
    print("Enter the number : ")
    Value = int(input())

    DisplayEven(Value)

if __name__ == "__main__":
    main()