## 💭 Thought Process

When tasked with representing a base-10 integer in another base (such as base 7), we need to express the number as a sum of powers of the target base:

$$\text{num} = d_k \cdot 7^k + d_{k-1} \cdot 7^{k-1} + \dots + d_1 \cdot 7^1 + d_0 \cdot 7^0$$

To extract the digits ($d_0, d_1, \dots, d_k$):
1. Taking `num % 7` isolated the least significant digit ($d_0$), because all higher power terms ($7^1, 7^2, \dots$) are divisible by 7.
2. Dividing `num` by `7` (`num / 7`) shifts all digits one place to the right, discarding $d_0$ and making $d_1$ the new least significant digit.
3. Repeating this process until `num` reaches `0` yields all the base-7 digits.

Since this process extracts digits from right to left (least significant to most significant), the generated digit sequence will be reversed. We simply need to reverse the result string at the end and re-apply the negative sign if the original number was negative.

---

## 💡 Intuition

- **Repeated Division & Modulo**: The modulo operator (`%`) extracts the current lowest digit, while integer division (`/`) removes that digit so we can process the next power of 7.
- **Handling Signs**: Base conversions work identical for magnitude regardless of sign. By saving the sign flag and operating on `abs(num)`, we avoid dealing with negative remainders.
- **Order of Digits**: The first digit extracted is the rightmost digit of the base-7 representation. Thus, accumulating characters sequentially builds the string backwards, necessitating a final string reversal.

---

## 🚀 Approach

1. **Check for Zero**: If `num` is `0`, return `"0"` directly since the main loop wouldn't execute.
2. **Handle Negative Sign**: Store whether `num` is negative in a boolean flag, then convert `num` to its absolute value.
3. **Extract Base-7 Digits**:
   - Loop while `num > 0`.
   - Calculate `num % 7` and convert the remainder (0–6) into its character equivalent.
   - Append the character to our result string.
   - Update `num = num / 7`.
4. **Reverse the Result**: Reverse the collected string to put digits in the correct order (most significant digit first).
5. **Apply Sign**: Prepend `"-"` if the original number was negative.
6. **Return**: Return the final formatted string.

---

## 🧠 Algorithm

1. If `num` equals `0`, return `"0"`.
2. Set `is_negative` to `true` if `num < 0`, else `false`.
3. Set `num` to `abs(num)`.
4. Initialize an empty string `digits`.
5. While `num > 0`:
   - `remainder = num MOD 7`
   - Append `remainder` as a character to `digits`
   - `num = num DIV 7`
6. Reverse `digits`.
7. If `is_negative` is `true`, prepend `"-"` to `digits`.
8. Return `digits`.

---

## 🔍 Dry Run

Let's trace the algorithm with `num = 100`:

| Step | `num` | `num % 7` (Digit) | `num / 7` | Appended Character | String (`ans`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | `100` | — | — | — | `""` |
| **Iter 1** | `100` | `2` | `14` | `'2'` | `"2"` |
| **Iter 2** | `14` | `0` | `2` | `'0'` | `"20"` |
| **Iter 3** | `2` | `2` | `0` | `'2'` | `"202"` |

- **Loop terminates** because `num` becomes `0`.
- **Reverse string**: `"202"` reversed is `"202"`.
- **Check sign**: `num` was positive, so no `"-"` is prepended.
- **Final Output**: `"202"`

---

## ⚠️ Edge Cases

- **Zero (`num = 0`)**: The loop condition `num > 0` fails immediately for zero. The initial check explicitly catches this and returns `"0"`.
- **Negative Numbers**: Extracted cleanly by taking `abs(num)` and appending `"-"` after digit extraction and string reversal.
- **Single-Digit Base-7 Numbers ($0 \le |num| \le 6$)**: The loop runs exactly once, generating a single character string which reverses to itself correctly.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$O(\log_7 |N|)$**: The algorithm divides `num` by $7$ in each step. The number of digits in base $7$ for a number $N$ is $\lfloor \log_7 |N| \rfloor + 1$. Reversing a string of length $L = \log_7 |N|$ takes $O(L)$ time. Hence, the total time complexity is logarithmic.

### Space Complexity
- **$O(\log_7 |N|)$**: The auxiliary space is used to store the output string, which holds at most $\lceil \log_7 |N| \rceil + 2$ characters (including potential minus sign).

---

## 🎯 Key Takeaways

- Base conversion problems are naturally solved using repeated **modulo** (to extract digits) and **integer division** (to shift digits).
- Modulo operations extract digits from **least significant to most significant**, making a final string reversal necessary.
- Separating sign logic (`abs()`) from base arithmetic prevents edge cases involving negative remainder definitions across different programming languages.
- The number of iterations required to convert a number $N$ into base $B$ is proportional to $O(\log_B N)$.