import threading
import time
import datetime as dt 

def task1():
    for i in range(0, 100):
        time_now = dt.datetime.utcnow()
        color = "\033[92m"
        default_color = "\033[00m"
        print(f'{time_now} :{color} Working on the First Task {default_color}')
        time.sleep(1)

def task2():
    for i in range(0, 100):
        time_now = dt.datetime.utcnow()
        color = "\033[94m"
        default_color = "\033[00m"
        print(f'{time_now} :{color} Working on the Second Task {default_color}')
        time.sleep(1)

# step1: define target(function)
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# step2: start thread
thread1.start()
thread2.start()