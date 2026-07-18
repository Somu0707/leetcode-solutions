# LeetCode 504: Base 7

## Problem Summary
Given an integer `num`, return its representation as a **base 7** string. The solution must correctly handle positive integers, negative integers, and the edge case of zero.

---

## Intuition
The core mechanism of positional numeral system conversion is successive division. To convert a base-10 number to base-7, we repeatedly divide the number by 7 and collect the remainders. These remainders represent the digits of the target base from the least significant digit (rightmost) to the most significant digit (leftmost). 

To simplify the mathematical operations and avoid handling negative modulo arithmetic, we can isolate the sign of the input, perform the conversion on the absolute value, and then reapply the negative sign at the end.

---

## Approach
1. **Edge Case Handling:** If `num` is `0`, immediately return `"0"`.
2. **Sign Preservation:** Store whether the input is negative in a boolean flag `neg`, then convert `num` to its absolute value using `abs()`.
3. **Successive Division Loop:**
   - Compute `num % 7` to get the current least significant digit.
   - Convert this digit to a character (`'0' + remainder`) and append it to the result string `ans`.
   - Update `num` by dividing it by `7` (`num /= 7`).
   - Repeat until `num` becomes `0`.
4. **Post-Processing:**
   - Since digits were gathered from right to left, reverse the string `ans` to restore the correct order (most significant to least significant).
   - If the original number was negative, prepend the `"-"` character to the reversed string.
5. **Return** the final string.

---

## Dry Run
Let's dry run the algorithm with `num = -100`:

1. **Initialization:**
   - `num != 0` -> Continue.
   - `neg = true` (since `-100 < 0`).
   - `num = abs(-100) = 100`.
   - `ans = ""`.

2. **Loop Iterations:**
   - **Iteration 1:**
     - `100 % 7 = 2` -> `ans` becomes `"2"`.
     - `num = 100 / 7 = 14`.
   - **Iteration 2:**
     - `14 % 7 = 0` -> `ans` becomes `"20"`.
     - `num = 14 / 7 = 2`.
   - **Iteration 3:**
     - `2 % 7 = 2` -> `ans` becomes `"202"`.
     - `num = 2 / 7 = 0`.
   - **Loop terminates** because `num == 0`.

3. **Reversal & Sign Correction:**
   - Reverse `ans`: `"202"` reversed is `"202"`.
   - Apply sign: `neg` is `true`, so `ans = "-" + "202" = "-202"`.

**Output:** `"-202"`

---

## Time Complexity
- **$O(\log_7 |N|)$**: The number of divisions we perform is proportional to the number of digits of $N$ in base 7. Reversing the string of length $L$ takes $O(L)$ time, where $L \approx \log_7 |N|$. Thus, the overall time complexity is logarithmic.

## Space Complexity
- **$O(\log_7 |N|)$**: Auxiliary space is used to store the output string, which contains at most $\lceil \log_7(|N| + 1) \rceil + 1$ characters. If we ignore the space required for the output, the auxiliary space complexity is **$O(1)$**.

---

## Key Learning
- **String Prepending vs. Appending + Reversing:** In C++, prepending to a string (`ans = char + ans`) takes $O(L)$ time per insertion due to element shifting, resulting in an $O(L^2)$ total complexity. Appending (`ans += char`) followed by a single standard reverse operation is much more efficient, running in linear $O(L)$ time.
- **Isolating Sign Logic:** Handling negative signs up front prevents tricky edge cases associated with negative modulo operators in different programming languages.

---

## C++ Code Solution

```cpp
class Solution {
public:
    string convertToBase7(int num) {
        // Base case: 0 is represented as "0" in any base
        if (num == 0) return "0";
        
        bool neg = num < 0;
        if (neg) num = abs(num);
        
        string ans = "";
        while (num > 0) {
            ans += char('0' + num % 7);
            num /= 7;
        }
        
        // Reverse to get the correct order (most to least significant digit)
        reverse(ans.begin(), ans.end());
        
        if (neg) {
            ans = "-" + ans;
        }
        
        return ans;
    }
};
```