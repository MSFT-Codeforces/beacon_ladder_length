
# Generates 15 edge test case inputs for the "Beacon Ladder Length" problem.
# Prints in the required format:
# Test Cases:
# Input 1:
# <input>
# ...
# Input 15:
# <input>

def make_input(cases):
    """cases: list of (l, r, S) tuples -> returns full multi-test input string"""
    lines = [f"{l} {r} {S}" for (l, r, S) in cases]
    return str(len(cases)) + "\n" + "\n".join(lines)

tests = []

# 1) Absolute minimums
tests.append(make_input([(1, 1, 1)]))

# 2) Maximum l=r=S (forces n=1)
MAX = 10**18
tests.append(make_input([(MAX, MAX, MAX)]))

# 3) n=2 is feasible, n=3 not (gap condition vacuous for n=2)
# l=5: minimal ladder n=2 -> [5,6] fits; n=3 would need a3=8 > r=6
tests.append(make_input([(5, 6, 100)]))

# 4) Exact equality on range constraint for n=3 (a3 == r)
# l=10, n=3 => a3 = 10 + 3 = 13
tests.append(make_input([(10, 13, MAX)]))

# 5) Exact equality on sum constraint for n=3 (sum == S), range very large
# l=1, n=3 => sum = 1+2+4 = 7
tests.append(make_input([(1, MAX, 7)]))

# 6) Off-by-one failure on range for n=3 (r is 1 too small)
# l=10, n=3 needs a3=13 but r=12
tests.append(make_input([(10, 12, MAX)]))

# 7) Off-by-one failure on sum for n=3 (S is 1 too small)
# Needs S>=7, give 6
tests.append(make_input([(1, MAX, 6)]))

# 8) Exact equality on both constraints for a medium n (n=10)
# l=2: a10 = 2 + 45 = 47; sum = 10*2 + (9*10*11)/6 = 185
tests.append(make_input([(2, 47, 185)]))

# 9) Huge range but very tight S (sum constraint dominates; also stresses overflow if binary search uses huge upper bound)
tests.append(make_input([(1, MAX, 1_000_000)]))

# 10) Range would allow n=2, but sum forbids it due to very large l and tiny S (=l)
# n=2 would require sum = 2l+1 > 1e18, so only n=1.
l10 = MAX - 1000
tests.append(make_input([(l10, MAX, l10)]))

# 11) Very tight small range, huge S (range dominates; answer should be small)
tests.append(make_input([(1, 3, MAX)]))

# 12) Large l, large r, large S (tests handling of large l in sum constraint)
tests.append(make_input([(10**12, MAX, MAX)]))

# 13) Another large-l regime (different scale), large r and S
tests.append(make_input([(10**9, MAX, MAX)]))

# 14) Stress: maximum t=10000 (performance + many small edge patterns)
# Mix of patterns: (n=1 only), (n=2 possible), (tight range), (tight sum)
stress_cases = []
patterns = [
    (1, 1, 1),
    (1, 2, 3),          # n=2 fits (1,2) sum=3
    (100, 100, 100),    # n=1 only (l=r)
    (2, 4, 10),         # small numbers
    (5, 6, 11),         # n=2 fits, sum boundary-ish
]
for i in range(10_000):
    stress_cases.append(patterns[i % len(patterns)])
tests.append(make_input(stress_cases))

# 15) Large n equality case (big integers; tests overflow if using 64-bit intermediates)
# Choose n=1_000_000, l=1; set r and S to exact minimal ladder bounds.
n = 1_000_000
l = 1
r = l + (n * (n - 1)) // 2
S = n * l + ((n - 1) * n * (n + 1)) // 6
tests.append(make_input([(l, r, S)]))

print("Test Cases:")
for i, inp in enumerate(tests, 1):
    print(f"Input {i}:")
    print(inp)
    if i != len(tests):
        print()
