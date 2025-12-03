def max_bank_joltage(bank: str) -> int:
    best = 0
    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            val = int(bank[i] + bank[j])
            if val > best:
                best = val
    return best


def total_output_joltage(lines):
    return sum(max_bank_joltage(line.strip()) for line in lines if line.strip())


with open("input.txt") as f:
    lines = f.readlines()

print(total_output_joltage(lines))
