
from concurrent.futures import ThreadPoolExecutor
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
    # create fixed thread pool
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(1,101):
            t = Task(i)
            executor.submit(t.run)

    print('done with thread')
