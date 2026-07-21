## 💭 Thought Process

When first encountering this problem, a simple brute-force approach comes to mind: compare every possible pair of numbers in the array using nested loops. For each element at index `i`, we would scan through all subsequent elements at index `j` to check if `nums[i] + nums[j] == target`. 

While this works, checking all pairs requires $O(n^2)$ time complexity. As the input array grows up to $10^4$ elements, an $O(n^2)$ algorithm performs roughly $10^8$ operations, which is far too slow and will result in a **Time Limit Exceeded (TLE)** error.

To optimize, ask yourself: *As we iterate through the array, what information do we actually need at each step?*

When standing at a number `x`, we don't need to scan the entire remaining array to find its pair. We already know the exact value we need: `complement = target - x`. Instead of scanning the array repeatedly to find this complement, we can use a data structure that allows us to look up previously seen numbers in constant time—a **Hash Map**.

---

## 💡 Intuition

The core insight is transforming an addition search problem into a lookup problem using the equation:
$$\text{complement} = \text{target} - \text{current\_element}$$

Instead of looking forward in the array to find a match, we can look backward at the elements we have already processed. 

By storing every element we visit alongside its index in a hash map, we can check if the current element's complement was already seen earlier. If it exists in our map, we have found our solution in a single pass.

---

## 🚀 Approach

1. **Initialize a Hash Map**: Create a map to store key-value pairs where the key is the number from the array and the value is its corresponding index (`value -> index`).
2. **Iterate Through the Array**: Process each element index by index.
3. **Calculate the Complement**: For the current element `nums[i]`, compute `complement = target - nums[i]`.
4. **Check Map for Complement**:
   - **If found**: The pair exists! Return the stored index of the complement and the current index `i`.
   - **If not found**: Store the current number and its index (`nums[i] -> i`) in the hash map so future elements can pair with it.
5. **Return Result**: Since the problem guarantees exactly one valid solution, the answer will always be found during the traversal.

---

## 🧠 Algorithm

1. Initialize an empty hash map `seen`.
2. For each index `i` from `0` to `nums.length - 1`:
   a. Compute `complement = target - nums[i]`.
   b. If `complement` exists in `seen`:
      i. Return `[seen[complement], i]`.
   c. Add `nums[i]` to `seen` with value `i`.
3. Return an empty array if no pair is found.

---

## 🔍 Dry Run

Let's trace the algorithm with `nums = [2, 7, 11, 15]` and `target = 9`:

| Step | Current Index (`i`) | Current Value (`nums[i]`) | Complement (`9 - nums[i]`) | Map State (`value -> index`) | Action / Result |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | `0` | `2` | `9 - 2 = 7` | `{}` | `7` is not in map. Store `2 -> 0`. |
| **2** | `1` | `7` | `9 - 7 = 2` | `{2: 0}` | `2` **is** in map at index `0`! Return `[0, 1]`. |

**Output:** `[0, 1]`

---

## ⚠️ Edge Cases

- **Duplicate Elements (e.g., `nums = [3, 3]`, `target = 6`)**: 
  - *Handling*: By checking if the complement exists in the map *before* adding the current element, we avoid pairing an element with itself. At index `1`, the first `3` is already stored at index `0`, correctly returning `[0, 1]`.
- **Negative Numbers and Zero (e.g., `nums = [-3, 4, 0, 8]`, `target = 5`)**:
  - *Handling*: The formula `complement = target - current` holds true mathematically for all integers (positive, negative, or zero). Hash maps support negative integer keys naturally.
- **Minimum Array Size ($n = 2$)**:
  - *Handling*: The loop runs for both elements, checking the complement on the second iteration and returning immediately.

---

## ⏱️ Complexity Analysis

### Time Complexity: $\mathcal{O}(n)$
- We iterate through the array of $n$ elements at most once.
- Hash map lookup and insertion operations take $\mathcal{O}(1)$ time on average.
- Overall time complexity is linear, $\mathcal{O}(n)$.

### Space Complexity: $\mathcal{O}(n)$
- In the worst-case scenario, we may insert $n - 1$ elements into the hash map before finding the matching pair.
- Auxiliary space required is proportional to the input size, $\mathcal{O}(n)$.

---

## 🎯 Key Takeaways

- **Hash maps trade space for time**: By using $\mathcal{O}(n)$ additional space, we reduce search time from $\mathcal{O}(n)$ to $\mathcal{O}(1)$.
- **Reframe the problem**: Converting $x + y = \text{target}$ into $y = \text{target} - x$ simplifies the lookup requirement.
- **Single-pass pattern**: Checking for existence *before* insertion allows processing and lookup in a single pass without self-matching bugs.
- **Optimized for lookups**: Choosing the right data structure (Hash Map over Array) is key to moving from brute-force to optimal solutions.