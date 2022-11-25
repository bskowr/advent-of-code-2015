import unittest
from day_1_solution import Day1


class TestDay1(unittest.TestCase):
    def test_task_1(self):
        day_1 = Day1(file_input='test_input.txt', output_file_task_1='task_1_test_output.txt')
        expected_output = []
        with open('task_1_test_output_expected.txt', 'r') as file:
            for line in file:
                expected_output.append(int(line))
        program_output = day_1.solve_task_1()
        self.assertEqual(expected_output, program_output)
        day_1.write_task_1()

    def test_task_2(self):
        day_1 = Day1(file_input='test_input.txt', output_file_task_2='task_2_test_output.txt')
        expected_output = []
        with open('task_2_test_output_expected.txt', 'r') as file:
            for line in file:
                expected_output.append(int(line))
        program_output = day_1.solve_task_2()
        self.assertEqual(expected_output, program_output)
        day_1.write_task_2()


if __name__ == '__main__':
    TestDay1().test_task_1()
    TestDay1().test_task_2()
