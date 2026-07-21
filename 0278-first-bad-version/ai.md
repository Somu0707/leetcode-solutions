## 💭 Thought Process

When approaching this problem, the simplest method that comes to mind is checking every version sequentially from $1$ to $n$ using the `isBadVersion` API. 

However, since $n$ can be as large as $2^{31} - 1$, a linear search could require up to $2.14 \times 10^9$ API calls in the worst case, leading to a Time Limit Exceeded (TLE) error.

To optimize, we need to observe the structure of the data:
- If a version is **good**, all versions before it are guaranteed to be **good**.
- If a version is **bad**, all versions after it are guaranteed to be **bad**.

This forms a sorted boolean structure: `[false, false, ..., false, true, true, ..., true]`. Whenever we encounter a search space that is sorted or split into two distinct monotonic halves, **Binary Search** is the ideal algorithm to drastically reduce the search space from linear to logarithmic time.

---

## 💡 Intuition

The core insight is that finding the "first bad version" is equivalent to finding the **boundary** between the `false` (good) and `true` (bad) states.

- **Why Binary Search?** Instead of checking versions one by one, we inspect the middle version (`mid`). 
  - If `mid` is **bad**, we know the first bad version is either `mid` itself or somewhere to its left.
  - If `mid` is **good**, we know all versions up to `mid` are good, so the first bad version must lie strictly to its right.
- **Why `low + (high - low) / 2`?** When working with large integers up to $2^{31} - 1$, calculating `(low + high) / 2` can cause integer overflow. Using `low + (high - low) / 2` prevents overflow while calculating the exact same midpoint.

---

## 🚀 Approach

1. **Initialize Search Space**: Set two pointers, `low = 1` and `high = n`, defining the initial search range. Keep track of the potential answer in a variable `ans`.
2. **Binary Search Loop**: While `low <= high`:
   - Calculate the midpoint `mid = low + (high - low) / 2`.
   - Query the API using `isBadVersion(mid)`.
   - **If `mid` is bad**: Record `mid` as a candidate answer (`ans = mid`) and shrink the upper bound (`high = mid - 1`) to search for an even earlier bad version in the left half.
   - **If `mid` is good**: Shrink the lower bound (`low = mid + 1`) to search in the right half, as the first bad version must appear later.
3. **Return Result**: Once `low > high`, the search terminates, and `ans` holds the first bad version.

---

## 🧠 Algorithm

1. Set `low = 1`, `high = n`, and `ans = n`.
2. While `low <= high`:
   1. Compute `mid = low + (high - low) / 2`.
   2. If `isBadVersion(mid)` is `true`:
      - Set `ans = mid`.
      - Set `high = mid - 1`.
   3. Else (`isBadVersion(mid)` is `false`):
      - Set `low = mid + 1`.
3. Return `ans`.

---

## 🔍 Dry Run

Let's trace the algorithm with **`n = 5`** and **`bad = 4`**:

| Iteration | `low` | `high` | `mid` | `isBadVersion(mid)` | Action | `ans` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Initial** | 1 | 5 | - | - | Initialize search range | 5 |
| **Step 1** | 1 | 5 | 3 | `false` | Version 3 is good $\rightarrow$ set `low = mid + 1` (4) | 5 |
| **Step 2** | 4 | 5 | 4 | `true` | Version 4 is bad $\rightarrow$ set `ans = 4`, `high = mid - 1` (3) | 4 |
| **End** | 4 | 3 | - | - | Loop terminates as `low > high` | **4** |

**Final Output:** `4`

---

## ⚠️ Edge Cases

- **$n = 1$**: The loop executes once, evaluates `mid = 1`, and correctly identifies whether version 1 is bad without infinite loops or out-of-bounds errors.
- **First Version is Bad (`bad = 1`)**: The algorithm continuously shifts `high` to the left until `high = 0` and `ans` stores `1`.
- **Last Version is Bad (`bad = n`)**: The algorithm continuously shifts `low` to the right until `low = n + 1` and `ans` stores `n`.
- **Integer Overflow**: Handled properly by computing `mid` as `low + (high - low) / 2` instead of `(low + high) / 2`.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$\mathcal{O}(\log n)$**: In each iteration, the search space is halved. For $n$ versions, the maximum number of API calls made is $\lceil \log_2 n \rceil$.

### Space Complexity
- **$\mathcal{O}(1)$**: The algorithm uses a constant amount of extra space for tracking pointers (`low`, `high`, `mid`, `ans`).

---

## 🎯 Key Takeaways

- Binary Search applies to any search space with **monotonic properties** (e.g., `[false, ..., false, true, ..., true]`), not just sorted numerical arrays.
- Always calculate `mid` using `low + (high - low) / 2` to prevent potential **integer overflow** issues in language environments with fixed-size integer types.
- Saving candidate solutions during binary search enables clean boundary tracking without needing complex post-processing checks.