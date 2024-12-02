from typing import Generator, Iterable, TypeVar, Iterator

T = TypeVar("T")

def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    saved = list(obj)
    while saved:
        for element in saved:
            yield element

class Cycle:
    def __init__(self, obj: Iterable[T]):
        self.saved = list(obj)
        self.index = 0

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        if not self.saved:
            raise StopIteration
        result = self.saved[self.index]
        self.index = (self.index + 1) % len(self.saved)
        return result
