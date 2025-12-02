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

def is_invalid_id_v2(n: int) -> bool:
    """
    Returns True if n consists of some block B repeated >= 2 times.
    No leading zeroes in the block B.
    """
    s = str(n)
    L = len(s)

    # k = block length
    for k in range(1, L // 2 + 1):
        if L % k != 0:  # block must tile the whole string
            continue

        block = s[:k]
        if block[0] == '0':  # block can't start with zero
            continue

        repetitions = L // k
        if repetitions >= 2 and block * repetitions == s:
            return True

    return False


def sum_invalid_ids_v2(input_line: str) -> int:
    ranges = input_line.strip().split(",")
    total = 0

    for r in ranges:
        if not r:
            continue
        lo_str, hi_str = r.split("-")
        lo, hi = int(lo_str), int(hi_str)

        for n in range(lo, hi + 1):
            if is_invalid_id_v2(n):
                total += n

    return total


puzzle_input = """input here""".replace("\n", "")

# Compute the result
result = sum_invalid_ids(puzzle_input)
result2 = sum_invalid_ids_v2(puzzle_input)
print(result)
print(result2)
