def backtrack(target, numbers, index, current_value):
    if index == len(numbers):
        return current_value == target

    if current_value > target:
        return False
    
    # Addition
    if backtrack(target, numbers, index + 1, current_value + numbers[index]):
        return True
        
    # Multiplication
    if backtrack(target, numbers, index + 1, current_value * numbers[index]):
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

        if backtrack(target, numbers, 1, numbers[0]):
            sol += target

print(f"Answer: {sol}") # 4555081946288
