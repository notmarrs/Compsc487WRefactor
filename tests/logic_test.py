import logic import LogicGate, AndGate, OrGate, UnaryGate, NotGate, XORGate
import unittest

class TestLogicGates(unittest.TestCase):
    def test_one_bit_adder(self):
        # Testing loop for one-bit adder
        one_bit_adder_tests()

    def test_eight_bit_adder(self):
        # Testing for eight-bit adder
        input1 = "10101010"
        input2 = "01010101"
        output = eight_bit_adder(input1, input2)
        self.assertIsNotNone(output)
        print(output)

        input1 = "00000001"
        input2 = "01111111"
        output = eight_bit_adder(input1, input2)
        self.assertIsNotNone(output)
        print(output)
