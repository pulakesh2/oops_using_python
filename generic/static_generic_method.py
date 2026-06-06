from typing import TypeVar, Generic

# create type variables
T = TypeVar('T')
X = TypeVar('X')
Y = TypeVar('Y')


# create Pair class
class Pair(Generic[X,Y]):
    def __init__(self, first:X, second:Y) -> None:
        self.first = first
        self.second = second
    
    def get_first(self) -> X:
        return self.first

    def set_first(self, value:X) -> None:
        self.first = value

    def get_second(self) -> Y:
        return self.second

    def set_second(self, value:Y) -> None:
        self.second = value


# create a Utlity class with static generic methods
class Utility(Generic[T]):
    @staticmethod
    def print_array(arr:list[T]) -> None:
        for item in arr:
            print(item)

    @staticmethod
    def get_first(arr:list[T]) -> T:
        return arr[0]
    
    @staticmethod
    def new_pair(first:T, second:X) -> Pair[T,X]:
        return Pair(first, second)
    
    



if __name__ == "__main__":

    # create a list of names and scores
    names:list[str] = ["sunny", "mia", "aubree", "sara","kendall"]
    scores:list[int] = [90, 85, 88, 92, 80]


    # print the names and scores using the static generic method
    Utility.print_array(names)
    Utility.print_array(scores)


    # get the first name and score using the static generic method 
    first_name: str = Utility.get_first(names)
    first_score: int = Utility.get_first(scores)


    # print the first name and score
    print(f"First name: {first_name}")
    print(f"First score: {first_score}")


    # create a new pair of name and score using the static generic method
    student: Pair[str, int] = Utility.new_pair("sunny", 95)
    student.set_first("mia")
    print(f"Student Name: {student.get_first()}, Student Score: {student.get_second()}")

