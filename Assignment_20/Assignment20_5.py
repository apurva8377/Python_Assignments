######################################################################################################
#
#   Program Name   : Assignment20_5.py
#   Author         : Apurva Vials Shinde
#   Description    :Design a Python application that creates two threads named Thread1 and Thread2.
#   •Thread1 should display numbers from 1 to 50.
#   . Thread2 should display numbers from 50 to 1 in reverse order.
#   •Ensure that:
#       ◦ Use appropriate thread synchronizatio
#       . Thread2 starts execution only after Thread1 has completed.
#   Date           : 16/05/2026
#
#######################################################################################################

import threading

def Display():
    for i in range(1,51):
        print(i)

def DisplayReverse():
    for i in range(50,0,-1):
        print(i)

def main():
    Thread1 = threading.Thread(target=Display,name="DisplayDigits")

    Thread2 = threading.Thread(target=DisplayReverse, name="DisplayReverse")

    Thread1.start()
    Thread1.join()
    
    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()