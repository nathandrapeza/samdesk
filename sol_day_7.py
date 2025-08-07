def can_equal_target(target, numbers, index, current_value):
    """
    Recursive backtracking function that indicates whether the numbers can reach the target using addition and/or
    multiplication (for part 1), and/or concatenation (for part 2).

    Args:
        target (int): The goal value on the left side of the colon on each line of the input.
        numbers (list): A list of numbers (ints) to process in order.
        index (int): The current index in the numbers list.
        current_value (int): The current accumulated value from previous operations.

    Returns:
        bool: True if the target can be reached using addition and/or multiplication, and/or concatenation.
        False otherwise.
    """

    if index == len(numbers):
        return current_value == target

    if current_value > target:
        return False
    
    # Addition
    if can_equal_target(target, numbers, index + 1, current_value + numbers[index]):
        return True
        
    # Multiplication
    if can_equal_target(target, numbers, index + 1, current_value * numbers[index]):
        return True

    # Concatenation (only in part 2)
    concatenated = int(str(current_value) + str(numbers[index]))
    if can_equal_target(target, numbers, index + 1, concatenated):
        return True

    return False

sol = 0

with open("day_7_input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
            
        target, numbers = line.split(": ")
        target = int(target)
        numbers = [int(num) for num in numbers.split(" ")]

        if can_equal_target(target, numbers, 1, numbers[0]):
            sol += target

# Part 1 solution: 4555081946288
# Part 2 solution: 227921760109726

print(f"Answer: {sol}")
