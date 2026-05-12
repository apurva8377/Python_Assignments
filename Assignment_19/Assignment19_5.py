########################################################################
#
#   Program Name      : Assignment19_5.py
#   Author            : Apurva Vials Shinde
#   Description       : Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
#   Input List        : [2, 70 , 11, 10, 17, 23, 31, 77]
#   List after filter : [2, 11, 17, 23, 31]
#   List after map    : [4, 22, 34, 46, 62]
#   Output of reduce  : 624         
#   Date           : 11/05/2026
#
#######################################################################

from functools import reduce

def CheckPrime(No):
    if No <= 1 :
        return False
    for i in range(2, int(No**0.5) + 1):
        if No % i == 0:
            return False
    return True

Multiply = lambda No : No * 2

def Maximum(A, B):
    if A > B:
        return A
    else:
        return B

def main():
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Actual data is : ",Data)

    FData = list(filter(CheckPrime,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Multiply,FData))
    print("Data after map is : ",MData)

    RData = reduce(Maximum,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()