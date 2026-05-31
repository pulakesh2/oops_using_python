import threading
from threading import Thread

# task1
def task1(name):
    print(f"threading name --> {threading.current_thread().name} || my name is {name}")

# task2
def task2(work):
    print(f"threading name --> {threading.current_thread().name} || my profession is {work}")


# create the thread
t1 = Thread(target=task1, args=('pulakesh',))
t2 = Thread(target=task2, args=('student',))

# start the threads
t1.start()
t2.start()

t1.join()
t2.join()