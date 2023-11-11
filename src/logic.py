class LogicGate:
    def __init__(self, n):
        self.name = n
        self.output = None

    def get_label(self):
        return self.name

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, n):
        super(BinaryGate, self).__init__(n)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a is None:
            return int(input("Enter Pin A input for gate " + self.get_label() + "-->"))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b is None:
            return int(input("Enter Pin B input for gate " + self.get_label() + "-->"))
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        else:
            if self.pin_b is None:
                self.pin_b = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.get_label() + "-->"))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1

class XORGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        return (a and not b) or (not (a and b))

class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate
        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate

def one_bit_adder_tests():
    c = 0
    for a in [0, 1]:
        for b in [0, 1]:
            c, s = adder(a, b, c)
            print(f"{a}+{b} = {c}{s}")

def eight_bit_adder(a, b, c=0):
    total = []
    reversed_a = list(reversed(a))
    reversed_b = list(reversed(b))
    for i in range(8):
        c, s = adder(int(reversed_a[i]), int(reversed_b[i]), c)
        total.insert(0, s)
    return c, total

def nth_bit_adder(a, b, c=0):
    total = []
    last = len(a)
    reversed_a = list(reversed(a))
    reversed_b = list(reversed(b))
    for i in range(last):
        c, s = adder(int(reversed_a[i]), int(reversed_b[i]), c)
        total.insert(0, s)
    return c, total