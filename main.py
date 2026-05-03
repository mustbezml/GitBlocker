
from enum import Enum

class t(Enum):
    A = 4
    B = 5
    C = 6

    def a():
        return t.__members__
    
print(type(t.a()['B']))