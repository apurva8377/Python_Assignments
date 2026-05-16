########################################################################
#
#   Program Name   : Assignment19_1.py
#   Author         : Apurva Vials Shinde
#   Description    : Design a Python application that creates two separate threads named Even and Odd.
#        •The Even thread should display the rst 10 even numbers.
#        •The Odd thread should display the rst 10 odd numbers.
#        •Both threads should execute independently using the threading module.
#        •Ensure proper thread creation and execution.        
#   Date           : 12/05/2026
#
#######################################################################

import threading

lobj = threading.Lock()

def DisplyEven():
    print("Even Thread has started...")
    for i in range(1,11):
        print(f"Even number : {i * 2}")

def DisplayOdd():
    print("Odd Thread has started...")
    for i in range(1,11):
        print(f"Odd number : {(i * 2) - 1}")

def main():
    print("Main Thread started...\n")

    t1 = threading.Thread(target=DisplyEven, name="Even")
    t2 = threading.Thread(target=DisplayOdd, name="Odd")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Main Thread finished execution")

if __name__ == "__main__":
    main()