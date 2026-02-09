
import os
from typing import Tuple, List


def _normalize_newlines(s: str) -> str:
    return s.replace("\r\n", "\n").replace("\r", "\n")


def _parse_input(input_text: str) -> Tuple[int, List[Tuple[int, int, int]]]:
    txt = _normalize_newlines(input_text)
    toks = txt.split()
    if not toks:
        raise ValueError("Input is empty")

    try:
        t = int(toks[0])
    except Exception:
        raise ValueError("First token of input is not an integer (t)")

    if t < 1:
        raise ValueError(f"t must be >= 1, got {t}")

    expected = 1 + 3 * t
    if len(toks) < expected:
        raise ValueError(f"Input has too few integers: expected {expected}, got {len(toks)}")

    cases: List[Tuple[int, int, int]] = []
    idx = 1
    for _ in range(t):
        try:
            l = int(toks[idx])
            r = int(toks[idx + 1])
            S = int(toks[idx + 2])
        except Exception:
            raise ValueError(f"Failed to parse l r S for a test case at input token index {idx}")
        idx += 3
        cases.append((l, r, S))
    return t, cases


def _min_last(n: int, l: int) -> int:
    # Minimal last element occurs for a1=l and gaps 1,2,...,n-1.
    return l + n * (n - 1) // 2


def _min_sum(n: int, l: int) -> int:
    # Minimal sum occurs for a1=l and gaps 1,2,...,n-1:
    # a_i = l + (i-1)i/2
    # sum = n*l + (n-1)n(n+1)/6
    return n * l + (n - 1) * n * (n + 1) // 6


def _feasible_length(n: int, l: int, r: int, S: int) -> Tuple[bool, str]:
    """
    Validates that there exists at least one beacon ladder of length n satisfying constraints.
    (Does NOT attempt to verify that n is maximum.)
    """
    if n < 1:
        return False, f"n must be >= 1, got {n}"

    # Necessary (and in fact sufficient) constraints via minimal construction.
    last = _min_last(n, l)
    if last > r:
        return False, f"no valid ladder: minimal possible a_n={last} exceeds r={r}"

    total = _min_sum(n, l)
    if total > S:
        return False, f"no valid ladder: minimal possible sum={total} exceeds S={S}"

    return True, "OK"


def check(input_text: str, output_text: str) -> Tuple[bool, str]:
    try:
        t, cases = _parse_input(input_text)
    except Exception as e:
        return False, f"Checker error while parsing input: {e}"

    out = _normalize_newlines(output_text)

    # Allow a single trailing newline at EOF; otherwise be strict.
    if out.endswith("\n"):
        out = out[:-1]
        if out.endswith("\n"):
            return False, "Output has more than one trailing newline / extra blank line at EOF"

    if out == "":
        return False, f"Expected {t} lines (one integer per test case), got empty output"

    lines = out.split("\n")
    if len(lines) != t:
        return False, f"Expected exactly {t} lines, got {len(lines)}"

    for ci, ((l, r, S), line) in enumerate(zip(cases, lines), start=1):
        if line == "":
            return False, f"Case {ci}: empty line; expected a single integer"
        if line.strip() != line:
            return False, f"Case {ci}: leading/trailing whitespace is not allowed"
        if len(line.split()) != 1:
            return False, f"Case {ci}: expected exactly one integer token on the line"

        try:
            n = int(line)
        except Exception:
            return False, f"Case {ci}: output is not a valid integer: '{line}'"

        # Basic sanity bounds derived from statement constraints.
        # Upper bound using only range: strictly increasing integers within [l..r] => n <= r-l+1.
        if n < 1:
            return False, f"Case {ci}: n={n} must be >= 1"
        if n > (r - l + 1):
            return False, f"Case {ci}: n={n} exceeds max possible distinct values in range (r-l+1={r-l+1})"

        # Also sum lower bound: sum >= n*l => n*l <= S (necessary).
        if n * l > S:
            return False, f"Case {ci}: n={n} violates necessary sum bound n*l={n*l} > S={S}"

        ok, why = _feasible_length(n, l, r, S)
        if not ok:
            return False, f"Case {ci}: n={n} is not feasible ({why})"

    # Note: This checker validates formatting and feasibility of the reported lengths.
    # It does not (and per requirements should not) verify that each reported n is maximal.
    return True, "OK"


if __name__ == "__main__":
    in_path = os.environ.get("INPUT_PATH")
    out_path = os.environ.get("OUTPUT_PATH")
    if not in_path or not out_path:
        print("False")
    else:
        with open(in_path, "r", encoding="utf-8") as f:
            inp = f.read()
        with open(out_path, "r", encoding="utf-8") as f:
            out = f.read()
        ok, _ = check(inp, out)
        print("True" if ok else "False")
