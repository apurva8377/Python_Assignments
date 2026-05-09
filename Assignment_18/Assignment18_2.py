########################################################################
#
#   Program Name   : Assignment18_2.py
#   Author         : Apurva Vilas Shinde
#   Description    : Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.   
#   Input          : Number of elements : 6   
#   Input Elements : 13    5   45   7   4   56    34
#   Output         : 56       
#   Date           : 09/05/2026
#
#######################################################################

def Maximum(Arr):
    if len(Arr) == 0:
        return None
    
    Max = Arr[0]

    for i in range(1, len(Arr)):
        if Arr[i] > Max:
            Max = Arr[i]

    return Max

def main():
    Size = int(input("Number of elements : "))

    Ptr = []

    print("Enter the numbers : ")
    for i in range(Size):
        Value = int(input())
        Ptr.append(Value)

    Ret = Maximum(Ptr)

    print("The Maximum number is : ",Ret)

if __name__ == "__main__":
    main()