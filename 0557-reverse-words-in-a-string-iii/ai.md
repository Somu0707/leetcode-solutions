## 💭 Thought Process

When approaching this problem, a naive or brute-force approach might be to split the sentence by space delimiters into an array of individual words, reverse each word string independently, and then join them back together with spaces. 

While this works, creating temporary arrays and intermediate string objects consumes extra memory.

To optimize, we can observe that:
1. The relative order of words and spaces remains unchanged.
2. Words are clearly bounded by spaces or the ends of the string.

This observation suggests that we don't need to reconstruct the string from scratch. Instead, we can scan the string, identify the start and end indices of each individual word, and reverse the characters of that word directly in-place using a standard two-pointer reversal approach.

---

## 💡 Intuition

The key insight is **delimiter-based range reversal**.

- **Tracking Boundaries:** By maintaining a pointer (or index) to mark where the current word begins, whenever we encounter a space, we know the word has ended just before that space.
- **In-Place Transformation:** Reversing a range within a string takes time proportional to the length of that range. By performing this range reversal in-place as we discover each word, we eliminate the need for extra memory structures.
- **Handling the Last Word:** Since the sentence does not end with a space, the last word won't trigger the space-check condition inside the loop. Reversing the remaining segment after the loop completes guarantees that every word is processed.

---

## 🚀 Approach

1. Initialize a pointer `prev` to `0`, which keeps track of the start index of the current word.
2. Iterate through the string character by character using an index `i`.
3. When `s[i]` is a space `' '`:
   - Reverse the segment of the string starting from index `prev` up to index `i - 1`.
   - Set `prev` to `i + 1` to mark the starting position of the next word.
4. After the iteration finishes, reverse the final segment from index `prev` to the end of the string.
5. Return the modified string.

---

## 🧠 Algorithm

1. Set `prev = 0` and `n = length(s)`.
2. Loop `i` from `0` to `n - 1`:
   - If `s[i] == ' '`:
     - Reverse characters in range `[prev, i - 1]`.
     - Update `prev = i + 1`.
3. Reverse characters in range `[prev, n - 1]`.
4. Return `s`.

---

## 🔍 Dry Run

Let's trace the algorithm with `s = "Mr Ding"`:

- **Initial State:** `n = 7`, `prev = 0`

| Step | Index `i` | Character `s[i]` | Action / Condition | String State | `prev` Value |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0` | `'M'` | Continue scanning | `"Mr Ding"` | `0` |
| 2 | `1` | `'r'` | Continue scanning | `"Mr Ding"` | `0` |
| 3 | `2` | `' '` | Space found! Reverse `s[0...1]` | `"rM Ding"` | `3` (`i + 1`) |
| 4 | `3` | `'D'` | Continue scanning | `"rM Ding"` | `3` |
| 5 | `4` | `'i'` | Continue scanning | `"rM Ding"` | `3` |
| 6 | `5` | `'n'` | Continue scanning | `"rM Ding"` | `3` |
| 7 | `6` | `'g'` | Continue scanning | `"rM Ding"` | `3` |

- **End of Loop:** Scanner finishes at `i = 7`.
- **Post-Loop Action:** Reverse final range `s[prev...n-1]`, which is `s[3...6]` (`"Ding"` $\rightarrow$ `"gniD"`).
- **Final Result:** `"rM gniD"`

---

## ⚠️ Edge Cases

- **Single Word (No spaces):** The loop executes without finding any spaces. The post-loop reversal reverses the entire string correctly.
- **Single-Character Words:** For single-character words (e.g., `"a b c"`), reversing a range where start equals end leaves the character unchanged.
- **Length 1 String:** Handled gracefully; loop finishes and post-loop reverses a single character without error.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$O(N)$**, where $N$ is the length of the string.
- Each character is traversed once during the linear scan and swapped at most once during the range reversals.

### Space Complexity
- **$O(1)$** auxiliary space.
- The string is modified in-place without allocating additional dynamic memory structures.

---

## 🎯 Key Takeaways

- **Two-Pointer Reversal:** Reversing a range in-place is an efficient operation requiring constant auxiliary space.
- **Boundary Detection:** Space characters act as natural delimiters to identify word ranges during traversal.
- **Handling Post-Loop Cleanup:** Always remember to process remaining elements after a loop when using delimiter-triggered logic.