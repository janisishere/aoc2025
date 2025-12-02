def is_invalid_id(n: int) -> bool:
    """
    Returns True if n is of the form XY where X is a nonempty digit sequence
    repeated exactly twice (e.g., 55, 6464, 123123).
    """
    s = str(n)
    L = len(s)

    if L % 2 != 0:
        return False

    half = L // 2
    a, b = s[:half], s[half:]

    if a[0] == '0' or b[0] == '0':
        return False

    return a == b


def sum_invalid_ids(input_line: str) -> int:
    ranges = input_line.strip().split(",")
    total = 0

    for r in ranges:
        if not r:
            continue
        lo_str, hi_str = r.split("-")
        lo, hi = int(lo_str), int(hi_str)

        for n in range(lo, hi + 1):
            if is_invalid_id(n):
                total += n

    return total


puzzle_input = """input here""".replace("\n", "")

# Compute the result
result = sum_invalid_ids(puzzle_input)
print(result)
