# LeetCode 504: Base 7

## Problem Summary
Given an integer `num`, return its representation as a **base 7** string. The input integer can be positive, negative, or zero, and the solution must handle these sign constraints accurately.

---

## Intuition
To convert a number from base 10 to any other base (in this case, base 7), we use the standard **successive division method**. By repeatedly dividing the number by 7 and collecting the remainders, we extract the digits of the target base from the least significant digit (rightmost) to the most significant digit (leftmost). Since we generate the digits in reverse order, we must reverse the final string to get the correct representation.

---

## Approach
1. **Edge Case Handling**: If the input `num` is `0`, return `"0"` immediately.
2. **Sign Tracking**: Store whether the number is negative using a boolean flag `neg`. Convert `num` to its absolute value to simplify modulo and division arithmetic.
3. **Successive Division**:
   - Loop while `num > 0`.
   - Compute the remainder `num % 7`, convert it to a character (`char('0' + remainder)`), and append it to the result string `ans`.
   - Update `num` by dividing it by 7 (`num /= 7`).
4. **Reverse and Sign Restore**: 
   - Reverse the accumulated string `ans` because the digits were gathered from right to left.
   - If the original number was negative, prepend the `"-"` character to the reversed string.
5. **Return** the final string.

---

## Dry Run
Let's dry run the algorithm with input `num = -100`:

1. **Sign Check**: `num < 0` is `true`. We set `neg = true` and `num = abs(-100) = 100`.
2. **Iteration 1**:
   - `num % 7 = 100 % 7 = 2` $\rightarrow$ `ans = "2"`
   - `num = 100 / 7 = 14`
3. **Iteration 2**:
   - `num % 7 = 14 % 7 = 0` $\rightarrow$ `ans = "20"`
   - `num = 14 / 7 = 2`
4. **Iteration 3**:
   - `num % 7 = 2 % 7 = 2` $\rightarrow$ `ans = "202"`
   - `num = 2 / 7 = 0` (Loop terminates)
5. **Reversal**: Reversing `"202"` gives `"202"`.
6. **Apply Sign**: Since `neg` is `true`, we prepend `"-"` $\rightarrow$ `"-202"`.

**Output**: `"-202"`

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_7 |N|)$  
  The number of iterations in the loop is proportional to the number of digits of `num` in base 7, which is $\lfloor\log_7 |N|\rfloor + 1$. Reversing the string also takes linear time relative to its length, making the overall time complexity logarithmic.

- **Space Complexity:** $\mathcal{O}(\log_7 |N|)$  
  The auxiliary space is used to store the output string, which requires space proportional to the number of digits in the base 7 representation of the input.

---

## Key Learning
- **Mathematical Base Conversion**: The technique of using `% Base` and `/ Base` is the foundational template for converting any integer to any base representation (Base 2, Base 8, Base 16, etc.).
- **Boundary Conditions**: Isolating the negative sign early simplifies the mathematical operations inside the loop and prevents negative modulo bugs in C++.
- **ASCII Offsetting**: Converting a numeric digit `d` (where $0 \le d \le 6$) to its character representation is cleanly done via `char('0' + d)`.

---

## C++ Solution

```cpp
class Solution {
public:
    string convertToBase7(int num) {
        if(num == 0) return "0";
        bool neg = num < 0;
        if(neg) num = abs(num);
        string ans = "";
        while(num > 0){
            ans += char('0' + num % 7);
            num /= 7;
        }
        reverse(ans.begin(), ans.end());
        if(neg) 
            ans = "-" + ans;
        return ans;
    }
};
```