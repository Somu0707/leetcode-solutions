## 💭 Thought Process

To find the minimum eating speed $k$, let's first consider the simplest brute-force approach:

1. **Brute Force Idea:**
   We can start testing eating speeds starting from $k = 1$ and incrementally check speeds $k = 2, 3, 4, \dots$. For each speed, we calculate the total hours Koko needs to finish all piles. The first speed $k$ that allows Koko to eat all bananas within $h$ hours would be our answer.

2. **Why Brute Force Fails:**
   The maximum possible pile size can be up to $10^9$. If the optimal speed is close to $10^9$ and there are $10^4$ piles, testing every speed sequentially would take $O(N \times \max(piles))$ operations, leading to a Time Limit Exceeded (TLE) verdict.

3. **Key Observation:**
   Notice how the total time required changes as the speed $k$ changes:
   - If a speed $k$ is **too slow** (takes more than $h$ hours), any speed smaller than $k$ will also be too slow.
   - If a speed $k$ is **fast enough** (takes $\le h$ hours), any speed greater than $k$ will also be fast enough.

   This **monotonic behavior** (a clear transition from *invalid* speeds to *valid* speeds) allows us to eliminate half of the search space at each step using **Binary Search on Answer**.

---

## 💡 Intuition

Instead of searching within the input array, we apply **Binary Search over a range of potential values** (the eating speeds):

- **Minimum possible speed (`low`):** `1` banana per hour (Koko must eat at least 1 banana per hour).
- **Maximum possible speed (`high`):** $\max(piles)$ bananas per hour (at this speed, Koko eats any pile in at most 1 hour, taking $N$ hours in total, which is always $\le h$).

By repeatedly picking the middle speed `mid`, we test if Koko can finish within $h$ hours:
- If `mid` works, we record it as a potential candidate and try to find an even smaller speed by searching in the left half.
- If `mid` does not work, we must increase the speed by searching in the right half.

---

## 🚀 Approach

1. **Find the Search Range:**
   - Set `low = 1`.
   - Set `high = max(piles)`.

2. **Binary Search for Minimum Speed:**
   - Compute `mid = low + (high - low) / 2`.
   - Calculate the total hours required to finish all piles at speed `mid`.
   - For a pile with $P$ bananas, hours taken is $\lceil P / mid \rceil$, which can be computed using integer division as `(P + mid - 1) / mid`.

3. **Adjust Search Boundaries:**
   - **If total hours $\le h$:** Speed `mid` is feasible. Try to find a smaller valid speed by moving the upper bound (`high = mid - 1`).
   - **If total hours $> h$:** Speed `mid` is too slow. Increase the lower bound (`low = mid + 1`).

4. **Return Answer:**
   - When `low` exceeds `high`, `low` will hold the minimum required speed.

---

## 🧠 Algorithm

```text
Function calculateTotalHours(piles, speed):
    totalHours = 0
    For each pile in piles:
        totalHours = totalHours + ceil(pile / speed)
    Return totalHours

Function minEatingSpeed(piles, h):
    low = 1
    high = max element in piles

    While low <= high:
        mid = low + (high - low) / 2
        
        If calculateTotalHours(piles, mid) <= h:
            high = mid - 1    // Try finding a smaller valid speed
        Else:
            low = mid + 1     // Speed too slow, increase it

    Return low
```

---

## 🔍 Dry Run

Let's trace the algorithm with `piles = [3, 6, 7, 11]` and `h = 8`:

- Initial Bounds: `low = 1`, `high = 11`

| Iteration | `low` | `high` | `mid` | Hours Needed Calculation | Total Hours | Feasible? ($\le 8$) | Action |
| :---: | :---: | :---: | :---: | :--- | :---: | :---: | :--- |
| **1** | 1 | 11 | **6** | $\lceil 3/6 \rceil + \lceil 6/6 \rceil + \lceil 7/6 \rceil + \lceil 11/6 \rceil = 1 + 1 + 2 + 2$ | **6** | Yes ($6 \le 8$) | `high = 6 - 1 = 5` |
| **2** | 1 | 5 | **3** | $\lceil 3/3 \rceil + \lceil 6/3 \rceil + \lceil 7/3 \rceil + \lceil 11/3 \rceil = 1 + 2 + 3 + 4$ | **10** | No ($10 > 8$) | `low = 3 + 1 = 4` |
| **3** | 4 | 5 | **4** | $\lceil 3/4 \rceil + \lceil 6/4 \rceil + \lceil 7/4 \rceil + \lceil 11/4 \rceil = 1 + 2 + 2 + 3$ | **8** | Yes ($8 \le 8$) | `high = 4 - 1 = 3` |

- **Loop Ends:** `low = 4`, `high = 3` (`low > high`).
- **Result:** Return `low = 4`.

---

## ⚠️ Edge Cases

- **$h$ equals the number of piles ($h = N$):** Koko must eat at least one full pile per hour. The algorithm correctly converges to $\max(piles)$.
- **Integer Overflow:** Accumulation of hours for all piles can exceed standard 32-bit integer limits (`INT_MAX`) when $h$ and pile sizes are large ($10^9$). Using a 64-bit integer (`long long`) for `totalHours` prevents overflow.
- **Single Pile ($N = 1$):** The search range correctly reduces to $\lceil piles[0] / h \rceil$.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$O(N \log M)$**, where $N$ is the number of piles and $M = \max(piles)$.
- The binary search range is $[1, M]$, requiring $O(\log M)$ iterations. In each iteration, we iterate through all $N$ piles to sum up the hours, taking $O(N)$ time.

### Space Complexity
- **$O(1)$** auxiliary space.
- The algorithm uses only a few variables (`low`, `high`, `mid`, `totalH`) without requiring additional data structures.

---

## 🎯 Key Takeaways

- **Binary Search on Answer** is a powerful technique when searching in a bounded numerical range with a monotonic decision function.
- Integer ceiling division $\lceil a / b \rceil$ can be safely implemented using `(a + b - 1) / b` without converting to floating-point numbers.
- Always be mindful of potential 32-bit integer overflow when computing sums of large numbers in helper functions.