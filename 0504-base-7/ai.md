## 💭 Thought Process

When converting a number from decimal (base-10) to another positional numeral system like base-7, we need to understand how numbers are represented across different bases:

- In base-10, place values represent powers of $10$ ($10^0, 10^1, 10^2, \dots$).
- In base-7, place values represent powers of $7$ ($7^0, 7^1, 7^2, \dots$).

To convert a decimal number into base-7:
1. We extract the least significant digit by computing `num % 7`.
2. We then shift the number to the right by dividing it by $7$ (`num / 7`).
3. We repeat this process until the number becomes $0$.

Since the digits are extracted from right-to-left (least significant to most significant), the resulting sequence of digits must be reversed at the end.

**Handling Signs and Edge Cases:**
- Negative numbers follow the exact same base-7 magnitude conversion, with a leading `"-"` sign attached at the end. We can store whether the initial number was negative, convert the number to its absolute magnitude, and re-attach the sign at the end.
- The number `0` is a special case because a loop condition checking for `num > 0` wouldn't execute. It can be handled directly as an early exit.

---

## 💡 Intuition

The algorithm relies on mathematical repeated division:
- **Modulo Operation (`% 7`)**: Isolates the remainder, which directly corresponds to the digit for the current base-7 position.
- **Integer Division (`/ 7`)**: Reduces the number magnitude by a factor of 7, effectively discarding the digit we just processed.

Using string concatenation and a final string reversal is the most efficient way to assemble the base-7 representation because we discover the least significant digits first.

---

## 🚀 Approach

1. **Handle Zero**: Check if `num` is `0`. If so, immediately return `"0"`.
2. **Track Sign**: Record whether `num` is negative using a boolean flag, and transform `num` to its absolute value.
3. **Repeated Division**:
   - Compute `num % 7` to get the current base-7 digit.
   - Convert the digit to a character and append it to a result string.
   - Divide `num` by $7$ using integer division.
   - Continue until `num` becomes `0`.
4. **Format Result**:
   - Reverse the result string to restore the digits from most significant to least significant.
   - If the original number was negative, prepend a `"-"` sign.
5. Return the final string.

---

## 🧠 Algorithm

```text
function convertToBase7(num):
    if num is equal to 0:
        return "0"
    
    isNegative = (num < 0)
    num = absolute_value(num)
    result = ""
    
    while num > 0:
        remainder = num mod 7
        append character representation of remainder to result
        num = num / 7 (integer division)
    
    reverse(result)
    
    if isNegative is true:
        result = "-" + result
        
    return result
```

---

## 🔍 Dry Run

Let's trace the algorithm with `num = 100`:

1. **Initial State**:
   - `num = 100`
   - `isNegative = false`
   - `result = ""`

2. **Loop Iterations**:

   - **Iteration 1**:
     - `remainder` = `100 % 7` = `2`
     - Append `'2'` $\rightarrow$ `result = "2"`
     - `num` = `100 / 7` = `14`

   - **Iteration 2**:
     - `remainder` = `14 % 7` = `0`
     - Append `'0'` $\rightarrow$ `result = "20"`
     - `num` = `14 / 7` = `2`

   - **Iteration 3**:
     - `remainder` = `2 % 7` = `2`
     - Append `'2'` $\rightarrow$ `result = "202"`
     - `num` = `2 / 7` = `0`

3. **Post-Processing**:
   - Loop ends because `num == 0`.
   - Reverse `result`: `"202"` reversed is `"202"`.
   - `isNegative` is `false`, so no sign is added.

4. **Output**: `"202"`

---

## ⚠️ Edge Cases

- **Zero (`num = 0`)**: Directly handled by an early check returning `"0"`.
- **Negative Numbers (e.g., `num = -7`)**: Handled by storing the sign, taking `abs(-7) = 7`, performing conversion (`"01"` $\rightarrow$ reversed to `"10"`), and prepending `"-"` to produce `"-10"`.
- **Exact Powers of 7 (e.g., `num = 7`, `49`)**: Produces remainders of `0` correctly followed by `1` (e.g., $7 \rightarrow 10_7$).
- **Maximum/Minimum Constraints**: Handled within standard integer limits without integer overflow risks.

---

## ⏱️ Complexity Analysis

### Time Complexity: $\mathcal{O}(\log_7 |num|)$
- In each step of the loop, `num` is divided by $7$. The number of iterations is bounded by the number of digits in the base-7 representation, which is $\lfloor\log_7 |num|\rfloor + 1$.
- Reversing the string takes time proportional to the length of the string, which is also $\mathcal{O}(\log_7 |num|)$.

### Space Complexity: $\mathcal{O}(\log_7 |num|)$
- Extra space is only required to store the constructed string representing the base-7 digits, which has a length of $\mathcal{O}(\log_7 |num|)$.

---

## 🎯 Key Takeaways

- Base conversion problems are naturally solved using **repeated division and modulo operations**.
- Modulo (`%`) extracts digits from right to left (LSB to MSB), requiring a final **string reversal**.
- Separating the sign logic from magnitude calculations keeps the core conversion clean and simple.
- Repeatedly dividing a number by a constant base yields logarithmic time complexity ($\mathcal{O}(\log_{base} N)$).