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

To solve this problem, let's start by thinking about what happens at different eating speeds:

1. **Brute Force Idea**: 
   We could try every possible eating speed $k$, starting from $k = 1$ and going up to the size of the largest pile ($\max(\text{piles})$). For each speed $k$, we iterate through all piles and calculate the total hours Koko needs to finish them. The first speed $k$ that allows Koko to finish within $h$ hours would be our minimum answer.

2. **Why Brute Force is Inefficient**: 
   The max pile size can be as large as $10^9$. If we linearly test speeds from $1$ to $10^9$, and for each speed we iterate through $N$ piles ($N \le 10^4$), the total operations could be up to $10^{13}$. This will definitely result in a **Time Limit Exceeded (TLE)**.

3. **Key Observation**: 
   Notice the relationship between speed $k$ and total hours required:
   - If Koko eats at a higher speed, the total hours required **decreases or stays the same**.
   - If Koko eats at a lower speed, the total hours required **increases**.

   This monotonic behavior (if speed $k$ is valid, any speed $> k$ is also valid) means we don't need to check every speed linearly. Instead, we can use **Binary Search on Answer** to find the minimal valid speed $k$ efficiently.

---

## 💡 Intuition

- **Search Space**:
  - Minimum speed `low = 1`: Koko eats at least 1 banana per hour.
  - Maximum speed `high = max(piles)`: Eating faster than the largest pile does not reduce total time below $N$ hours, because Koko can eat at most one pile per hour.

- **Monotonic Feasibility Function**:
  For a candidate speed $k$, calculating the total time required takes $O(N)$ time. Since the answer space is sorted from $1$ to $\max(\text{piles})$, Binary Search allows us to eliminate half of the search space at each step.

- **Ceiling Division Trick**:
  To compute hours taken for a pile of size $p$ at speed $k$, we need $\lceil p / k \rceil$. Using integer arithmetic, this can be written as `(p + k - 1) / k` without needing floating-point operations.

---

## 🚀 Approach

1. **Initialize Binary Search Range**:
   - Set `low = 1`.
   - Set `high = max(piles)`.

2. **Binary Search for Minimum Speed**:
   - Calculate candidate speed `mid = low + (high - low) / 2`.
   - Compute the total hours required to finish all piles at speed `mid`.
   - **If total hours $\le h$**: Speed `mid` is fast enough! Since we want the *minimum* speed, record `mid` as a potential answer and narrow the search range to smaller speeds (`high = mid - 1`).
   - **If total hours $> h$**: Speed `mid` is too slow. Increase the speed range (`low = mid + 1`).

3. **Return Result**:
   - When the search loop finishes, `low` will be pointing to the smallest valid eating speed.

---

## 🧠 Algorithm

1. Function `calculateTotalHours(piles, speed)`:
   - Initialize `total_hours = 0`.
   - For each `bananas` in `piles`:
     - `total_hours += (bananas + speed - 1) / speed`
   - Return `total_hours`.

2. Function `minEatingSpeed(piles, h)`:
   - Set `low = 1`
   - Set `high = maximum element in piles`
   - While `low <= high`:
     - `mid = low + (high - low) / 2`
     - If `calculateTotalHours(piles, mid) <= h`:
       - `high = mid - 1` (try finding a smaller valid speed)
     - Else:
       - `low = mid + 1` (speed is too slow, increase lower bound)
   - Return `low`

---

## 🔍 Dry Run

Let's trace the algorithm with an example: `piles = [3, 6, 7, 11]`, `h = 8`

1. **Initial Setup**:
   - `low = 1`, `high = 11` ($\max(3, 6, 7, 11)$)

2. **Iteration 1**:
   - `mid = 1 + (11 - 1) / 2 = 6`
   - Calculate hours at speed $6$:
     - Pile $3 \rightarrow \lceil 3/6 \rceil = 1$ hour
     - Pile $6 \rightarrow \lceil 6/6 \rceil = 1$ hour
     - Pile $7 \rightarrow \lceil 7/6 \rceil = 2$ hours
     - Pile $11 \rightarrow \lceil 11/6 \rceil = 2$ hours
     - Total Hours $= 1 + 1 + 2 + 2 = 6$
   - $6 \le 8$ (Feasible speed $\rightarrow$ try smaller speeds)
   - Update: `high = 6 - 1 = 5`

3. **Iteration 2**:
   - `low = 1`, `high = 5`
   - `mid = 1 + (5 - 1) / 2 = 3`
   - Calculate hours at speed $3$:
     - Pile $3 \rightarrow 1$, Pile $6 \rightarrow 2$, Pile $7 \rightarrow 3$, Pile $11 \rightarrow 4$
     - Total Hours $= 1 + 2 + 3 + 4 = 10$
   - $10 > 8$ (Too slow $\rightarrow$ need faster speed)
   - Update: `low = 3 + 1 = 4`

4. **Iteration 3**:
   - `low = 4`, `high = 5`
   - `mid = 4 + (5 - 4) / 2 = 4`
   - Calculate hours at speed $4$:
     - Pile $3 \rightarrow 1$, Pile $6 \rightarrow 2$, Pile $7 \rightarrow 2$, Pile $11 \rightarrow 3$
     - Total Hours $= 1 + 2 + 2 + 3 = 8$
   - $8 \le 8$ (Feasible speed $\rightarrow$ try smaller speeds)
   - Update: `high = 4 - 1 = 3`

5. **Termination**:
   - Loop ends since `low (4) > high (3)`.
   - Result: `low = 4`.

---

## ⚠️ Edge Cases

- **$h = \text{piles.length}$**: Koko has exactly enough hours to eat one pile per hour. She must eat at a speed equal to the largest pile ($\max(\text{piles})$).
- **Integer Overflow**: Total hours accumulated across piles can exceed standard 32-bit integer limits when `piles[i]` and $h$ are large (up to $10^9$). Using a **64-bit integer** (`long long`) for `total_hours` avoids overflow during evaluation.
- **Single Pile Input**: Handled naturally because search boundaries adjust between $1$ and `piles[0]`.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$O(N \log M)$**, where $N$ is the number of piles (`piles.length`) and $M$ is the maximum value in `piles` ($\max(\text{piles})$).
- The binary search space ranges from $1$ to $M$, taking $O(\log M)$ iterations.
- In each iteration, calculating total hours requires traversing all $N$ piles, taking $O(N)$ time.

### Space Complexity
- **$O(1)$** auxiliary space.
- Only scalar variables are used for binary search boundaries and sum calculations, consuming constant extra memory.

---

## 🎯 Key Takeaways

- **Binary Search on Answer Space** is ideal when finding the minimum/maximum parameter that satisfies a monotonic condition.
- **Monotonicity** guarantees that if a condition is satisfied at speed $k$, it will also be satisfied for all speeds $> k$.
- Ceiling division for positive integers $a / b$ can be computed using integer arithmetic as `(a + b - 1) / b`.
- Always check variable types for potential **integer overflow** when summing large values across many elements.

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