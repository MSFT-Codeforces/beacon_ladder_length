
import sys
import re

INT_RE = re.compile(r"-?\d+$")

def is_int_token(tok: str) -> bool:
    return bool(INT_RE.fullmatch(tok))

def main() -> None:
    data = sys.stdin.read()
    if data == "":
        print("False")
        return

    lines = data.splitlines()

    # Disallow empty/whitespace-only lines (strict line structure)
    for ln in lines:
        if ln.strip() == "":
            print("False")
            return

    if len(lines) < 1:
        print("False")
        return

    first_tokens = lines[0].strip().split()
    if len(first_tokens) != 1 or not is_int_token(first_tokens[0]):
        print("False")
        return

    try:
        t = int(first_tokens[0])
    except Exception:
        print("False")
        return

    if not (1 <= t <= 10_000):
        print("False")
        return

    # Must have exactly t subsequent lines
    if len(lines) != t + 1:
        print("False")
        return

    LIM = 10**18

    for i in range(1, t + 1):
        toks = lines[i].strip().split()
        if len(toks) != 3 or any(not is_int_token(x) for x in toks):
            print("False")
            return
        try:
            l = int(toks[0])
            r = int(toks[1])
            S = int(toks[2])
        except Exception:
            print("False")
            return

        if not (1 <= l <= r <= LIM):
            print("False")
            return
        if not (l <= S <= LIM):
            print("False")
            return

    print("True")

if __name__ == "__main__":
    main()
