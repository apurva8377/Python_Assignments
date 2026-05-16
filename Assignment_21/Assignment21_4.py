########################################################################
#
#   Program Name   : Assignment21_3.py
#   Author         : Apurva Vials Shinde
#   Description    : Design a Python application that creates two threads.
#        •Thread 1 should compute the sum of elements from a list.
#        •Thread 2 should compute the product of elements from the same list.
#        •Return the results to the main thread and display them.
#   Date           : 16/05/2026
#
#######################################################################

import threading

def Summation(List, Result):
    Sum = 0

    for no in List:
        Sum = Sum + no

    Result["Sum"] = Sum

def Multiplication(List, Result):
    Mult = 1

    for no in List:
        Mult = Mult * no

    Result["Mult"] = Mult

def main():
    print("Enter the number of elements : ")
    Size = int(input())

    Data = []

    print("Enter the elemnts : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    ThreadResult = {}

    t1 = threading.Thread(target=Summation, args=(Data,ThreadResult), name="Summation")

    t2 = threading.Thread(target=Multiplication, args=(Data, ThreadResult), name="multiplication")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"The summation of elements from list is : {ThreadResult["Sum"]}")

    print(f"The multiplication of elements from list is : {ThreadResult["Mult"]}")

if __name__ == "__main__":
    main()

