import threading

class Adder(threading.Thread):
    # TODO: implement the constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    # TODO: Implement the run method
    def run(self):
        sum = self.num1 + self.num2
        print(sum)


class Client:
    @staticmethod
    def main():
        # take input from the user
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # TODO: create a thread of Adder class and add num1 and num2
        
        # create adder object
        adder = Adder(num1,num2)

        # create the thread
        t1 = threading.Thread(target=adder.run)
        
        # start the thread 
        t1.start()

        # wait for the thread
        t1.join()
