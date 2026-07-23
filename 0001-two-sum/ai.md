## 💭 Thought Process

When approaching the **Two Sum** problem, the most straightforward idea is to test every possible pair of numbers in the array to see if their sum equals the `target`. 

This brute-force approach requires two nested loops:
- The outer loop picks the first number.
- The inner loop iterates through the rest of the array to find a second number such that `nums[i] + nums[j] == target`.

While this works, checking all pairs takes **$\mathcal{O}(N^2)$** time complexity. Given that the array size $N$ can be up to $10^4$, an $\mathcal{O}(N^2)$ solution would perform up to $10^8$ operations, which is far too slow for optimal performance.

To improve this, we need to ask: *Can we find the required second number without scanning the array again?*

If we rewrite the equation:
$$\text{nums}[i] + \text{complement} = \text{target} \implies \text{complement} = \text{target} - \text{nums}[i]$$

This simple mathematical shift reveals that for every number we encounter, we are looking for a specific target **complement**. If we can store numbers we have already seen in a data structure that allows **$\mathcal{O}(1)$ average lookup time**, we can solve the problem in a single pass.

---

## 💡 Intuition

The key insight is to trade a small amount of extra memory for a dramatic speedup in execution time.

Instead of searching forward for a matching number, we store each element and its index as we iterate. As we move to the next element, we look *backward* to see if its complement has already been processed and saved.

A **Hash Map (Unordered Map)** is the ideal data structure for this task because:
1. It maps each element value (key) to its original array index (value).
2. It allows us to check if the `complement` exists in constant time $\mathcal{O}(1)$ on average.

---

## 🚀 Approach

1. **Initialize a Hash Map**: Create an empty hash map to keep track of previously seen numbers and their corresponding indices (`value -> index`).
2. **Iterate Through the Array**: Loop through `nums` index by index ($i = 0$ to $N-1$).
3. **Calculate Complement**: For the current element `nums[i]`, compute `complement = target - nums[i]`.
4. **Check Hash Map**:
   - If `complement` is already present in the map, we have found our pair! Return the current index $i$ and the stored index of `complement`.
   - If `complement` is not in the map, store the current element and its index (`map[nums[i]] = i`) so future elements can look it up.
5. **Return Result**: Return the indices once the match is found.

---

## 🧠 Algorithm

```text
1. Initialize an empty hash map 'seen'.
2. For each index 'i' from 0 to length(nums) - 1:
    a. Calculate complement = target - nums[i].
    b. If complement exists in 'seen':
        i. Return [i, seen[complement]].
    c. Add key nums[i] with value 'i' to 'seen'.
3. Return an empty array if no pair is found.
```

---

## 🔍 Dry Run

Let's trace the algorithm with an example:  
`nums = [2, 7, 11, 15]`, `target = 9`

| Step | Index ($i$) | Current Value (`nums[i]`) | Complement (`9 - nums[i]`) | Map State BEFORE step | Is Complement in Map? | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` | `2` | `9 - 2 = 7` | `{}` | ❌ No | Add `{2: 0}` to map |
| 2 | `1` | `7` | `9 - 7 = 2` | `{2: 0}` | ✅ Yes! (found at index `0`) | Return indices `[1, 0]` |

The execution finishes in just **2 iterations**!

---

## ⚠️ Edge Cases

- **Duplicate Values in Array (e.g., `nums = [3, 3]`, `target = 6`)**: By checking for the complement *before* adding the current number to the hash map, we avoid matching an element with itself. When the second `3` is processed, the first `3` is already stored in the map, correctly triggering a match.
- **Negative Numbers (e.g., `nums = [-3, 4, 3]`, `target = 0`)**: The subtraction `target - nums[i]` naturally handles negative values without needing any special logic.
- **Large Inputs**: The hash map lookup keeps execution time linear even for the maximum constraint $N = 10^4$.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$\mathcal{O}(N)$**: We traverse the array of length $N$ at most once. For each element, hash map lookups and insertions take $\mathcal{O}(1)$ average time complexity.

### Space Complexity
- **$\mathcal{O}(N)$**: In the worst-case scenario, we may store up to $N - 1$ elements in the hash map before finding a match.

---

## 🎯 Key Takeaways

- **Hash maps enable constant-time lookups**, reducing search overhead from $\mathcal{O}(N)$ to $\mathcal{O}(1)$.
- **Reframing the problem** from $a + b = \text{target}$ to $b = \text{target} - a$ simplifies search logic.
- **Space-Time Trade-off**: Spending extra memory ($\mathcal{O}(N)$ space) allows us to achieve optimal execution time ($\mathcal{O}(N)$ time).
- **Single-pass lookup**: Populating the map dynamically on-the-fly prevents self-matching issues and avoids the need for a separate preprocessing loop.