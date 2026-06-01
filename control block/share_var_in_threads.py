from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor
# import time

# shared variable in threads
class Shared_data:
    def __init__(self, value):
        self.value = value
        self.lock = Lock()



# adder class
class Adder:
    def __init__(self, shared_data):
        self.shared_data = shared_data

    def addder(self):
        with self.shared_data.lock:
             self.shared_data.value += 1
        # temp = self.shared_data.value
        # time.sleep(0.0001)
        # self.shared_data.value = temp + 1

# subtractor class
class Subtractor:
    def __init__(self, shared_data):
        self.shared_data = shared_data

    def subtractor(self):
        with self.shared_data.lock:
             self.shared_data.value -= 1
        # temp = self.shared_data.value
        # time.sleep(0.0001)
        # self.shared_data.value = temp - 1


if __name__ == "__main__":

    # create the share data object
    data = Shared_data(0)

    # create the adder and subtractor objects
    adder = Adder(data)
    subtractor = Subtractor(data)


    # create the thread pool executor and submit the tasks
    with ThreadPoolExecutor(max_workers=4) as executor:
        for _ in range(1000):
            executor.submit(adder.addder)
            executor.submit(subtractor.subtractor)

           

    
    # print the final value of the shared variable
    print("Final value of shared variable:", data.value)

    
