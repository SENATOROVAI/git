import unittest

from code_1 import generateReport


class Test1(unittest.TestCase):

    def test_1(self):
        x_list = [
            -1,
            1
        ]
        report = generateReport(x_list)
        
        self.assertEqual(len(report), 2)
        self.assertEqual(report[0], False)
        self.assertEqual(report[1], True)


if __name__ == '__main__':
    unittest.main()