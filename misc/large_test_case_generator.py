
# Generates 10 large inputs for the "Beacon Ladder Length" problem.
# Each "Input k" is a full valid input file (with its own t and test cases).

def make_input(cases):
    lines = [str(len(cases))]
    for l, r, S in cases:
        assert 1 <= l <= r <= 10**18
        assert l <= S <= 10**18
        lines.append(f"{l} {r} {S}")
    return "\n".join(lines)

def tetra_term(n):
    # (n-1)*n*(n+1)/6
    return (n - 1) * n * (n + 1) // 6

inputs = []

# Input 1: maximal r and S, smallest l (overflow-prone midpoints, large feasible n)
inputs.append(make_input([
    (1, 10**18, 10**18),
]))

# Input 2: large l but still allows non-trivial n; big r,S
# Tests impact of n*l in sum constraint.
inputs.append(make_input([
    (5 * 10**11, 10**18, 10**18),
]))

# Input 3: l=r=1e18, S=1e18 (forces n=1; tight range + big numbers)
inputs.append(make_input([
    (10**18, 10**18, 10**18),
]))

# Input 4: n=2 is feasible but n=3 is impossible due to tight range; large values
# Also targets the "gap condition is vacuous for n=2" pitfall.
l4 = 4 * 10**17
inputs.append(make_input([
    (l4, l4 + 1, 10**18),
]))

# Input 5: exact equality on sum constraint with large n (close to max possible under S<=1e18)
n5 = 1_800_000
l5 = 1
S5 = n5 * l5 + tetra_term(n5)
assert S5 <= 10**18
inputs.append(make_input([
    (l5, 10**18, S5),
]))

# Input 6: off-by-one on sum constraint (S = exact - 1)
inputs.append(make_input([
    (l5, 10**18, S5 - 1),
]))

# Input 7: exact equality on BOTH range and sum for small n, but with very large magnitudes
# Uses n=4 minimal ladder: last increment is +6, sum adds +10 beyond 4*l.
l7 = 2 * 10**17
r7 = l7 + 6
S7 = 4 * l7 + 10
inputs.append(make_input([
    (l7, r7, S7),
]))

# Input 8: off-by-one on range constraint (r = exact - 1), sum still ample
inputs.append(make_input([
    (l7, r7 - 1, S7),
]))

# Input 9: multi-testcase input (varied regimes, all with large magnitudes somewhere)
# - sum-limited with huge range
# - very large r,S with moderate l
# - tiny range with huge S
# - exact sum boundary for n=3 with large l
# - exact sum boundary for n=2 with large l
cases9 = []
cases9.append((1, 10**18, 10**15))  # huge range, comparatively smaller S (still large)
cases9.append((10**6, 10**18, 10**18))
cases9.append((2 * 10**14, 2 * 10**14 + 3, 10**18))
l93 = 3 * 10**17
S93 = 3 * l93 + 4  # n=3 minimal sum: 3l + 4
cases9.append((l93, l93 + 3, S93))
l92 = 4 * 10**17
S92 = 2 * l92 + 1  # n=2 minimal sum: 2l + 1
cases9.append((l92, l92 + 1, S92))
inputs.append(make_input(cases9))

# Input 10: maximum t=10000 stress input, mixed patterns to catch:
# - overflow in intermediate computations
# - incorrect upper bounds / binary search issues
# - small-n logic and tight ranges
cases10 = []
for i in range(10_000):
    typ = i % 4
    if typ == 0:
        # Huge range, huge S, tiny l (overflow-prone if hi is from range bound)
        l, r, S = 1, 10**18, 10**18
    elif typ == 1:
        # Larger l to stress n*l term; still huge r,S
        l, r, S = 10**12 + i, 10**18, 10**18
    elif typ == 2:
        # Tight range but large magnitudes; feasible n limited by range and sum
        l = 10**14 + i
        r = l + 10**6
        S = 10**18
    else:
        # Very large l close to 1e18; typically forces n=1 (tests trivial handling)
        l = 10**18 - (i % 1000)
        r = 10**18
        S = 10**18
    cases10.append((l, r, S))
inputs.append(make_input(cases10))

print("Test Cases:")
for idx, inp in enumerate(inputs, start=1):
    print(f"Input {idx}:")
    print(inp)
    if idx != len(inputs):
        print()
