def safe(report):
    # check if r is strictly increasing or decreasing with steps of 1–3
    d = [j - i for i, j in zip(report, report[1:])]
    return (all(x > 0 for x in d) or all(x < 0 for x in d)) and all(1 <= abs(x) <= 3 for x in d)

with open("day_2_input.txt") as f:
    # parse each non‑empty line into a list of ints
    reports = [list(map(int, line.split())) for line in f if line.strip()]

# Input is the same for parts 1 and 2

# amount of reports that are safe (part 1)
safe_reports = sum(safe(r) for r in reports) # 524 using input

# in the second part, we're allowed to drop by one level (part 2)
safe_allow_dropping = sum(safe(r) or any(safe(r[:i] + r[i+1:]) for i in range(len(r))) for r in reports) # 569

print("Part 1:", safe_reports)
print("Part 2:", safe_allow_dropping)
