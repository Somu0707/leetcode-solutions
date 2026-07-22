# 875. Koko Eating Bananas

<div align="center">

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-brightgreen)
![Acceptance](https://img.shields.io/badge/Acceptance-50.27%25-blue)
![Topics](https://img.shields.io/badge/Topics-2-orange)

</div>

---

# 📝 Problem Statement

Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

---

# 📚 Examples

## Example 1

```
Input: piles = [3,6,7,11], h = 8
Output: 4
```

## Example 2

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

## Example 3

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

---

# 📌 Constraints

- `1 <= piles.length <= 10⁴`
- `piles.length <= h <= 10⁹`
- `1 <= piles[i] <= 10⁹`



---

# 🧠 AI Solution Explanation

## 💭 Thought Process

To solve this problem, a good starting point is to think about how we can test different eating speeds.

1. **Brute Force Approach**:
   We could test eating speeds starting from $k = 1$ and incrementally check $k = 2, 3, 4, \dots$ up to the maximum pile size. For each speed $k$, we iterate through all piles to calculate the total time required. As soon as we find a speed $k$ that allows Koko to finish within $h$ hours, we return $k$.

2. **Why Brute Force is Inefficient**:
   The maximum pile size can be up to $10^9$. In the worst case, linear search would require checking up to $10^9$ speeds. For each speed, we iterate through $N$ piles ($N \le 10^4$), leading to approximately $O(N \times \text{max}(piles))$ operations. This will trigger a **Time Limit Exceeded (TLE)** error.

3. **Key Observation**:
   Notice the relationship between eating speed $k$ and the total time required:
   - Increasing the speed $k$ **decreases** (or keeps equal) the total hours needed.
   - Decreasing the speed $k$ **increases** (or keeps equal) the total hours needed.

   This **monotonic behavior** (a non-increasing function) means the search space of valid speeds is sorted naturally. If a speed $k$ is fast enough, any speed greater than $k$ is also fast enough. If $k$ is too slow, any speed less than $k$ is definitely too slow. This property makes the problem a classic candidate for **Binary Search on Answer**.

---

## 💡 Intuition

Instead of searching through elements of an array, we perform **Binary Search over a range of possible answers**:
- **Minimum possible speed (`low`)**: $1$ (eating at least 1 banana per hour).
- **Maximum possible speed (`high`)**: $\text{max}(piles)$ (eating the largest pile in 1 hour; eating faster than this provides no extra benefit because Koko cannot eat from multiple piles in the same hour).

By repeatedly bisecting this range $[low, high]$:
- If a candidate speed `mid` enables Koko to finish within $h$ hours, then `mid` is a valid speed. However, a smaller valid speed might exist, so we narrow our search to the left half (`high = mid - 1`).
- If `mid` takes more than $h$ hours, it is too slow, so we must increase the speed and search the right half (`low = mid + 1`).

---

## 🚀 Approach

1. **Identify the Range**:
   - Set `low = 1` as the lower boundary of speed.
   - Find the maximum value in `piles` and set `high = max(piles)` as the upper boundary.

2. **Binary Search Loop**:
   - Calculate candidate speed `mid = low + (high - low) / 2`.
   - Compute total hours required to consume all piles at speed `mid`.

3. **Helper Function / Hours Calculation**:
   - For a pile with $P$ bananas eaten at speed $k$, time taken is $\lceil P / k \rceil$.
   - In integer arithmetic, $\lceil P / k \rceil$ is computed as `(P + k - 1) / k`.

4. **Adjust Range**:
   - If total hours $\le h$: Speed `mid` is feasible. We attempt to find a smaller valid speed by moving `high = mid - 1`.
   - If total hours $> h$: Speed `mid` is too slow. We must increase speed by moving `low = mid + 1`.

5. **Result**:
   - When the binary search loop completes, `low` holds the minimum valid eating speed.

---

## 🧠 Algorithm

```text
function minEatingSpeed(piles, h):
    low = 1
    high = max_element(piles)

    while low <= high:
        mid = low + (high - low) / 2
        total_hours = calculateTotalHours(piles, mid)

        if total_hours <= h:
            high = mid - 1      // Try to find a smaller feasible speed
        else:
            low = mid + 1       // Speed is too slow, increase it

    return low

function calculateTotalHours(piles, speed):
    total_hours = 0
    for each pile in piles:
        total_hours += (pile + speed - 1) / speed  // Ceiling division
    return total_hours
```

---

## 🔍 Dry Run

### Input
- `piles = [3, 6, 7, 11]`
- `h = 8`

### Execution

- **Initial Search Range**: `low = 1`, `high = 11` (since $\text{max}(3, 6, 7, 11) = 11$)

| Iteration | `low` | `high` | `mid` (Speed) | Hours per Pile | Total Hours | Condition (`Total <= 8`) | Next Range |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 1 | 11 | **6** | $\lceil 3/6 \rceil=1, \lceil 6/6 \rceil=1, \lceil 7/6 \rceil=2, \lceil 11/6 \rceil=2$ | **6** | $6 \le 8$ **(Valid)** | `high = 5` |
| **2** | 1 | 5 | **3** | $\lceil 3/3 \rceil=1, \lceil 6/3 \rceil=2, \lceil 7/3 \rceil=3, \lceil 11/3 \rceil=4$ | **10** | $10 > 8$ **(Invalid)** | `low = 4` |
| **3** | 4 | 5 | **4** | $\lceil 3/4 \rceil=1, \lceil 6/4 \rceil=2, \lceil 7/4 \rceil=2, \lceil 11/4 \rceil=3$ | **8** | $8 \le 8$ **(Valid)** | `high = 3` |

- **Termination**: Loop ends because `low` ($4$) > `high` ($3$).
- **Output**: `low = 4`.

---

## ⚠️ Edge Cases

- **Minimum possible hours ($h = \text{piles.length}$)**: Koko must eat each pile in at most 1 hour. The required speed will be equal to $\text{max}(piles)$, which is handled correctly as `high` starts at $\text{max}(piles)$.
- **Integer Overflow**: Summing calculated hours across all piles can exceed standard 32-bit integer limits when pile sizes and speeds are large. Use a 64-bit integer (`long long` in C++) for `total_hours`.
- **Floating-Point Inaccuracy**: Using `ceil((double)pile / speed)` can introduce floating-point precision issues. The integer formula `(pile + speed - 1) / speed` avoids this entirely.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$O(N \log M)$**, where $N$ is the number of piles (`piles.length`) and $M$ is the maximum pile size ($\text{max}(piles)$).
- **Reason**: The search space size is $M$. Binary search takes $O(\log M)$ steps. In each step, we iterate over $N$ elements to compute total hours, leading to a total time complexity of $O(N \log M)$.

### Space Complexity
- **$O(1)$**
- **Reason**: The algorithm uses a constant amount of extra space for pointers and sum variables without requiring additional data structures.

---

## 🎯 Key Takeaways

- **Binary Search on Answer Space**: When a decision problem exhibits monotonic behavior over a bounded numeric range, binary search can optimize linear searches from $O(M)$ to $O(\log M)$.
- **Integer Ceiling Division**: Computing $\lceil a / b \rceil$ safely with integer arithmetic can be written as `(a + b - 1) / b`.
- **Search Space Bounds**: Defining tight boundaries ($low = 1$, $high = \text{max}(piles)$) ensures minimal iterations while guaranteeing correctness.
- **Data Type Safety**: Always account for intermediate sum overflows when accumulating values over large datasets.

---

# 💻 C++ Solution

```cpp
class Solution {
public:
    long long calculateTotalHours(vector<int>& piles, int speed) {
        long long totalH = 0;

        for (int bananas : piles) {
            totalH += (bananas + speed - 1LL) / speed;
        }

        return totalH;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1;
        int high = *max_element(piles.begin(), piles.end());

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (calculateTotalHours(piles, mid) <= h) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return low;
    }
};
```

---

## 🚀 Repository

⭐ If you found this explanation helpful, consider starring the repository.

Happy Coding! 🚀