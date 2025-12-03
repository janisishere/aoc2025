def max_digit_joltage(bank: str, k: int = 12) -> int:
    to_remove = len(bank) - k
    stack = []

    for digit in bank.strip():
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    result_digits = stack[:k]

    return int("".join(result_digits))


def total_output_joltage_part(lines):
    return sum(max_digit_joltage(line.strip(), 12)
               for line in lines if line.strip())


with open("input.txt") as f:
    lines = f.readlines()

print(total_output_joltage_part(lines))
