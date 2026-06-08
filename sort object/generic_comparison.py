from typing import TypeVar, Callable

T = TypeVar('T')

def compare(x: T, y: T, key: Callable[[T], any] = None) -> int:
    """
    Compare two objects of the same type.

    Args:
        x (T): The first object to compare.
        y (T): The second object to compare.
        key (Callable[[T], any], optional): A function to extract a key from each object for comparison.
            Defaults to None, which means direct comparison of objects.

    Returns:
        int: -1 if x < y, 0 if x == y, 1 if x > y.
    """
    if key is not None:
        #todo
        if x[key] < y[key]:
            return -1
        elif x[key] > y[key]:
            return 1
        else:
            return 0
        
    else:
        #todo
        if x < y:
            return -1
        elif x > y:
            return 1
        else:
            return 0


# Example usage:

# Direct comparison
print(compare(5, 10))  # Output: -1
print(compare("abc", "abc"))  # Output: 0
print(compare(20, 10))  # Output: 1


# Comparison with key function
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

# Sort students by age
sorted_students = sorted(students, key=lambda x: x['age'])
print(sorted_students)  # Output: [{'name': 'Charlie', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]