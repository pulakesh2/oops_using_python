import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        # Initialize semaphores here
        self.zero_sem = threading.Semaphore(1)
        self.even_sem = threading.Semaphore(0)
        self.odd_sem = threading.Semaphore(0)

    def zero(self, printNumber):
        # TODO: Implement the method to print "0" followed by releasing either even_sem or odd_sem
        for i in range(1, self.n + 1):
            self.zero_sem.acquire()
            printNumber.accept(0)
            if i % 2 == 0:
                self.even_sem.release()
            else:
                self.odd_sem.release() 
            

    def even(self, printNumber):
        # TODO: Implement the method to print even numbers and release zero_sem afterwards
        for i in range(2, self.n + 1, 2):
            self.even_sem.acquire()
            printNumber.accept(i)
            self.zero_sem.release()

    def odd(self, printNumber):
        # TODO: Implement the method to print odd numbers and release zero_sem afterwards
        for i in range(1, self.n + 1, 2):
            self.odd_sem.acquire()
            printNumber.accept(i)
            self.zero_sem.release()


class PrintNumber:
    def accept(self, x):
        print(x, end='')


def test_zero_even_odd():
    n = 8
    zeo = ZeroEvenOdd(n)
    pn = PrintNumber()

    threads = [threading.Thread(target=zeo.zero, args=(pn,)), threading.Thread(target=zeo.even, args=(pn,)),
               threading.Thread(target=zeo.odd, args=(pn,))]

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    test_zero_even_odd()
