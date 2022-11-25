import unittest

class TestDay1(unittest.TestCase):
    day_1 = Day1('task-1-input-test', 'task-2-input-test.txt')
    def test_task_1(self):
        expected_output = []
        with open('task-1-test-output-expected.txt', 'r') as file:
            for line in file:
                expected_output.append(line.strip())
        program_output = self.day_1.solve_task_1()
        for expected_line, program_line  in zip(expected_output, program_output):
            self.assertEqual(expected_line, program_line)


if __name__ == '__main__':
    TestDay1.test_task_1()
