from typing import Generator, Iterable, TypeVar, Iterator, Tuple

T = TypeVar("T")

def batched(obj: Iterable[T], n: int) -> Generator[Tuple[T, ...], None, None]:
    it = iter(obj)
    while True:
        batch = tuple(next(it, None) for _ in range(n))
        if not batch or batch == (None,) * n:
            break
        yield batch[:len(batch) - batch.count(None)]

class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        self.obj = iter(obj)
        self.n = n

    def __iter__(self) -> Iterator[Tuple[T, ...]]:
        return self

    def __next__(self) -> Tuple[T, ...]:
        batch = tuple(next(self.obj, None) for _ in range(self.n))
        if not batch or batch == (None,) * self.n:
            raise StopIteration
        return batch[:len(batch) - batch.count(None)]
