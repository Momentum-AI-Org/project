from utils.constants import THIS_IS_A_CONSTANT
class Thing():
    def __init__(self, a, b, c=5, d=5) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = THIS_IS_A_CONSTANT
    
if __name__ == "__main__":
    x = Thing(1, 2)
    print(
        x.a,
        x.b,
        x.c,
        x.d,
        x.d
    )