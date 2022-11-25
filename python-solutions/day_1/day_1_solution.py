class Day1:
    def __init__(self, input_task_1=None, file_task_1=None, input_task_2=None, file_task_2=None):
        if input_task_1 is not None:
            self.input_task_1 = input_task_1
        elif file_task_1 is not None:
            self.input_task_1 = self.__read_input(file_task_1)
        else:
            self.input_task_1 = self.__read_input('task-1-input.txt')

        if input_task_2 is not None:
            self.input_task_2 = input_task_2
        elif file_task_2 is not None:
            self.input_task_2 = self.__read_input(file_task_2)
        else:
            self.input_task_2 = self.__read_input('task-2-input.txt')


    @staticmethod
    def __read_input(input_file_path):
        return open(input_file_path, 'r').readlines()

    def solve_task_1(self):
        result = {}
        for i, line in enumerate(self.input_task_1):
            result[i] = line.count('(') - line.count(')')
        return result

    def print_task_1(self):
        for line, result in self.solve_task_1().items():
            print(f'Line {line}: {result}')


if __name__ == '__main__':
    Day1().print_task_1()
