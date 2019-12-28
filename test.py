from __future__ import annotations

from datetime import date




class A:
    i: int

    def __init__(self):
        self.i = 12

    def JU(self)->A:
         return self

if __name__ == '__main__':
    a = A()
    b = A()
    print(A().JU().i)
