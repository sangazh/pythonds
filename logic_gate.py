# 1.13
class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a is None:
            return int(input("Enter Pin A input for gate " + self.get_label() + " --> "))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b is None:
            return int(input("Enter Pin B input for gate " + self.get_label() + " --> "))
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        else:
            if self.pin_b is None:
                self.pin_b = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.get_label() + " --> "))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


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


class XorGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == b:
            return 0
        else:
            return 1


class NandGate(AndGate):
    def __init__(self, n):
        AndGate.__init__(self, n)

    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1


class NorGate(OrGate):
    def __init__(self, n):
        OrGate.__init__(self, n)

    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin()
        if a == 0:
            return 1
        else:
            return 0


class Wire:
    def __init__(self, pin):
        self.pin = pin

    def perform_gate_logic(self):
        return self.pin

    def get_output(self):
        return self.pin


class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate
        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


class HalfAdder:
    def __init__(self, a, b):
        self.input_a = a
        self.input_b = b
        self.output_catch = 0
        self.output_sum = 0
        self.connect()

    def get_output_catch(self):
        return self.output_catch

    def get_output_sum(self):
        return self.output_sum

    def connect(self):
        w1 = Wire(self.input_a)
        w2 = Wire(self.input_b)

        g1 = OrGate("G1")
        g2 = AndGate("G2")

        c1 = Connector(w1, g1)
        c2 = Connector(w1, g2)
        c3 = Connector(w2, g1)
        c4 = Connector(w2, g2)

        g3 = NotGate("G3")
        c5 = Connector(g2, g3)

        g4 = AndGate("G4")
        c6 = Connector(g1, g4)
        c7 = Connector(g3, g4)

        self.output_sum = g4.get_output()
        self.output_catch = g2.get_output()


class FullAdder:
    def __init__(self, a, b, c_in):
        self.input_a = a
        self.input_b = b
        self.input_catch = c_in
        self.output_sum = 0
        self.output_catch = 0
        self.connect()

    def connect(self):
        h1 = HalfAdder(self.input_b, self.input_catch)
        h1_sum = h1.get_output_sum()
        h1_catch = h1.get_output_catch()

        h2 = HalfAdder(self.input_a, h1_sum)
        h2_catch = h2.get_output_catch()
        self.output_sum = h2.get_output_sum()

        g1 = OrGate("G1")
        w1 = Wire(h1_catch)
        w2 = Wire(h2_catch)
        Connector(w1, g1)
        Connector(w2, g1)
        self.output_catch = g1.get_output()

    def get_output_catch(self):
        return self.output_catch

    def get_output_sum(self):
        return self.output_sum


def main1():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())
    # =g1 -> c1 \
    #            g3 -> c3 -> g4 --
    # =g2 -> c2 /


def main2():
    # exercise
    # g1 = Nor(and(a,b), and(c,d))
    # g2 = and(nand(a,b), nand(c,d))
    # a = 1
    # b = 1
    # c = 0
    # d = 1
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = NorGate("G3")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    result1 = g3.get_output()

    g4 = NandGate("G4")
    g5 = NandGate("G5")
    g6 = AndGate("G6")
    c3 = Connector(g4, g6)
    c4 = Connector(g5, g6)
    result2 = g6.get_output()

    return print("result1:%s, result2:%s, compare:%s" % (result1, result2, result1 == result2))


def main():
    a = HalfAdder(0, 0)
    print("sum:%s, catch:%s" % (a.get_output_sum(), a.get_output_catch()))

    f = FullAdder(0, 0, 1)
    print("sum:%s, catch:%s" % (f.get_output_sum(), f.get_output_catch()))


main()
