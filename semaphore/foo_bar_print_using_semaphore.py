import threading


class FooBar:
    def __init__(self, n):
        # TODO: Initialize semaphores here
        self.n = n
        self.foo_sem = threading.Semaphore(1)
        self.bar_sem = threading.Semaphore(0)

    def foo(self):
        # TODO: Implement synchronization to ensure "foo" is printed before "bar"
        for _ in range(self.n):
            self.foo_sem.acquire()
            print("foo", end="")
            self.bar_sem.release()
            

    def bar(self):
        # TODO: Implement synchronization to ensure "bar" is printed after "foo"
        for _ in range(self.n):
            self.bar_sem.acquire()
            print("bar", end="")
            self.foo_sem.release()


def test_foobar():
    n = 5
    fb = FooBar(n)

    def foo():
        fb.foo()

    def bar():
        fb.bar()

    threads = [threading.Thread(target=foo), threading.Thread(target=bar)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    test_foobar()
