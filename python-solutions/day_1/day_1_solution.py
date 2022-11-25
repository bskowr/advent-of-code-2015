class Day1:
    def __init__(self, input=None, file_input=None,
                 output_file_task_1=None, output_file_task_2=None, ):
        if input is not None:
            self.input = input
        elif file_input is not None:
            self.input = self.__read_input(file_input)
        else:
            self.input = self.__read_input('input.txt')

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
        for line in self.input:
            result.append(line.count('(') - line.count(')'))
        return result

    def print_task_1(self):
        for i, result in enumerate(self.solve_task_1()):
            print(f'Line {i}: {result}')

    def write_task_1(self):
        with open(self.output_file_task_1, 'w') as output_file:
            for result in self.solve_task_1():
                output_file.write(f'{result}\n')

    def solve_task_2(self):
        result = []
        for line in self.input:
            result.append(0)
            floor = 0
            for i, instruction in enumerate(line.strip()):
                if instruction == '(':
                    floor += 1
                elif instruction == ')':
                    floor -= 1
                if floor < 0:
                    result[len(result) - 1] = (i+1)
                    break
        return result

    def print_task_2(self):
        for i, result in enumerate(self.solve_task_2()):
            print(f'Line {i}: {result}')

    def write_task_2(self):
        with open(self.output_file_task_2, 'w') as output_file:
            for result in self.solve_task_2():
                output_file.write(f'{result}\n')


if __name__ == '__main__':
    day_1 = Day1()
    day_1.print_task_1()
    day_1.write_task_1()
    day_1.print_task_2()
    day_1.write_task_2()
