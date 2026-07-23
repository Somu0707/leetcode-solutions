## 💭 Thought Process

When approaching this problem, a simple brute-force idea is to iterate linearly through all versions from `1` to `n` and call `isBadVersion(i)` for each version `i`. The first version that returns `true` would be our answer.

However, since `n` can be as large as $2^{31} - 1$, a linear scan would require up to $O(n)$ API calls, leading to a Time Limit Exceeded (TLE) error. 

To optimize this, we must look for a pattern in the data:
- Once a version is bad, **all subsequent versions are also bad**.
- This creates a sorted sequence of boolean states: `[false, false, ..., true, true]`.

This monotonic property (a sequence transitioning from one state to another without flipping back) is a classic indicator that we can use **Binary Search** to find the boundary in logarithmic time.

---

## 💡 Intuition

The key insight is that the search space is divided into two continuous segments:
1. **Good versions** (`isBadVersion(v) == false`) on the left.
2. **Bad versions** (`isBadVersion(v) == true`) on the right.

Our goal is to find the transition point—the first occurrence of `true`.

By selecting a middle point `mid`:
- If `isBadVersion(mid)` is `true`, `mid` could be the first bad version, or the first bad version exists somewhere to its **left**. We record `mid` as a potential answer and narrow our search to the left half.
- If `isBadVersion(mid)` is `false`, all versions up to `mid` are guaranteed to be good. The first bad version must lie strictly to its **right**.

Using this logic, we halve the search space at each step, drastically reducing the number of API calls needed.

---

## 🚀 Approach

1. **Initialize Search Space**: Set `low = 1` and `high = n`. Maintain a variable `ans` initialized to `n` to keep track of the minimal bad version found so far.
2. **Binary Search Loop**: Continue looping while `low <= high`:
   - Calculate the midpoint `mid` safely to avoid integer overflow: `mid = low + (high - low) / 2`.
   - Call the `isBadVersion(mid)` API.
   - If `mid` is a bad version (`true`):
     - Update `ans = mid` (this might be the first bad version).
     - Search the left range (`high = mid - 1`) to check if an even earlier bad version exists.
   - If `mid` is a good version (`false`):
     - Search the right range (`low = mid + 1`).
3. **Return Answer**: When `low > high`, the search terminates, and `ans` holds the first bad version.

---

## 🧠 Algorithm

1. Set `low = 1`, `high = n`, and `ans = n`.
2. While `low <= high`:
   1. Compute `mid = low + (high - low) / 2`.
   2. If `isBadVersion(mid)` is `true`:
      - Set `ans = mid`.
      - Set `high = mid - 1`.
   3. Else:
      - Set `low = mid + 1`.
3. Return `ans`.

---

## 🔍 Dry Run

Let $n = 5$ and the first bad version be $4$.

| Step | `low` | `high` | `mid` | `isBadVersion(mid)` | Action | `ans` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | `1` | `5` | - | - | Initialize boundaries | `5` |
| **Iter 1**| `1` | `5` | `3` | `false` | Version 3 is Good $\rightarrow$ Move right (`low = 4`) | `5` |
| **Iter 2**| `4` | `5` | `4` | `true` | Version 4 is Bad $\rightarrow$ Update `ans = 4`, move left (`high = 3`) | `4` |
| **End** | `4` | `3` | - | - | Loop terminates as `low > high` | `4` |

**Final Output**: `4`

---

## ⚠️ Edge Cases

- **Single Version ($n = 1$)**: The loop runs once with `low = 1`, `high = 1`, `mid = 1`, correctly identifying if version 1 is bad.
- **First Version is Bad ($bad = 1$)**: The algorithm continuously updates `ans` and moves `high` to the left until `high = 0`, returning `1`.
- **Last Version is Bad ($bad = n$)**: The algorithm repeatedly shifts `low` to the right until it reaches `n`, returning `n`.
- **Integer Overflow**: Using `mid = low + (high - low) / 2` prevents overflow when $n$ is close to $2^{31} - 1$, which would occur if calculated as `(low + high) / 2`.

---

## ⏱️ Complexity Analysis

### Time Complexity
$\mathcal{O}(\log n)$: The search space is divided in half at each iteration, requiring at most $\lceil\log_2 n\rceil$ calls to `isBadVersion`.

### Space Complexity
$\mathcal{O}(1)$: The algorithm uses a fixed number of variables (`low`, `high`, `mid`, `ans`), requiring constant auxiliary space.

---

## 🎯 Key Takeaways

- Binary Search can be applied to any search space that displays a **monotonic property** (e.g., `[false, ..., false, true, ..., true]`).
- Always calculate midpoints as `low + (high - low) / 2` to prevent potential 32-bit signed integer overflow.
- Storing candidate answers in a variable (`ans`) during binary search simplifies boundary management when searching for first or last occurrences.