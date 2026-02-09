**Beacon Ladder Length**

Time Limit: **1 seconds**

Memory Limit: **32 MB**

In the underground city of Arkhaven, engineers place beacons along a tunnel. Each beacon is assigned an integer frequency, forming a sequence $a_1,a_2,\dots,a_n$.

The sequence must be a **beacon ladder**, meaning:

1. Frequencies strictly increase:
   $$a_{i-1} < a_i \quad \text{for all } 2 \le i \le n$$
2. The gaps between consecutive frequencies also strictly increase:
   $$(a_i-a_{i-1}) < (a_{i+1}-a_i) \quad \text{for all } 2 \le i < n$$

For each test case, you are given integers $l$, $r$, and $S$ such that:

- Every frequency must satisfy $l \le a_i \le r$
- The total power used must satisfy $\sum_{i=1}^{n} a_i \le S$

For each test case, determine the **maximum possible length** $n$ of a beacon ladder.

**Input Format:-**

The first line contains an integer $t$ — the number of test cases.  
Each of the next $t$ lines contains three integers $l$, $r$, $S$.

**Output Format:-**

For each test case, output a single integer — the maximum feasible $n$.

**Constraints:-**

- $1 \le t \le 10^4$
- $1 \le l \le r \le 10^{18}$
- $l \le S \le 10^{18}$
**Examples:-**
 - **Input:**
```
1
4 30 25
```

 - **Output:**
```
3
```

 - **Input:**
```
10
1 1 5
1 4 100
2 3 10
2 7 11
3 15 30
1 20 12
5 25 40
6 10 100
9 12 25
2 20 9
```

 - **Output:**
```
1
3
2
3
4
3
4
3
2
2
```

**Note:-**
In the first example, we can take the shortest increasing gaps \(1,2\) starting from \(l=4\): the ladder \((4,5,7)\) has strictly increasing values and gaps, stays within \([4,30]\), and has sum \(4+5+7=16 \le 25\). Length \(4\) is impossible because the minimal length-\(4\) ladder \((4,5,7,10)\) already sums to \(26>25\), so the answer is \(3\).

In the first example, \(l=r=1\), so every valid ladder must be \((1)\). Hence the maximum length is \(1\).

In the first example, with \(l=1,r=4,S=100\), the minimal ladder of length \(3\) is \((1,2,4)\) with gaps \(1,2\) and sum \(7\). Length \(4\) would require \((1,2,4,7)\) which violates \(a_4 \le r=4\), so the answer is \(3\).

In the first example, with \(l=2,r=3,S=10\), length \(2\) is possible as \((2,3)\) (sum \(5\)), but length \(3\) would minimally be \((2,3,5)\) and violates \(a_3 \le 3\). So the answer is \(2\).

In the first example, with \(l=2,r=7,S=11\), a length \(3\) ladder \((2,3,5)\) has sum \(10 \le 11\). The minimal length \(4\) ladder \((2,3,5,8)\) violates \(a_4 \le 7\), so the answer is \(3\).

In the first example, with \(l=3,r=15,S=30\), the minimal length \(4\) ladder is \((3,4,6,9)\) with sum \(22 \le 30\). Length \(5\) would minimally be \((3,4,6,9,13)\) with sum \(35>30\), so the answer is \(4\).

In the first example, with \(l=1,r=20,S=12\), the minimal length \(3\) ladder is \((1,2,4)\) (sum \(7\)), and the minimal length \(4\) ladder is \((1,2,4,7)\) (sum \(14>12\)). Hence the maximum length is \(3\).

In the first example, with \(l=5,r=25,S=40\), the minimal length \(4\) ladder is \((5,6,8,11)\) with sum \(30 \le 40\). Length \(5\) would minimally be \((5,6,8,11,15)\) with sum \(45>40\), so the answer is \(4\).

In the first example, with \(l=6,r=10,S=100\), the minimal length \(3\) ladder is \((6,7,9)\) with sum \(22\), while length \(4\) would minimally be \((6,7,9,12)\) and violates \(a_4 \le 10\). Therefore the answer is \(3\).

In the first example, with \(l=9,r=12,S=25\), length \(2\) is possible as \((9,10)\) (sum \(19\)). Length \(3\) would minimally be \((9,10,12)\) but its sum is \(31>25\), so the answer is \(2\).

In the first example, with \(l=2,r=20,S=9\), the minimal length \(2\) ladder \((2,3)\) has sum \(5 \le 9\). The minimal length \(3\) ladder \((2,3,5)\) has sum \(10>9\), so the answer is \(2\).