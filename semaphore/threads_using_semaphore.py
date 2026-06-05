import threading

semaphore = threading.Semaphore(2)  # Initialize a semaphore with a count of 2

def task(name):
    print(f"Thread {name} is waiting")

    with semaphore:  
        print(f"Thread {name} is entered the critical section")
        print(f"Thread {name} is leaving the critical section")
    

if __name__ == "__main__":
    threads = []

    for i in range(1,6):
        t = threading.Thread(target = task, args=(i,))
        threads.append(t)
        t.start() 

    for t in threads:
        t.join() 

