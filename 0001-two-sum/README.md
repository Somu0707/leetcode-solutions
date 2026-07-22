# 1. Two Sum

<div align="center">

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Acceptance](https://img.shields.io/badge/Acceptance-57.84%25-blue)
![Topics](https://img.shields.io/badge/Topics-2-orange)

</div>

---

# 📝 Problem Statement

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have *exactly* one solution, and you may not use the *same* element twice.

You can return the answer in any order.

---

# 📚 Examples

## Example 1

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## Example 2

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

## Example 3

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

---

# 📌 Constraints

- `2 <= nums.length <= 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`
- `-10⁹ <= target <= 10⁹`
- Only one valid answer exists.


---

# 💡 Follow Up

Can you come up with an algorithm that is less than `O(n²)` time complexity?


---

# 🧠 AI Solution Explanation

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

---

# 💻 C++ Solution

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& a, int target) {
        unordered_map<int, int> mp;
        int sum=0;
        // vector<int> ans;
        for(int i=0;i<a.size();i++){
            if(mp.find(target-a[i])!=mp.end()){
                return {i,mp[target-a[i]]};
            }
            mp[a[i]] = i;
        }
        return {};
    }
};
```

---

## 🚀 Repository

⭐ If you found this explanation helpful, consider starring the repository.

Happy Coding! 🚀