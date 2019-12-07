class Machine():
    def __init__(self, tape, instream):
        self.tape = tape
        self.input = instream
        self.ip = 0

    @property
    def code(self):
        return self.tape[self.ip] % 100

    @property
    def flags(self):
        return self.tape[self.ip] // 10

    def get(self, offset):
        ans = self.tape[self.ip + offset]
        if (self.flags // (10 ** offset)) % 10 == 0:
            ans = self.tape[ans]
        return ans

    def put(self, offset, val):
        self.tape[self.tape[self.ip + offset]] = val

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
                self.put(1, self.input.pop(0))
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
            else:
                raise RuntimeError("Invalid opcode: %d" % self.tape[self.ip])

