import math
import threading


# Todo: implement the factorial thread class
class FactorialThread(threading.Thread):
    # write code here
    def __init__(self, n):
        self.num = n
        self.result = None

    def run(self):
        self.result = math.factorial(self.num)

    



def compute_large_factorial(n):
    # Todo: Create a factorial thread
    fact = FactorialThread(n)
    
    # Todo: wait for calc to finish by calling the join method
    t1 = threading.Thread(target = fact.run)
    t1.start()
    t1.join()
    # Todo: return the result
    return fact.result
    

