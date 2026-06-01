from concurrent.futures import ThreadPoolExecutor
import threading

# create client class
class Client:

    # take array as input
    def __init__(self, array):
        self.array_list = array

    # callable method to print the array
    def __call__(self):
        for number in self.array_list:
            print(f"number: {number} || thread : {threading.current_thread().name}")
    

# create array creator class
class Array_creator:
    # take size of array as input
    def __init__(self,size):
        self.size = size
    

    # callable method to create the array
    def __call__(self):
        return [i for i in range(self.size)]
    

# main method
if __name__ == "__main__":

    # create the array creator object and submit it to the thread pool executor
    array_creator_obj = Array_creator(10)
    with ThreadPoolExecutor() as executor:
        future = executor.submit(array_creator_obj)

    # get the future result which is the array created by the array creator class
    future_array = future.result()

    # create the client object and submit it to the thread pool executor
    client_obj = Client(future_array)
    with ThreadPoolExecutor() as executor:
        future_c = executor.submit(client_obj)

    
    # get the future result which is the client object that prints the array
    future_client = future_c.result()


    # print the future client object 
    print(future_client)