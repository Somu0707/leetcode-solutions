# 557. Reverse Words in a String III

<div align="center">

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Acceptance](https://img.shields.io/badge/Acceptance-84.08%25-blue)
![Topics](https://img.shields.io/badge/Topics-2-orange)

</div>

---

# 📝 Problem Statement

Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

---

# 📚 Examples

## Example 1

```
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```

## Example 2

```
Input: s = "Mr Ding"
Output: "rM gniD"
```

---

# 📌 Constraints

- `1 <= s.length <= 5 * 10⁴`
- `s` contains printable ASCII characters.
- `s` does not contain any leading or trailing spaces.
- There is at least one word in `s`.
- All the words in `s` are separated by a single space.



---

# 🧠 AI Solution Explanation

## 💭 Thought Process

When approaching this problem, a naive idea might be to split the sentence into an array of words using space as a delimiter, reverse each word individually, and then join them back together with spaces.

While this works, splitting and creating new string objects requires extra memory and array allocations. 

Instead, we can observe that:
1. Words are separated by single spaces.
2. The sequence and positions of the spaces remain unchanged.
3. We only need to flip characters locally between word boundaries.

This leads us to an optimal **In-Place Two-Pointer / Index Tracking** strategy. By identifying the start and end indices of each word during a single pass, we can reverse each word directly within the string without allocating extra memory for arrays of words.

---

## 💡 Intuition

The key insight is treating each word as an independent sub-segment defined by two boundaries:
- The **start index** of the word.
- The **end index** of the word (either right before a space or at the end of the string).

By traversing the string character by character:
- A space character serves as a natural boundary signal indicating that the current word has ended.
- Reversing a word locally inside its boundary does not affect surrounding words or spaces.
- Performing the reversal in-place avoids extra memory overhead.

---

## 🚀 Approach

1. Maintain a pointer `prev` initialized to `0` to keep track of the start index of the current word.
2. Iterate through the string character by character.
3. When a space character is encountered at index `i`:
   - Reverse the characters in the range `[prev, i - 1]`.
   - Move `prev` to `i + 1` to mark the beginning of the next word.
4. After the loop finishes, reverse the remaining range `[prev, length - 1]` to process the final word (which isn't followed by a space).
5. Return the modified string.

---

## 🧠 Algorithm

1. Initialize `prev = 0` and `N = length of string`.
2. Loop `i` from `0` to `N - 1`:
   - If character at `i` is a space `' '`:
     - Reverse substring from index `prev` to `i - 1`.
     - Update `prev = i + 1`.
3. Reverse substring from index `prev` to `N - 1` (handles the last word).
4. Return the modified string.

---

## 🔍 Dry Run

Let's trace the algorithm with `s = "Mr Ding"`:

- **Initial State:** `s = "Mr Ding"`, `N = 7`, `prev = 0`

| Index `i` | Character `s[i]` | Action | String `s` | `prev` Value |
| :---: | :---: | :--- | :--- | :---: |
| `0` | `'M'` | Continue | `"Mr Ding"` | `0` |
| `1` | `'r'` | Continue | `"Mr Ding"` | `0` |
| `2` | `' '` | Space detected! Reverse range `[0, 1]` (`"Mr"` $\rightarrow$ `"rM"`). Update `prev = 2 + 1 = 3`. | `"rM Ding"` | `3` |
| `3` | `'D'` | Continue | `"rM Ding"` | `3` |
| `4` | `'i'` | Continue | `"rM Ding"` | `3` |
| `5` | `'n'` | Continue | `"rM Ding"` | `3` |
| `6` | `'g'` | Continue | `"rM Ding"` | `3` |

- **End of Loop:** 
  - Perform post-loop reversal for the last word from `prev = 3` to end `6` (`"Ding"` $\rightarrow$ `"gniD"`).
- **Final Result:** `"rM gniD"`

---

## ⚠️ Edge Cases

- **Single Word (No spaces):** The loop runs without detecting spaces, and the post-loop step correctly reverses the entire single word.
- **Single Character Words:** Reversing a single character is a no-op, which the algorithm handles seamlessly without index errors.
- **Words at String Boundaries:** The last word isn't followed by a space, which is explicitly handled by the post-loop reversal step.

---

## ⏱️ Complexity Analysis

### Time Complexity
$\mathcal{O}(N)$, where $N$ is the length of the string. We iterate through the string once to locate spaces. Each character is involved in a reversal swap at most once, making the overall time complexity strictly linear.

### Space Complexity
$\mathcal{O}(1)$ Auxiliary Space. The algorithm modifies the string in-place using two-pointer indices without allocating extra space for arrays or additional strings.

---

## 🎯 Key Takeaways

- Delimiter-based parsing allows processing data in chunks without full string tokenization.
- In-place two-pointer operations eliminate auxiliary space overhead for string manipulations.
- Always remember to handle post-loop remaining elements when processing delimiter-separated sequences.

---

# 💻 C++ Solution

```cpp
class Solution {
public:
    string reverseWords(string s) {
        int n = s.length();
        int prev = 0;
        for(int i=0;i<n;i++){
            if(s[i]==' '){
                reverse(s.begin()+prev,s.begin()+i);
                 prev = i+1;
            }
           
        }
        reverse(s.begin()+prev,s.end());
        return s;
    }
};
```

---

## 🚀 Repository

⭐ If you found this explanation helpful, consider starring the repository.

Happy Coding! 🚀