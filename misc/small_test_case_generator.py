
def make_inputs():
    inputs = []

    # 1) Absolute minimum boundary
    inputs.append("1\n1 1 1\n")

    # 2) n=2 feasible with exact sum equality (also checks n=2 vacuous gap condition)
    inputs.append("1\n1 2 3\n")

    # 3) Range prevents n=3 (n=2 max), with room for increasing but last-element bound tight-ish
    inputs.append("1\n1 3 100\n")

    # 4) n=3 exactly fits range equality: l=2 -> sequence 2,3,5
    inputs.append("1\n2 5 100\n")

    # 5) n=3 exactly fits sum equality: 1+2+4 = 7
    inputs.append("1\n1 10 7\n")

    # 6) Off-by-one on range: just 1 short for n=3 (needs r=5)
    inputs.append("1\n2 4 100\n")

    # 7) Off-by-one on sum: just 1 short for n=3 (needs S=7)
    inputs.append("1\n1 10 6\n")

    # 8) All-equal range forces n=1
    inputs.append("1\n10 10 10\n")

    # 9) Very tight range of width 1, but large S; checks range-limited behavior
    inputs.append("1\n5 6 100\n")

    # 10) Sum-limited with larger r (n grows until sum stops it)
    inputs.append("1\n1 50 20\n")

    # 11) Range-limited with ample S (n determined by triangular bound)
    inputs.append("1\n3 10 100\n")

    # 12) Multi-test input (t>1) mixing different regimes
    inputs.append(
        "3\n"
        "1 2 100\n"   # should allow n=2 easily
        "2 6 12\n"    # checks both constraints in small numbers
        "8 8 20\n"    # all-equal range => n=1
    )

    # 13) Another explicit n=2 equality case with larger l
    inputs.append("1\n7 8 15\n")

    # 14) Sum tight with l>1 (n=4 just barely fails)
    inputs.append("1\n4 30 25\n")

    # 15) Small "stress" within constraints: multiple cases (t=10) varied small values
    inputs.append(
        "10\n"
        "1 1 5\n"     # range forces n=1
        "1 4 100\n"   # range-limited
        "2 3 10\n"    # tight range
        "2 7 11\n"    # sum tight-ish
        "3 15 30\n"   # moderate
        "1 20 12\n"   # sum-limited
        "5 25 40\n"   # moderate
        "6 10 100\n"  # range-limited
        "9 12 25\n"   # tight-ish
        "2 20 9\n"    # sum-limited
    )

    return inputs


def main():
    cases = make_inputs()
    print("Test Cases: ")
    for i, s in enumerate(cases, 1):
        print(f"Input {i}:")
        print(s.rstrip("\n"))
        if i != len(cases):
            print()

if __name__ == "__main__":
    main()
