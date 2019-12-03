from advent_of_code.utils import load_input, save_answers

# Intcode - comma-separated values for a program
# opcode - program to run (position 0)

def part1():
    # Initial memory state
    # It's position in memory is the `address`, each item in memory has an address as well
    input = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 13, 19, 2, 9, 19, 23, 1, 23, 6, 27, 1, 13, 27, 31, 1, 31, 10, 35, 1, 9, 35, 39, 1, 39, 9, 43, 2, 6, 43, 47, 1, 47, 5, 51, 2, 10, 51, 55, 1, 6, 55, 59, 2, 13, 59, 63, 2, 13, 63, 67, 1, 6, 67, 71, 1, 71, 5,
             75, 2, 75, 6, 79, 1, 5, 79, 83, 1, 83, 6, 87, 2, 10, 87, 91, 1, 9, 91, 95, 1, 6, 95, 99, 1, 99, 6, 103, 2, 103, 9, 107, 2, 107, 10, 111, 1, 5, 111, 115, 1, 115, 6, 119, 2, 6, 119, 123, 1, 10, 123, 127, 1, 127, 5, 131, 1, 131, 2, 135, 1, 135, 5, 0, 99, 2, 0, 14, 0]

    # input = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    def chunks(list, size):
        for i in range(0, len(input), size):
            yield input[i:size+i]
    
    program_functions = list(chunks(input, 4))

    # Each four-digit list is an `instruction`
    # The opcode is the first item in an instruction
    # Items 2,3,4 (if any) are `parameters`
    # opcode 99 has no parameters
    # The address of an instruction is the `instruction pointer`
    # The instruction pointer increases by the number of values in the instruction
    for func in program_functions:
        # print(f'Current function: {func}')
        op = func[0]

        if op == 1:
            # Increate instruction pointer by 4
            sum = input[func[1]] + input[func[2]]
            # print(f'Changing position {func[3]} to {sum}')
            input[func[3]] = sum
        elif op == 2:
            # Increase instruction pointer by 4
            prod = input[func[1]] * input[func[2]]
            # print(f'Changing position {input[func[3]]} to {prod}')
            input[func[3]] = prod
        elif op == 99:
            # Would increase instruction pointer by 1, but HALTS
            return input[0]

    return "Challenge not solved"


def part2():
    # What pair of outputs produces 19690720?
    
    input = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 13, 19, 2, 9, 19, 23, 1, 23, 6, 27, 1, 13, 27, 31, 1, 31, 10, 35, 1, 9, 35, 39, 1, 39, 9, 43, 2, 6, 43, 47, 1, 47, 5, 51, 2, 10, 51, 55, 1, 6, 55, 59, 2, 13, 59, 63, 2, 13, 63, 67, 1, 6, 67, 71, 1, 71, 5,
                75, 2, 75, 6, 79, 1, 5, 79, 83, 1, 83, 6, 87, 2, 10, 87, 91, 1, 9, 91, 95, 1, 6, 95, 99, 1, 99, 6, 103, 2, 103, 9, 107, 2, 107, 10, 111, 1, 5, 111, 115, 1, 115, 6, 119, 2, 6, 119, 123, 1, 10, 123, 127, 1, 127, 5, 131, 1, 131, 2, 135, 1, 135, 5, 0, 99, 2, 0, 14, 0]

    def intcode(program, index = 0):
        opcode = program[index]
        if opcode == 99:
            return program[0]
        param_1 = program[index + 1]
        param_2 = program[index + 2]
        answer = program[index + 3]

        if opcode == 1:
            program[answer] = program[param_1] + program[param_2]
            index += 4
            return intcode(program, index)
        elif opcode == 2:
            program[answer] = program[param_1] * program[param_2]
            index += 4
            return intcode(program, index)

    def set_intcode(program, noun, verb):
        program_copy = program.copy()
        program_copy[1] = noun
        program_copy[2] = verb
        return intcode(program_copy)

    for i in range(100):
        for j in range(100):
            output = set_intcode(input, i, j)
            if output == 19690720:
                return 100 * i + j

    return "Challenge not solved"


if __name__ == "__main__":
    answer1 = part1()
    answer2 = part2()
    print(f"Day 2 - Part 1 Answer: {answer1}")
    print(f"Day 2 - Part 2 Answer: {answer2}")
    save_answers(answer1, 2, 1)
    save_answers(answer2, 2, 2)
