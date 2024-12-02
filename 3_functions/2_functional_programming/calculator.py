def zero(op=None): return op(0) if op else 0
def one(op=None): return op(1) if op else 1
def two(op=None): return op(2) if op else 2
def three(op=None): return op(3) if op else 3
def four(op=None): return op(4) if op else 4
def five(op=None): return op(5) if op else 5
def six(op=None): return op(6) if op else 6
def seven(op=None): return op(7) if op else 7
def eight(op=None): return op(8) if op else 8
def nine(op=None): return op(9) if op else 9

def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y
