import math
import sys


def is_length_feasible(
    lower_bound: int,
    upper_bound: int,
    budget_sum: int,
    length: int,
) -> bool:
    """Check whether a minimal beacon ladder of a given length is feasible.

    Args:
        lower_bound: Minimum allowed value for each element (l).
        upper_bound: Maximum allowed value for each element (r).
        budget_sum: Maximum allowed total sum of elements (S).
        length: Candidate ladder length n.

    Returns:
        True if a valid beacon ladder of length `length` exists, otherwise False.
    """
    last_value = lower_bound + (length * (length - 1)) // 2
    if last_value > upper_bound:
        return False

    total_sum = (
        length * lower_bound
        + (length * (length + 1) * (length - 1)) // 6
    )
    return total_sum <= budget_sum


def maximum_beacons(lower_bound: int, upper_bound: int, budget_sum: int) -> int:
    """Compute the maximum feasible beacon ladder length for one test case.

    Args:
        lower_bound: Minimum allowed value for each element (l).
        upper_bound: Maximum allowed value for each element (r).
        budget_sum: Maximum allowed total sum of elements (S).

    Returns:
        The maximum integer length n for which a valid beacon ladder exists.
    """
    range_width = upper_bound - lower_bound

    upper_from_range = (1 + math.isqrt(1 + 8 * range_width)) // 2 + 2
    upper_from_sum = budget_sum // lower_bound + 1
    high = min(upper_from_range, upper_from_sum)

    low = 1
    best_length = 1
    while low <= high:
        midpoint = (low + high) // 2
        if is_length_feasible(
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            budget_sum=budget_sum,
            length=midpoint,
        ):
            best_length = midpoint
            low = midpoint + 1
        else:
            high = midpoint - 1

    return best_length


def main() -> None:
    """Read input, solve all test cases, and print results.

    Returns:
        None.
    """
    input_stream = sys.stdin.buffer
    test_cases_line = input_stream.readline().split()
    test_cases_count = int(test_cases_line[0])

    results = []
    for _ in range(test_cases_count):
        line_parts = input_stream.readline().split()
        lower_bound = int(line_parts[0])
        upper_bound = int(line_parts[1])
        budget_sum = int(line_parts[2])

        answer = maximum_beacons(lower_bound, upper_bound, budget_sum)
        results.append(str(answer))

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()