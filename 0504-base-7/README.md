# 504. Base 7

<div align="center">

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Acceptance](https://img.shields.io/badge/Acceptance-54.9%25-blue)
![Topics](https://img.shields.io/badge/Topics-2-orange)

</div>

---

# 📝 Problem Statement

Given an integer `num`, return *a string of its base 7 representation*.

---

# 📚 Examples

## Example 1

```
Input: num = 100
Output: "202"
```

## Example 2

```
Input: num = -7
Output: "-10"
```

---

# 📌 Constraints

- `-10⁷ <= num <= 10⁷`



---

# 🧠 AI Solution Explanation

## 💭 Thought Process

When tasked with converting a base-10 integer to another base (in this case, base 7), we need to recall how number systems work. In base 10, each digit position represents a power of 10. Similarly, in base 7, each digit position represents a power of 7.

To convert a decimal number to base 7 manually:
1. We repeatedly divide the number by 7.
2. The remainder at each step represents the current least significant digit (LSD) in base 7.
3. The quotient becomes the new number for the next iteration.
4. We stop when the quotient reaches zero.

Since remainder extraction produces digits from right-to-left (least significant to most significant), the resulting sequence of remainders must be reversed to form the final representation.

Additionally, we must consider sign management. A negative sign can simply be extracted beforehand, allowing us to perform the base conversion on the positive magnitude and attach the sign back at the end.

---

## 💡 Intuition

The core insight is that taking a number modulo 7 (`num % 7`) extracts its rightmost base-7 digit, while integer division by 7 (`num / 7`) shifts all base-7 digits one position to the right.

- **Why does this work?** Any integer $N$ can be expressed as:
  $$N = a_k \cdot 7^k + a_{k-1} \cdot 7^{k-1} + \dots + a_1 \cdot 7^1 + a_0 \cdot 7^0$$
  where $0 \le a_i < 7$. Taking $N \pmod 7$ isolates $a_0$. Dividing by 7 shifts $a_1$ into the $7^0$ position, making it ready for the next extraction.

- **Why handle zero separately?** The standard division loop (`while num > 0`) will not execute if `num = 0`. Explicitly checking for zero upfront prevents returning an empty string.

---

## 🚀 Approach

1. **Handle Zero Case**: Check if `num` is `0`. If so, immediately return `"0"`.
2. **Handle Negative Numbers**: Record whether `num` is negative using a flag, then convert `num` to its absolute value to simplify remainder calculations.
3. **Repeated Division and Modulo**:
   - Loop while `num > 0`.
   - Calculate `num % 7` and convert the remainder to its character representation.
   - Append this character to a result string.
   - Update `num` to `num / 7`.
4. **Final Assembly**:
   - Reverse the result string so digits are in order from most significant to least significant.
   - Prepend `"-"` if the original number was negative.
5. **Return** the final string.

---

## 🧠 Algorithm

```text
1. IF num is 0:
    RETURN "0"

2. SET is_negative = (num < 0)
3. SET num = absolute_value(num)
4. INITIALIZE empty string digits

5. WHILE num > 0:
    a. digit = num MOD 7
    b. APPEND character representation of digit TO digits
    c. num = num DIV 7

6. REVERSE digits

7. IF is_negative:
    PREPEND "-" TO digits

8. RETURN digits
```

---

## 🔍 Dry Run

Let's trace the algorithm with **`num = 100`**:

| Step | `num` | `num % 7` (Remainder) | `num / 7` (Quotient) | Appended Char | Accumulated String |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | `100` | — | — | — | `""` |
| **Iter 1** | `100` | `2` | `14` | `'2'` | `"2"` |
| **Iter 2** | `14` | `0` | `2` | `'0'` | `"20"` |
| **Iter 3** | `2` | `2` | `0` | `'2'` | `"202"` |

- **Loop Terminated**: `num` becomes `0`.
- **Reverse String**: Reversing `"202"` yields `"202"`.
- **Sign Check**: `is_negative` is `false`, so no `"-"` prepended.
- **Output**: `"202"`.

---

## ⚠️ Edge Cases

- **`num = 0`**: The standard loop won't run because `num > 0` is false. Handled by an early return `"0"`.
- **Negative Inputs (e.g., `num = -7`)**: Handled by storing the sign flag and using `abs(num)`. `-7` correctly converts to `"-10"`.
- **Powers of 7 (e.g., `num = 7`)**: Correctly produces remainders `0` then `1`, yielding `"10"` after reversal.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$\mathcal{O}(\log_7 |num|)$**: In each iteration, `num` is divided by 7. The total number of loop iterations is proportional to the number of base-7 digits, which is $\lfloor \log_7 |num| \rfloor + 1$. Reversing a string of length at most 10 takes $\mathcal{O}(1)$ time.

### Space Complexity
- **$\mathcal{O}(\log_7 |num|)$**: The space required is strictly for storing the output string, which contains at most $\approx 10$ characters given the problem constraints ($-10^7 \le num \le 10^7$).

---

## 🎯 Key Takeaways

- Base conversion algorithms rely on repeated division (`/`) and remainder extraction (`%`).
- Extracting remainders yields digits from **Least Significant Digit (LSD)** to **Most Significant Digit (MSD)**, requiring a string reversal at the end.
- Separating the sign logic from the conversion magnitude simplifies edge case management for negative numbers.

---

# 💻 C++ Solution

```cpp
class Solution {
public:
    string convertToBase7(int num) {
        if(num == 0) return "0";
        bool neg=num<0;
        if(neg) num = abs(num);
       string ans="";
        while(num>0){
            ans += char('0'+num%7);
            num /=7;
        }
        reverse(ans.begin(), ans.end());
        if(neg) 
            ans = "-"+ans;
        return ans;
    }
};
```

---

## 🚀 Repository

⭐ If you found this explanation helpful, consider starring the repository.

Happy Coding! 🚀