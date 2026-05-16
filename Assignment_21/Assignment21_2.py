########################################################################
#
#   Program Name   : Assignment21_2.py
#   Author         : Apurva Vials Shinde
#   Description    : Design a Python application that creates two threads.
#        •Thread 1 should calculate and display the maximum element from an list.
#        •Thread 2 should calculate and display the minimum element from the same list.
#        •The list should be accepted from the user.       
#   Date           : 16/05/2026
#
#######################################################################

import threading

def Maximum(List):
    Max = List[0]

    for i in range(len(List)):
        if(List[i] > Max):
            Max = List[i]

    print(f"Thread Name : {threading.current_thread().name}")
    print(f"The maximum element from the list is : {Max}")

def Minimum(List):
    Min = List[0]

    for i in range(len(List)):
        if(List[i] < Min):
            Min = List[i]

    print(f"Thread Name : {threading.current_thread().name}")
    print(f"The minimum element from the list is : {Min}")
    
def main():
    print("Enter the number of elements : ")
    Size = int(input())

    Data = []

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=Maximum, args=(Data,), name="Maximum")

    t2 = threading.Thread(target=Minimum, args=(Data,), name="Minimum")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()