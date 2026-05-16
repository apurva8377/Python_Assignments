########################################################################
#
#   Program Name   : Assignment20_2.py
#   Author         : Apurva Vials Shinde
#   Description    : Design a Python application that creates two threads named EvenFactor and OddFactor.
#   •Both threads should accept one integer number as a parameter.
#   •The EvenFactor thread should: 
#       • Identify all even factors of the given number.
#       • Calculate and display the sum of even factors.
#   The OddFactor thread should:
#       ◦Identify all odd factors of the given number.
#       ◦Calculate and display the sum of odd factors.
#   After both threads complete execution, the main thread should display the message: “Exit from main”        
#   Date           : 12/05/2026
#
#######################################################################

import threading

lobj = threading.Lock()

def EvenFactor(No):
    Sum = 0
    Factors = []

    for i in range(1, No+1):
        if((No % i == 0) and (i % 2 == 0)):
            Sum = Sum + i
            Factors.append(i)

    with lobj:
        print("-----------------------------------------------------------")
        print(f"EvenFactor Thread : Even factors of {No} are : {Factors}")
        print(f"EvenFactor Thread : Sum of even factor is : {Sum}")
        print("-----------------------------------------------------------")
        

def OddFactor(No):
    Sum = 0
    Factors = []

    for i in range(1,No+1):
        if((No % i == 0) and (i % 2 != 0)):
            Sum = Sum + i
            Factors.append(i)

    with lobj:
        print("-----------------------------------------------------------")
        print(f"OddFactor Thread : Odd factors of {No} are : {Factors}")
        print(f"OddFactor Thread : Sum of odd factor is : {Sum}")
        print("-----------------------------------------------------------")
        

def main():
    print("Enter the value : ")
    Value = int(input())

    t1 = threading.Thread(target=EvenFactor, args=(Value,) ,name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(Value,), name=OddFactor)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()