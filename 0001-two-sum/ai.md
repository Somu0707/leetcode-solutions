## 💭 Thought Process

When approaching this problem, the initial inclination might be to test every possible pair of numbers in the array to see if their sum equals the `target`. This brute-force approach uses two nested loops: for each element, we iterate through the remainder of the array to search for a matching complement. However, checking all pairs requires $O(n^2)$ time, which quickly becomes too slow as the size of the array grows.

To optimize, we need to ask: **Can we find the required complement faster than scanning the entire array every time?**

For any given number $x$, the required complement that completes the sum is fixed: $\text{complement} = \text{target} - x$. Instead of actively searching for this complement in future iterations, we can flip the perspective—as we move through the array, we can remember the numbers we have already seen and their indices. If the complement of the current number is among the previously seen numbers, we have instantly found our pair!

---

## 💡 Intuition

The key insight is transforming a **search problem** into a **lookup problem**.

- **Why a Hash Map?** Hash maps provide constant-time $O(1)$ average complexity for insertions and lookups. By mapping each visited element's value to its index, we can immediately query whether the needed complement has already been processed.
- **Why a Single Pass?** We don't need to populate the entire map beforehand. By checking for the complement *before* adding the current number to the map, we achieve two goals:
  1. We prevent an element from matching with itself.
  2. We naturally handle duplicate numbers without overriding required indices prematurely.

---

## 🚀 Approach

1. Initialize an empty hash map where keys represent array values and values represent their respective zero-based indices.
2. Iterate through the array from left to right:
   1. Calculate the required complement for the current element: `complement = target - current_element`.
   2. Query the hash map for the `complement`.
   3. **If found**: Return the index of the complement (retrieved from the hash map) along with the current index.
   4. **If not found**: Store the `current_element` as the key and its index as the value in the hash map.
3. Because the problem guarantees exactly one valid solution, the iteration is guaranteed to locate and return the matching pair.

---

## 🧠 Algorithm

1. Initialize `map` as an empty Hash Table.
2. For index `i` from `0` to `size(nums) - 1`:
   1. Set `complement = target - nums[i]`.
   2. If `complement` exists in `map`:
      - Return `[i, map[complement]]`.
   3. Store `map[nums[i]] = i`.
3. Return an empty result if no solution exists (fallback).

---

## 🔍 Dry Run

Let's trace the algorithm with `nums = [2, 7, 11, 15]` and `target = 9`:

| Step | Index (`i`) | Value (`nums[i]`) | Complement (`9 - nums[i]`) | Map State Before Step | Map Lookup Result | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | `0` | `2` | `9 - 2 = 7` | `{}` | `7` not in map | Add `2: 0` to map |
| **2** | `1` | `7` | `9 - 7 = 2` | `{2: 0}` | `2` found at index `0` | Return `[1, 0]` |

The algorithm terminates immediately at Step 2 and returns `[1, 0]`.

---

## ⚠️ Edge Cases

- **Negative Numbers**: Works seamlessly because subtraction correctly evaluates negative complements (e.g., if `target = -3` and `nums[i] = -5`, then `complement = -3 - (-5) = 2`).
- **Duplicate Values**: Handled safely. If `nums = [3, 3]` and `target = 6`, when processing the second `3`, the complement `3` is already present in the hash map from the first element, so the match is detected before any overwriting occurs.
- **Minimum Array Length ($N = 2$)**: Handled without extra logic since the loop evaluates both elements and finds the match on the second iteration.

---

## ⏱️ Complexity Analysis

### Time Complexity
$\mathcal{O}(N)$: We traverse the array containing $N$ elements at most once. For each element, hash map lookups and insertions take $\mathcal{O}(1)$ average time.

### Space Complexity
$\mathcal{O}(N)$: In the worst-case scenario, we may need to store up to $N - 1$ elements in the hash map before finding a matching pair.

---

## 🎯 Key Takeaways

- Hash maps trade space ($\mathcal{O}(N)$) to significantly reduce time complexity from quadratic ($\mathcal{O}(N^2)$) to linear ($\mathcal{O}(N)$).
- Reformulating mathematical problems to look for complements (`target - current`) simplifies lookups.
- Building the hash map dynamically during a single pass prevents self-matching and gracefully handles duplicates.