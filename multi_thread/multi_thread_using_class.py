import threading
from abc import ABC, abstractmethod
from threading import Thread

# create an interface
class Runnable(ABC):
    @abstractmethod
    def run(self):
        pass


# create the Task class
class Task(Runnable):
    def __init__(self, num):
        self.num = num

    def run(self):
        print(f"running task: {self.num} || thread : {threading.current_thread().name}")


if __name__ == "__main__":
    # create the task
    task1 = Task(1)
    task2 = Task(2)

    # create the thread
    t1 = Thread(target=task1.run)
    t2 = Thread(target=task2.run)

    # start the thread
    t1.start()
    t2.start()

    # end the thread
    t1.join()
    t2.join()

    print('done with thread')
