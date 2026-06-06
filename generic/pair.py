from typing import Generic, TypeVar


T = TypeVar("T")
V = TypeVar("V")


class Pair(Generic[T,V]):
    def __init__(self, first:T, second:V):
        self.first = first
        self.second = second

    def set_first(self, first:T)->None:
        self.first = first
    
    def get_first(self) -> T:
        return self.first
    
    def set_second(self, second:V) -> None:
        self.second = second

    def get_second(self) -> V:
        return self.second
    

if __name__ == "__main__":

    student = Pair[str,int]("pulakesh", 2522302)
    coordinates = Pair[float,float](12, 45)
    credentials = Pair[str, str]("pulakesh", "pass123")

    print(student.get_first(), student.get_second())
    print(coordinates.get_first(), coordinates.get_second())
    print(credentials.get_first(), credentials.get_second())

    
    