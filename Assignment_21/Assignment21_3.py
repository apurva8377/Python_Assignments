########################################################################
#
#   Program Name   : Assignment21_3.py
#   Author         : Apurva Vials Shinde
#   Description    : Design a Python application where multiple threads update a shared variable.
#        •Use a Lock to avoid race conditions.
#        •Each thread should increment the shared counter multiple times.
#        •Display the nal value of the counter after all threads complete execution.  
#   Date           : 16/05/2026
#
#######################################################################

import threading

Count = 0    # Shared global variable

Lock = threading.Lock()

def Increment(Steps):
    global Count

    for i in range(Steps):
        with Lock:
            Count = Count + 1

    print(f"Thread Name : {threading.current_thread().name}")

def main():
    global Count

    Steps = 100000

    print(f"Initial value of Counter : {Count}")

    t1 = threading.Thread(target=Increment, args=(Steps,), name="Thread1")
    t2 = threading.Thread(target=Increment, args=(Steps,), name="Thread2")
    t3 = threading.Thread(target=Increment, args=(Steps,), name="Thread3")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print(f"Expected final value : {Steps*3}")
    print(f"Actual final value of counter : {Count}")

if __name__ == "__main__":
    main()

