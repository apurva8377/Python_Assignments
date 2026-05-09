########################################################################
#
#   Program Name   : Assignment18_4.py
#   Author         : Apurva Vilas Shinde
#   Description    : Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
#   Input          : Number of elements : 11 
#   Input Elements : 13    5   45   7   4   56    5    34   2   5   65
#   Element to search : 5
#   Output         : 3      
#   Date           : 09/05/2026
#
#######################################################################

def CountFrequency(Arr,Target):
    Count = 0
    
    for num in Arr:
        if num == Target:
            Count = Count + 1

    return Count
    
def main():
    Size = int(input("Enter the number of elements : "))

    Ptr = []

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Ptr.append(Value)

    No = int(input("Enter the number that you want to search : "))
    
    Ret = CountFrequency(Ptr,No)

    print("The",No,"occurs",Ret,"times")

if __name__ == "__main__":
    main()