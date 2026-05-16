######################################################################################################
#
#   Program Name   : Assignment20_4.py
#   Author         : Apurva Vials Shinde
#   Description    :Design a Python application that creates three threads named Small, Capital, and Digits.
#   All threads should accept a string as input.
#   •The Small thread should count and display the number of lowercase characters.
#   •The Capital thread should count and display the number of uppercase characters.
#   •The Digits thread should count and display the number of numeric digits.
#   •Each thread must also display:
#       ◦Thread ID
#       ◦Thread Name     
#   Date           : 12/05/2026
#
#######################################################################################################

import threading

def small(StringData):
    Count = 0

    for char in StringData:
        if char.islower():
            Count = Count + 1

    print("-----------------------------------------------------------------")
    print(f"Thread Name = {threading.current_thread().name}")
    print(f"Thread ID  : {threading.get_ident()}")
    print(f"Number of lowercase characters are : {Count}")
    print("-----------------------------------------------------------------")

def Capital(StringData):
    Count = 0

    for char in StringData:
        if char.isupper():
            Count = Count + 1

    print("-----------------------------------------------------------------")
    print(f"Thread name : {threading.current_thread().name}")
    print(f"Thread ID : {threading.get_ident()}")
    print(f"Number of uppercase character are : {Count}")
    print("-----------------------------------------------------------------")

def Digits(StringData):
    Count = 0

    for char in StringData:
        if char.isdigit():
            Count = Count + 1

    print("-----------------------------------------------------------------")
    print(f"Thread Name : {threading.current_thread().name}")
    print(f"Thread ID : {threading.get_ident()}")
    print(f"The number of digits are : {Count}")
    print("-----------------------------------------------------------------")

def main():
    print("Enter the string : ")
    Data = input()

    t1 = threading.Thread(target=small, args=(Data,), name="Small")
    t2 = threading.Thread(target=Capital, args=(Data,), name="Capital")
    t3 = threading.Thread(target=Digits, args= (Data,) , name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()