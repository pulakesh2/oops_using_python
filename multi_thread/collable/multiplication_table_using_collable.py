import threading


# Complete the implementation of the TableCreator class below

class TableCreator(threading.Thread):
    def __init__(self, num):
        # Initialize the threading.Thread superclass and set up any necessary attributes
        self.multiply = num


    def run(self):
        # Implement the logic to print the multiplication table for self.num, from 1 to 10
        # Each line should follow the format: "<num> times <i> is <result>"
        # TODO: Complete the run method
        for i in range(1, 11):
            print(f"{self.multiply} times {i} is {self.multiply * i}")


class Client:
    @staticmethod
    def main():
        n = int(input("Enter a number: "))

        threads = []
        for i in range(1, n + 1):
            thread = TableCreator(i)
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
