# 278. First Bad Version

<div align="center">

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Acceptance](https://img.shields.io/badge/Acceptance-47.38%25-blue)
![Topics](https://img.shields.io/badge/Topics-2-orange)

</div>

---

# 📝 Problem Statement

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

---

# 📚 Examples

## Example 1

```
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```

## Example 2

```
Input: n = 1, bad = 1
Output: 1
```

---

# 📌 Constraints

- `1 <= bad <= n <= 2³¹ - 1`



---

# 🧠 AI Solution Explanation

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

---

# 💻 C++ Solution

```cpp
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int low  =1;
        int high = n;
        int ans = n;
        while(low<=high){
            int mid = low+(high-low)/2;
            if(isBadVersion(mid)){
                ans = mid;
                high = mid-1;
            }
            else low = mid+1;
        }
        return ans;
    }
};
```

---

## 🚀 Repository

⭐ If you found this explanation helpful, consider starring the repository.

Happy Coding! 🚀