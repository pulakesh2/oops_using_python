from concurrent.futures import ThreadPoolExecutor

# create merge sort using callable class
class merge_sort:

    # constructor:
    def __init__(self, arr, executor):
        self.arr = arr
        self.executor = executor
    
    # callable method:
    def __call__(self):

        # IF the length of the array is less than or equal to 1, return the array
        if len(self.arr) <= 1:
            return self.arr
        
        # find the middle length
        mid = len(self.arr) // 2

        # get the left array and the right array
        left = self.arr[:mid]
        right = self.arr[mid:]

        # submit left and right array to threads
        left_future = self.executor.submit(merge_sort(left, self.executor))
        right_future = self.executor.submit(merge_sort(right, self.executor))

        # get the results from the threads
        left_sorted = left_future.result()
        right_sorted = right_future.result()

        # merge the lists and return the result
        return self.merge(left_sorted, right_sorted)
    

    # merge function
    def merge(self, left, right):
        merged = []
        i = j = 0

        # merge the left and right arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
            
        # if there are remaining elements in the left or right array, add them to the merged array
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged
    

if __name__ == "__main__":
    # create a thread pool executor
    with ThreadPoolExecutor() as executor:
        # create an array to sort
        arr = [38, 27, 43, 3, 9, 82, 10]

        # create an instance of the merge_sort class and submit it to the executor
        future = executor.submit(merge_sort(arr, executor))

        # get the sorted array from the future
        sorted_arr = future.result()

        print("Sorted array:", sorted_arr)