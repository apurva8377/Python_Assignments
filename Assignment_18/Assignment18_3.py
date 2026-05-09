########################################################################
#
#   Program Name   : Assignment18_3.py
#   Author         : Apurva Vilas Shinde
#   Description    : Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
#   Input          : Number of elements : 7  
#   Input Elements : 13    5   45   7   4   56    34
#   Output         : 4       
#   Date           : 09/05/2026
#
#######################################################################

def Minimum(Arr):
    if len(Arr) == 0:
        return None
    
    Min = Arr[0]

    for i in range(1,len(Arr)):
        if(Min > Arr[i]):
            Min = Arr[i]

    return Min
    
def main():
    Size = int(input("Enter the number of elements : "))

    Ptr = []

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Ptr.append(Value)
    
    Ret = Minimum(Ptr)

    print("The Minimum element from the List is : ",Ret)

if __name__ == "__main__":
    main()