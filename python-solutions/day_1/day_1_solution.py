class Day1:
    def __init__(self, input_task_1=None, file_task_1=None, input_task_2=None, file_task_2=None,
                 output_file_task_1=None, output_file_task_2=None, ):
        if input_task_1 is not None:
            self.input_task_1 = input_task_1
        elif file_task_1 is not None:
            self.input_task_1 = self.__read_input(file_task_1)
        else:
            self.input_task_1 = self.__read_input('task_1_input.txt')

        if input_task_2 is not None:
            self.input_task_2 = input_task_2
        elif file_task_2 is not None:
            self.input_task_2 = self.__read_input(file_task_2)
        else:
            self.input_task_2 = self.__read_input('task_2_input.txt')

        if output_file_task_1 is None:
            self.output_file_task_1 = 'task_1_output.txt'
        else:
            self.output_file_task_1 = output_file_task_1

        if output_file_task_2 is None:
            self.output_file_task_2 = 'task_2_output.txt'
        else:
            self.output_file_task_2 = output_file_task_2

    @staticmethod
    def __read_input(input_file_path):
        with open(input_file_path, 'r') as source_file:
            return source_file.readlines()

    def solve_task_1(self):
        result = []
        for i, line in enumerate(self.input_task_1):
            result.append(line.count('(') - line.count(')'))
        return result

    def print_task_1(self):
        for i, result in enumerate(self.solve_task_1()):
            print(f'Line {i}: {result}')

    def write_task_1(self):
        with open(self.output_file_task_1, 'w') as output_file:
            for i, result in enumerate(self.solve_task_1()):
                output_file.write(f'{result}\n')


if __name__ == '__main__':
    Day1().print_task_1()
    Day1().write_task_1()
