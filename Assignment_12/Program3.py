############################################################################################################################
#
#   Program Name : Program3.py (Assignment_12)
#   Discription  : Write a program which accepts two numbers and prints addition, substraction, multiplication and division
#   Function     : ArithmaticOperations()
#   Author       : Apurva Vilas Shinde
#   Date         : 22/01/2026
#
############################################################################################################################

#    Input : 12  6
#    Output : Addition :  18
#             Sunstrction :  6
#             Multiplication is :  72
#             Division is :  2.0

def ArithmaticOperations(No1, No2):
    print("Addition : ",No1+No2)
    print("Sunstrction : ",No1-No2)
    print("Multiplication is : ",No1*No2)
    print("Division is : ",No1/No2)
    
def main():
    Value1 = 0
    Value2 = 0

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    ArithmaticOperations(Value1, Value2)

if __name__ == "__main__":
    main()