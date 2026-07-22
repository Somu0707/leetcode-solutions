## 💭 Thought Process

When approaching this problem, a simple starting point is to test every version sequentially from $1$ to $n$ using the `isBadVersion` API. The first version that returns `true` would be our answer. However, for a maximum value of $n = 2^{31} - 1$, a linear scan could require over 2 billion API calls in the worst case, making it far too slow.

To optimize, we look for a structural pattern in the data. Once a version is bad, all subsequent versions are guaranteed to be bad. This means the array of versions is implicitly divided into two distinct contiguous blocks:
`[false, false, ..., false, true, true, ..., true]`

This monotonic property (a transition from `false` to `true` at exactly one threshold point) allows us to eliminate half of the remaining choices with a single check. Instead of checking every element, we can use **Binary Search** to find the boundary in logarithmic time.

---

## 💡 Intuition

The key insight is that the versions are sorted by state: all good versions appear before all bad versions.

- **Why Binary Search works**: Checking the middle version (`mid`) gives definitive information about where the first bad version lies:
  - If `isBadVersion(mid)` is `true`, then `mid` is a bad version. It could be the *first* bad version, or the first bad version lies somewhere to its left. We save `mid` as a candidate solution and search the left half.
  - If `isBadVersion(mid)` is `false`, then `mid` and all versions before it are good. The first bad version must be strictly to the right of `mid`.
- **Why it is efficient**: Each API call eliminates half of the remaining search space, drastically reducing the number of calls from $O(n)$ to $O(\log n)$.

---

## 🚀 Approach

1. **Initialize Search Range**: Set `low = 1` and `high = n` to cover all possible versions. Maintain a variable `ans` initialized to `n` to store the smallest bad version index found so far.
2. **Search Loop**: Execute a loop while `low <= high`:
   - Calculate the midpoint `mid` safely using `low + (high - low) / 2`.
   - Call `isBadVersion(mid)`:
     - **If `true`**: Mark `ans = mid` as a candidate answer, and narrow the search space to the left half (`high = mid - 1`) to check if an even earlier bad version exists.
     - **If `false`**: Exclude `mid` and all preceding versions by shifting the search space to the right half (`low = mid + 1`).
3. **Return Result**: Once `low > high`, the search terminates, and `ans` will hold the index of the first bad version.

---

## 🧠 Algorithm

1. Initialize `low = 1`, `high = n`, and `ans = n`.
2. While `low <= high`:
   a. Compute `mid = low + (high - low) / 2`.
   b. Call `isBadVersion(mid)`:
      - If `true`:
        - Set `ans = mid`.
        - Set `high = mid - 1`.
      - Else:
        - Set `low = mid + 1`.
3. Return `ans`.

---

## 🔍 Dry Run

Let $n = 5$ and the first bad version be $4$.

| Step | `low` | `high` | `mid` | `isBadVersion(mid)` | Action | `ans` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Initial | `1` | `5` | - | - | Initialize search boundary | `5` |
| **Iter 1** | `1` | `5` | `3` | `false` | Version 3 is good; move right (`low = 4`) | `5` |
| **Iter 2** | `4` | `5` | `4` | `true` | Version 4 is bad; save candidate and check left (`high = 3`) | `4` |
| **End** | `4` | `3` | - | - | Loop terminates as `low > high` | **`4`** |

**Final Output**: `4`

---

## ⚠️ Edge Cases

- **Single Version ($n = 1$)**: The range is `[1, 1]`. The loop runs once, evaluates `mid = 1`, updates `ans = 1`, and correctly returns `1`.
- **First Version is Bad ($bad = 1$)**: `isBadVersion` returns `true` on early iterations, causing `high` to continuously shift left until `ans` settles on `1`.
- **Last Version is Bad ($bad = n$)**: `isBadVersion` returns `false` until `mid` reaches `n`, causing `low` to shift right until `ans` settles on `n`.
- **Integer Overflow**: Calculating `mid` as `(low + high) / 2` can cause integer overflow when `low + high` exceeds $2^{31} - 1$. Using `low + (high - low) / 2` avoids overflow entirely.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$\mathcal{O}(\log n)$**: In each step, the search space is halved. For $n = 2^{31} - 1$, the maximum number of API calls made will be at most $31$.

### Space Complexity
- **$\mathcal{O}(1)$**: The algorithm only uses a few scalar variables (`low`, `high`, `mid`, `ans`) to keep track of state, consuming constant memory.

---

## 🎯 Key Takeaways

- Binary Search is applicable to any monotonic domain (e.g., `[false, ..., false, true, ..., true]`), not just explicitly sorted numerical arrays.
- Always calculate midpoints as `low + (high - low) / 2` to protect against 32-bit signed integer overflow.
- When searching for a boundary, keep track of the best valid candidate found so far while continuing to shrink the search window.
- Minimizing expensive operations (like network/API calls) is a primary practical use case for logarithmic algorithms.