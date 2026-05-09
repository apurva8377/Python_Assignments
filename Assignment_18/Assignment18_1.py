########################################################################
#
#   Program Name   : Assignment18_1.py
#   Author         : Apurva Vials Shinde
#   Description    : Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
#   Function       : SumList()     
#   Input          : Number of elements : 6   
#   Input Elements : 13    5   45   7   4   56 
#   Output         : 130
#              
#   Date           : 01/05/2026
#
#######################################################################

def SumList(Arr):
    Sum = 0

    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    
    return Sum

def main():
    Size = int(input("Number of elements : "))
    ptr = []

    print("Enter the elements : ")
    for i in range(Size):
        ptr.append(int(input()))

    Ret = SumList(ptr)
    print("The sum of elements in list is : ",Ret)

if __name__ == "__main__":
    main()