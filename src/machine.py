from collections import abc

class Machine():
    def __init__(self, tape, instream):
        self.tape = tape + [0] * 3000
        self.input = instream
        self.ip = 0
        self.rel = 0

        self.flag_table = [0] * 1000
        for i in range(1000):
            self.flag_table[i] = [0, i % 10, i // 10 % 10, i // 100]

    @property
    def code(self):
        return self.tape[self.ip] % 100

    @property
    def flags(self):
        return self.flag_table[self.tape[self.ip] // 100]

    def getinput(self):
        if isinstance(self.input, abc.Iterable):
            return self.input.pop(0)
        return self.input()

    def get(self, offset):
        ans = self.tape[self.ip + offset]
        if self.flags[offset] == 0:
            ans = self.tape[ans]
        elif self.flags[offset] == 2:
            ans = self.tape[ans + self.rel]
        return ans

    def put(self, offset, val):
        offset2 = self.tape[self.ip + offset]
        if self.flags[offset] == 0:
            self.tape[offset2] = val
        elif self.flags[offset] == 2:
            self.tape[offset2 + self.rel] = val
        else:
          raise RuntimeError("Can't use parameter mode 1 when writing stuff")

    def run(self):
        while True:
            if self.code == 99:
                break
            elif self.code == 1:
                self.put(3, self.get(1) + self.get(2))
                self.ip += 4
            elif self.code == 2:
                self.put(3, self.get(1) * self.get(2))
                self.ip += 4
            elif self.code == 3:
                self.put(1, self.getinput())
                self.ip += 2
            elif self.code == 4:
                yield self.get(1)
                self.ip += 2
            elif self.code == 5:
                if self.get(1): self.ip = self.get(2)
                else: self.ip += 3
            elif self.code == 6:
                if not self.get(1): self.ip = self.get(2)
                else: self.ip += 3
            elif self.code == 7:
                self.put(3, self.get(1) < self.get(2))
                self.ip += 4
            elif self.code == 8:
                self.put(3, self.get(1) == self.get(2))
                self.ip += 4
            elif self.code == 9:
                self.rel += self.get(1)
                self.ip += 2
            else:
                raise RuntimeError("Invalid opcode: %d" % self.tape[self.ip])

