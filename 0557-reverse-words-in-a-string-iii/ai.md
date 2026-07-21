## 💭 Thought Process

When approaching this problem, a naive idea might be to split the sentence into a list of individual words using whitespace as a delimiter, reverse each word independently, and then join them back together with single spaces. 

While this split-and-join approach works, it requires creating new string arrays and extra intermediate string copies, leading to additional memory overhead.

To optimize space, we can observe that:
1. The relative ordering of words stays fixed.
2. The spaces between words remain in their exact original positions.

This means we don't need to rebuild the sentence from scratch. Instead, we can scan through the string in-place, identify the start and end boundaries of each word, and reverse the characters directly within those boundaries.

---

## 💡 Intuition

The core insight is that a word is simply a sequence of non-space characters bounded either by spaces or by the ends of the string.

By maintaining a pointer to track the starting index of the current word, we can scan forward until we hit a space character. That space signals the end of the word. Once a word boundary is identified, we can perform an in-place two-pointer reversal on that specific subsegment.

This approach allows us to process the entire string in a single pass without allocating additional dynamic memory.

---

## 🚀 Approach

1. Maintain an index `prev` to track the start of the current word (initialized to `0`).
2. Traverse the string character by character using an index `i`.
3. Whenever `s[i]` encounters a space character `' '`:
   - Reverse the characters in the range `[prev, i - 1]`.
   - Update `prev` to `i + 1` to mark the start of the next word.
4. After the traversal loop completes, the last word will remain unreversed because there is no trailing space to trigger the condition.
5. Perform a final reversal on the remaining substring from `prev` to the end of the string.
6. Return the modified string.

---

## 🧠 Algorithm

1. Initialize `prev = 0`.
2. For each index `i` from `0` to `s.length - 1`:
   - If `s[i]` is equal to `' '`:
     - Reverse elements in range `[prev, i - 1]`.
     - Set `prev = i + 1`.
3. Reverse elements in range `[prev, s.length - 1]`.
4. Return `s`.

---

## 🔍 Dry Run

Let's trace the algorithm with `s = "Mr Ding"`:

- **Initial State**: `s = "Mr Ding"`, `length = 7`, `prev = 0`

| Step | `i` | `s[i]` | Action | String State | `prev` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` | `'M'` | Continue scanning | `"Mr Ding"` | `0` |
| 2 | `1` | `'r'` | Continue scanning | `"Mr Ding"` | `0` |
| 3 | `2` | `' '` | Space found! Reverse `[0, 1]` ("Mr" $\rightarrow$ "rM") | `"rM Ding"` | `3` |
| 4 | `3` | `'D'` | Continue scanning | `"rM Ding"` | `3` |
| 5 | `4` | `'i'` | Continue scanning | `"rM Ding"` | `3` |
| 6 | `5` | `'n'` | Continue scanning | `"rM Ding"` | `3` |
| 7 | `6` | `'g'` | Continue scanning | `"rM Ding"` | `3` |

- **Post Loop**:
  - Reached end of string. Reverse remaining segment from `prev = 3` to `6` ("Ding" $\rightarrow$ "gniD").
  - Final string: `"rM gniD"`

---

## ⚠️ Edge Cases

- **Single Word Input** (e.g., `"Hello"`): No spaces are encountered during iteration. The loop finishes and the final post-loop step reverses the entire single word correctly.
- **Single Character Words** (e.g., `"A B C"`): Reversing a range where the start and end indices are equal is a harmless no-op, preserving single characters as expected.
- **No Trailing Spaces**: The problem guarantees single spaces between words and no trailing spaces, so handling the last word explicitly after the loop fully covers boundary conditions.

---

## ⏱️ Complexity Analysis

### Time Complexity
$\mathcal{O}(N)$, where $N$ is the length of the string. 
- The linear scan visits each character once ($\mathcal{O}(N)$).
- Reversing each character swaps elements at most once across all word reversals ($\mathcal{O}(N)$ total).
- Overall time complexity remains linear.

### Space Complexity
$\mathcal{O}(1)$ auxiliary space.
- The reversal operations are done in-place within the existing string memory, requiring no additional data structures.

---

## 🎯 Key Takeaways

- In-place string manipulations save space by eliminating unnecessary temporary allocations.
- Boundary detection using pointers allows efficient processing of segmented structures like sentences.
- Always remember to handle trailing segments after loop termination when splitting by delimiters.