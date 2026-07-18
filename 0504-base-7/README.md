# Base 7 - LeetCode 504

## Problem Summary
Given an integer `num`, return its representation as a string in **base 7**. The input can be positive, negative, or zero, and the solution must handle these edge cases gracefully while maintaining optimal performance.

---

## Intuition
The standard mathematical approach to convert a number from base 10 to any other base $B$ is **successive division**. 
By repeatedly dividing the number by $7$ and collecting the remainders, we extract the digits of the base-7 representation from the least significant digit (units place) to the most significant digit. Because this process extracts digits in reverse order, we can collect them in a string and reverse the string at the end to get the correct representation. 

---

## Approach
1. **Edge Case Handling**: If the input `num` is `0`, immediately return `"0"`.
2. **Sign Management**: Store whether the number is negative using a boolean flag `neg`. If it is negative, convert `num` to its absolute value using `abs(num)` to simplify the modulo operations.
3. **Successive Division Loop**:
   - While `num > 0`, calculate `num % 7` to get the current digit.
   - Convert this integer digit to its character equivalent by adding `'0'` and append it to our result string `ans`.
   - Update `num` by performing integer division `num /= 7`.
4. **Reconstruct the Representation**:
   - Reverse the accumulated string `ans` because digits were collected from right-to-left.
   - If the `neg` flag is true, prepend the `"-"` character.
5. **Return** the final string.

---

## Dry Run

Let's dry run the algorithm with `num = -100`:

1. **Initial State**: 
   - `num = -100` (Not zero, so we skip the `num == 0` guard).
   - `neg = true`.
   - `num = abs(-100) = 100`.
   - `ans = ""`.

2. **Loop Iterations**:
   - **Iteration 1**:
     - `num % 7` $\rightarrow 100 \pmod 7 = 2$.
     - `ans` becomes `"2"`.
     - `num` becomes $100 / 7 = 14$.
   - **Iteration 2**:
     - `num % 7` $\rightarrow 14 \pmod 7 = 0$.
     - `ans` becomes `"20"`.
     - `num` becomes $14 / 7 = 2$.
   - **Iteration 3**:
     - `num % 7` $\rightarrow 2 \pmod 7 = 2$.
     - `ans` becomes `"202"`.
     - `num` becomes $2 / 7 = 0$.
   - **Loop terminates** since `num` is now `0`.

3. **Post-Processing**:
   - Reverse `ans`: `"202"` $\rightarrow$ `"202"`.
   - `neg` is `true` $\rightarrow$ prepend `"-"` to `ans` $\rightarrow$ `"-202"`.

**Result**: `"-202"` (Correct)

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_7 |N|)$
  The number of iterations in the `while` loop is proportional to the number of digits of $N$ in base 7, which is $\lfloor\log_7 |N|\rfloor + 1$. Reversing the string takes time proportional to the length of the string, resulting in an overall logarithmic time complexity. Since $N \le 10^7$, the loop runs at most $9$ times, making this virtually $\mathcal{O}(1)$ in practice.

- **Space Complexity:** $\mathcal{O}(\log_7 |N|)$
  The auxiliary space is used solely to store the output string representation of the number. The length of this string is bounded by $\mathcal{O}(\log_7 |N|)$.

---

## Key Learning
1. **Avoid In-Loop Prepending:** Appending characters to the end of a string (`ans += ...`) and reversing it once at the end is an $\mathcal{O}(L)$ operation. Prepending characters directly inside the loop (`ans = char + ans`) forces a string shift on every iteration, leading to inefficient $\mathcal{O}(L^2)$ time complexity.
2. **Isolate Sign Logic:** Handling the negative sign upfront by caching it and working with the absolute value avoids messy modulo arithmetic with negative integers.

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