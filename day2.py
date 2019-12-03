original = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 2, 9, 19, 23, 2, 13, 23, 27, 1, 6, 27, 31, 2,
           6, 31, 35, 2, 13, 35, 39, 1, 39, 10, 43, 2, 43, 13, 47, 1, 9, 47, 51, 1, 51, 13, 55, 1, 55, 13, 59, 2, 59,
           13, 63, 1, 63, 6, 67, 2, 6, 67, 71, 1, 5, 71, 75, 2, 6, 75, 79, 1, 5, 79, 83, 2, 83, 6, 87, 1, 5, 87, 91, 1,
           6, 91, 95, 2, 95, 6, 99, 1, 5, 99, 103, 1, 6, 103, 107, 1, 107, 2, 111, 1, 111, 5, 0, 99, 2, 14, 0, 0]

program = original.copy()

def execute(memory: list):
    instructionPointer = 0
    while True:
        if memory[instructionPointer] == 1:
            memory[memory[instructionPointer + 3]] = memory[memory[instructionPointer + 1]] + memory[
                memory[instructionPointer + 2]]
        elif memory[instructionPointer] == 2:
            memory[memory[instructionPointer + 3]] = memory[memory[instructionPointer + 1]] * memory[
                memory[instructionPointer + 2]]
        elif memory[instructionPointer] == 99:
            break
        else:
            print("broken instructions, halting")
            return memory
        instructionPointer += 4
    return memory


def bruteforce():
    for i in range(100):
        for j in range(100):
            program = original.copy()
            program[1] = i
            program[2] = j
            if execute(program)[0] == 19690720:
                return i, j


print(bruteforce())
