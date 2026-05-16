########################################################################
#
#   Program Name   : Assignment21_1.py
#   Author         : Apurva Vials Shinde
#   Description    : Design a Python application that creates two threads named Prime and NonPrime.
#        •Both threads should accept a list of integers.
#        •The Prime thread should display all prime numbers from the list.
#        •The NonPrime thread should display all non-prime numbers from the list.        
#   Date           : 16/05/2026
#
#######################################################################

import threading

def CheckPrime(no):
    if no <= 1:
        return False
    
    for i in range(2, int(no**0.5)+1):
        if(no % i) == 0:
            return False
    return True

def Prime(List):
    PrimeNumbers = []

    for no in List:
        if CheckPrime(no):
            PrimeNumbers.append(no)

    print(f"Thread Name : {threading.current_thread().name}")
    print(f"Prime number from the list are : {PrimeNumbers}")

def NonPrime(List):
    NonPrimeNumbers = []

    for no in List:
        if not CheckPrime(no):
            NonPrimeNumbers.append(no)

    print(f"Thread Name : {threading.current_thread().name}")
    print(f"Non prime number from the list are : {NonPrimeNumbers}")

def main():
    print("Enter the number of elements : ")
    size = int(input())

    Data = []

    print("Enter the elements : ")
    for i in range(size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=Prime,args=(Data,),name="Prime")

    t2 = threading.Thread(target=NonPrime,args=(Data,),name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()