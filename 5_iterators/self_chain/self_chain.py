from typing import Generator, Iterable, TypeVar, Iterator

T = TypeVar("T")

def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    for iterable in iterables:
        for element in iterable:
            yield element

class Chain:
    def __init__(self, *iterables: Iterable[T]):
        self.iterables = iterables
        self.current_iter = iter(self.iterables)
        self.current = None
        self._advance_iterable()

    def _advance_iterable(self):
        try:
            self.current = iter(next(self.current_iter))
        except StopIteration:
            self.current = None

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        if self.current is None:
            raise StopIteration
        try:
            return next(self.current)
        except StopIteration:
            self._advance_iterable()
            return self.__next__()
