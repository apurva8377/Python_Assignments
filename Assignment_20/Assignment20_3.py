######################################################################################################
#
#   Program Name   : Assignment20_3.py
#   Author         : Apurva Vials Shinde
#   Description    : Design a Python application that creates two threads named EvenList and OddList.
#   •Both threads should accept a list of integers as input.
#   •The EvenList thread should:
#       • Extract all even elements from the list.
#       • Calculate and display their sum.
#   The OddList thread should:
#       ◦Extract all odd elements from the list.
#       ◦Calculate and display their sum.
#   Threads should run concurrently.     
#   Date           : 12/05/2026
#
#######################################################################################################

import threading

def EvenList(List):
    Sum = 0
    EvenElements = []

    for no in List:
        if (no % 2 == 0):
            EvenElements.append(no)
            Sum = Sum + no

    print("-------------------------------------------------------------------------------")
    print(f"EvenList Thread = The even elements from the list are {EvenElements}")
    print(f"Sum of even elements are  : {Sum}")
    print("-------------------------------------------------------------------------------")

def OddList(List):
    Sum = 0
    OddElements = []

    for no in List:
        if (no % 2 != 0):
            OddElements.append(no)
            Sum = Sum + no

    print("-------------------------------------------------------------------------------")
    print(f"OddList Thread = The odd elements from the list are {OddElements}")
    print(f"Sum of odd elements are  : {Sum}")
    print("-------------------------------------------------------------------------------")


def main():
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = []

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=EvenList, args=(Data,), name=EvenList)
    t2 = threading.Thread(target=OddList, args=(Data,), name=OddList)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()