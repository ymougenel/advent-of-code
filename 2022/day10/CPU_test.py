import unittest
import main
from CPU import CPU
class main_test(unittest.TestCase):

    def test_noop(self):
        cpu = CPU()
        cpu.run("noop", None)
        self.assertEqual(1, cpu.register)
        self.assertEqual(0, cpu.remaining_cycle)
        self.assertEqual(1, cpu.cycle)

    def test_addx(self):
        cpu = CPU()
        cpu.run("addx", 4)
        self.assertEqual(1, cpu.register)
        self.assertEqual(1, cpu.remaining_cycle)
        self.assertEqual(1, cpu.cycle)

        cpu.run("addx", 4)
        self.assertEqual(5, cpu.register)
        self.assertEqual(0, cpu.remaining_cycle)
        self.assertEqual(2, cpu.cycle)

        cpu.run("addx", -2)
        self.assertEqual(5, cpu.register)
        self.assertEqual(1, cpu.remaining_cycle)
        self.assertEqual(3, cpu.cycle)

        cpu.run("addx", -2)
        self.assertEqual(3, cpu.register)
        self.assertEqual(0, cpu.remaining_cycle)
        self.assertEqual(4, cpu.cycle)
if __name__ == '__main__':
    unittest.main()
