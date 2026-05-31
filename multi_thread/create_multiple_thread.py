from multiprocessing import Process, current_process
from threading import Thread
from abc import ABC, abstractmethod

class Runnable(ABC):
    @abstractmethod
    def run(self):
        pass


class Task(Runnable):
    def __init__(self, num):
        self.num = num

    def run(self):
        print(f"number : {self.num} task : {current_process().name}")


if __name__ == "__main__":
    for i in range(1,101):
        # create task
        task = Task(i)

        # create thread
        t = Process(target=task.run)

        # run the thread
        t.start()

