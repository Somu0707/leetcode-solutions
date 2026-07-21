# 🚀 Solution Explanation

---

## 💭 Thought Process

When first encountering this problem, a simple brute-force approach comes to mind: compare every single pair of numbers in the array to see if they sum up to the target. This would involve two nested loops, taking $O(n^2)$ time. 

However, we can notice that for any number `x` we are currently looking at, we are searching for a very specific second number: `target - x` (the complement). The brute-force approach is slow because searching for this complement in an unsorted array takes $O(n)$ time. 

To optimize this, we need a way to find if the complement exists in the array much faster. If we can perform this search in $O(1)$ constant time, we can solve the entire problem in a single pass. This naturally points us toward using a Hash Map.

---

## 💡 Intuition

The key insight is to trade a small amount of memory for a massive boost in speed. 

By utilizing a **Hash Map**, we can store the numbers we have already seen along with their respective indices. As we traverse the array:
- We calculate the complement needed to reach the target: `complement = target - current_value`.
- Instead of searching the rest of the array, we check our Hash Map to see if this complement has already been processed.
- If it is in the map, we instantly have our solution.
- If it is not, we store the current number and its index in the map and move to the next element.

This "one-pass" approach is highly efficient because we populate the map dynamically as we go. This also ensures that we never accidentally pair an element with itself.

---

## 🚀 Approach

1. Initialize an empty Hash Map to store the elements of the array as keys and their corresponding indices as values.
2. Iterate through the array from left to right.
3. For each element:
   - Calculate the required `complement` (`target - current_element`).
   - Look up this `complement` in the Hash Map.
   - If the complement exists in the map, return the current index and the index of the complement retrieved from the map.
   - If the complement does not exist, insert the current element and its index into the Hash Map.
4. If the loop finishes without finding a pair, return an empty array (though the problem guarantees a solution exists).

---

## 🧠 Algorithm

1. Create an empty hash map `seen`.
2. For each index `i` from `0` to `n - 1`:
   - Set `current = nums[i]`.
   - Set `complement = target - current`.
   - If `complement` exists in `seen`:
     - Return `[seen[complement], i]`.
   - Store `current` in `seen` with index `i` (`seen[current] = i`).
3. Return an empty list if no match is found.

---

## 🔍 Dry Run

Let's trace the algorithm with `nums = [2, 7, 11, 15]` and `target = 9`.

* **Initial State:** 
  `seen = {}`

* **Step 1 (`i = 0`, `nums[0] = 2`):**
  - `complement = 9 - 2 = 7`
  - Is `7` in `seen`? No.
  - Insert `2` into `seen`: `seen = {2: 0}`

* **Step 2 (`i = 1`, `nums[1] = 7`):**
  - `complement = 9 - 7 = 2`
  - Is `2` in `seen`? Yes! It is stored at index `0`.
  - We immediately return `[0, 1]`.

---

## ⚠️ Edge Cases

- **Duplicate Values:** If the array contains duplicate values (e.g., `nums = [3, 3]`, `target = 6`), the algorithm handles them correctly. When we are at the second `3`, we look for `6 - 3 = 3` in the map. The first `3` is already stored, so we successfully return their indices without overwriting issues.
- **Negative Numbers and Zero:** Since hash map lookups and basic arithmetic work seamlessly with negative integers and zero, no special logic is required.
- **No Self-Pairing:** Because we check the map for the complement *before* adding the current element to the map, an element cannot match with itself.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$O(n)$**: We traverse the array of size $n$ exactly once. Hash map lookups and insertions take $O(1)$ time on average. Thus, the overall time complexity is linear.

### Space Complexity
- **$O(n)$**: In the worst-case scenario, we may need to store up to $n$ elements in the Hash Map before finding a matching pair.

---

## 🎯 Key Takeaways

- **Hash maps enable constant-time lookups**, allowing us to search for complements in $O(1)$ time.
- **Space-Time Trade-off:** By spending $O(n)$ auxiliary space, we drastically reduce the runtime complexity from $O(n^2)$ to $O(n)$.
- **Single-pass traversal** combined with on-the-fly hashing prevents an element from pairing with itself and handles duplicate elements seamlessly.
- **Mathematical Reformulation:** Rewriting the search equation from `x + y = target` to `y = target - x` simplifies the lookup logic.