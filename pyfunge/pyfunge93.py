import sys
import random


class Befunge:
    sx = 80
    sy = 25
    
    def __init__(self, source):
        self.x = 0
        self.y = 0
        self.data = []
        for line in source.splitlines()[0:Befunge.sy]:
            self.data.append(list(line)[0:Befunge.sx])
        while len(self.data) < Befunge.sy:
            self.data.append([])
        for line in self.data:
            while len(line) < Befunge.sx:
                line.append("")

    def move(self, d):
        if d == ">": self.x = (self.x + Befunge.sx + 1) % Befunge.sx
        elif d == "v": self.y = (self.y + Befunge.sy + 1) % Befunge.sy
        elif d == "<": self.x = (self.x + Befunge.sx - 1) % Befunge.sx
        elif d == "^": self.y = (self.y + Befunge.sy - 1) % Befunge.sy

    def setAt(self, x, y, v): self.data[y][x] = v
    def getAt(self, x, y): return self.data[y][x]
    def get(self): return self.getAt(self.x, self.y)    


def run(bf):
    d = ">"
    s = []
    sm = False
    while True:
        c = bf.get()

        if sm:
            if c == "\"": sm = False
            else: s.append(ord(c))
        else:

            # print([x, y, c, s])
            # flow
            if c == "@":
                print()
                hr()
                print("Stack")
                print(s)
                exit()
            elif c == "#": bf.move(d)
            elif c == "!":
                if s.pop() == 0: s.append(1)
                else: s.append(0)
            elif c == "`":
                if s.pop() < s.pop(): s.append(1)
                else: s.append(0)
            elif c == "_":
                if s.pop() == 0: d = ">"
                else: d = "<"
            elif c == "|":
                if s.pop() == 0: d = "v"
                else: d = "^"
            # movement
            elif c == ">": d = c
            elif c == "v": d = c
            elif c == "<": d = c
            elif c == "^": d = c
            elif c == "?":
                a = list(">v<^")
                random.shuffle(a)
                d = a[0]
            # data
            elif c == "0": s.append(0)
            elif c == "1": s.append(1)
            elif c == "2": s.append(2)
            elif c == "3": s.append(3)
            elif c == "4": s.append(4)
            elif c == "5": s.append(5)
            elif c == "6": s.append(6)
            elif c == "7": s.append(7)
            elif c == "8": s.append(8)
            elif c == "9": s.append(9)
            elif c == "\"": sm = True
            # math
            elif c == "+": s.append(s.pop()+s.pop())
            elif c == "-":
                a = s.pop()
                s.append(s.pop()-a)
            elif c == "*": s.append(s.pop()*s.pop())
            elif c == "/":
                a = s.pop()
                s.append(s.pop()//a)
            elif c == "%":
                a = s.pop()
                s.append(s.pop()%a)
            # stack
            elif c == ":": s.append(s[-1])
            elif c == "\\":
                a = s.pop()
                b = s.pop()
                s.append(a)
                s.append(b)
            elif c == "$": s.pop()
            elif c == ".": print(s.pop(), end=" ")
            elif c == ",": print(chr(s.pop()), end="")
            # I/O
            elif c == "g":
                v = s.pop()
                u = s.pop()
                w = bf.get(u, v)
                if ord("0")<=ord(w) and ord(w)<=ord("9"): s.append(int(w))
                else: s.append(ord(w))
            elif c == "p":
                v = s.pop()
                u = s.pop()
                w = s.pop()
                if 0<=w and w<=9:
                    bf.setAt(u, v, ascii(w))
                else:
                    bf.setAt(u, v, chr(w))

        bf.move(d)
        
    
def show(source):
    print("\n".join(["".join(x) for x in source]))

def hr():
    print(80*"-")
    
if __name__ == "__main__":
    src = []
    with open(sys.argv[1]) as f:
        bf = Befunge(f.read())

    show(bf.data)
    hr()
    run(bf)
