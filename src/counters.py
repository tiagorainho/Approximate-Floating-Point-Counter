
from math import floor
from random import random, randint

class Counter:
    x:int

    def __init__(self) -> None:
        self.x = 0

    def increment(self) -> None:
        self.x += 1
    
    @property
    def value(self) -> int:
        return self.x

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.value}'

class FixedProbabilityCounter(Counter):
    p:float
    x:int

    def __init__(self, p:float=1/64) -> None:
        self.x = 0
        self.p = p
    
    def increment(self) -> None:
        if random() < self.p:
            self.x += 1
    
    @property
    def value(self) -> int:
        return int(1/self.p * self.x)

class CsurosCounter(Counter):
    m:int
    x:int

    def __init__(self, d:int=2) -> None:
        self.x = 0
        self.m = 2**d

    def increment(self) -> None:
        t:int = floor(self.x/self.m)
        prob:float = (1/2)**(t)
        if random() < prob:
            self.x += 1
        # while t > 0:
        #     if randint(0,1) == 1: return
        #     t -= 1
        # self.x += 1
        
    
    @property
    def value(self) -> int:
        u = self.x%self.m
        return int(( self.m + u ) * ( 2**floor(self.x/self.m) ) - self.m)


if __name__ == '__main__':
    import time
    
    t1 = time.perf_counter()

    counter = CsurosCounter()
    for _ in range(1000000):
        counter.increment()
    
    t2 = time.perf_counter()
    print(f'{counter} in {round(t2-t1, 3)} seconds')