#include <iostream>

using namespace std;

static long long maxLengthBrutish(long long l, long long r, long long s) {
    /*
        Brute-force baseline (intentionally non-optimal):
        Greedily constructs the lexicographically smallest (and thus minimum-sum)
        beacon ladder by:
          a1 = l
          gaps = 1, 2, 3, ...

        For any fixed length n, this construction minimizes both a_n and the total sum.
        Therefore, if this minimal ladder violates (a_i in [l, r]) or sum <= S,
        then no ladder of that length can exist.

        This approach is correct but may be slow for large inputs.
    */

    if (s < l || r < l) {
        return 0; // Robustness for invalid input (not expected per constraints).
    }

    __int128 currentA = 0;      // last element a_length
    __int128 currentSum = 0;    // sum of chosen elements
    __int128 prevDiff = 0;      // last gap (a_i - a_{i-1})
    long long length = 0;

    while (true) {
        __int128 nextA;
        __int128 nextDiff;

        if (length == 0) {
            nextA = (__int128)l;
            nextDiff = 0;
        } else {
            nextDiff = prevDiff + 1;   // smallest strictly larger integer gap
            nextA = currentA + nextDiff;
        }

        __int128 nextSum = currentSum + nextA;

        if (nextA > (__int128)r) {
            break;
        }
        if (nextSum > (__int128)s) {
            break;
        }

        currentA = nextA;
        currentSum = nextSum;
        prevDiff = nextDiff;
        length++;
    }

    return length;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) {
        return 0;
    }

    while (t--) {
        long long l, r, s;
        cin >> l >> r >> s;
        cout << maxLengthBrutish(l, r, s) << "\n";
    }

    return 0;
}