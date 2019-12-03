from advent_of_code.utils import load_input, save_answers

# Intcode - comma-separated values for a program
# opcode - program to run (position 0)

def part1():
    # input = load_input(2)[0].split(',')
    input = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 13, 19, 2, 9, 19, 23, 1, 23, 6, 27, 1, 13, 27, 31, 1, 31, 10, 35, 1, 9, 35, 39, 1, 39, 9, 43, 2, 6, 43, 47, 1, 47, 5, 51, 2, 10, 51, 55, 1, 6, 55, 59, 2, 13, 59, 63, 2, 13, 63, 67, 1, 6, 67, 71, 1, 71, 5,
             75, 2, 75, 6, 79, 1, 5, 79, 83, 1, 83, 6, 87, 2, 10, 87, 91, 1, 9, 91, 95, 1, 6, 95, 99, 1, 99, 6, 103, 2, 103, 9, 107, 2, 107, 10, 111, 1, 5, 111, 115, 1, 115, 6, 119, 2, 6, 119, 123, 1, 10, 123, 127, 1, 127, 5, 131, 1, 131, 2, 135, 1, 135, 5, 0, 99, 2, 0, 14, 0]

    # input = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    def chunks(list, size):
        for i in range(0, len(input), size):
            yield input[i:size+i]
    
    program_functions = list(chunks(input, 4))

    for func in program_functions:
        print(f'Current function: {func}')
        op = func[0]

        if op == 1:
            sum = input[func[1]] + input[func[2]]
            print(f'Changing position {func[3]} to {sum}')
            input[func[3]] = sum
        elif op == 2:
            prod = input[func[1]] * input[func[2]]
            print(f'Changing position {input[func[3]]} to {prod}')
            input[func[3]] = prod
        elif op == 99:
            return input[0]

    return "Challenge not solved"


def part2():
    return "Challenge not solved"


if __name__ == "__main__":
    answer1 = part1()
    answer2 = part2()
    print(f"Day 2 - Part 1 Answer: {answer1}")
    print(f"Day 2 - Part 2 Answer: {answer2}")
    save_answers(answer1, 2, 1)
    save_answers(answer2, 2, 2)
