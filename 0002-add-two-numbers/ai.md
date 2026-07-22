## 💭 Thought Process

When approaching this problem, a naive strategy might be to convert both linked lists into standard integers, sum them up, and then convert the result back into a linked list. 

However, this brute-force approach quickly fails. The problem constraints state that each linked list can contain up to 100 nodes. A 100-digit number far exceeds the storage capacity of standard primitive data types such as `long long` or 64-bit integers, leading to arithmetic overflow.

To solve this efficiently without integer overflow, we can make an important observation: **the digits are stored in reverse order**. This means the head of each linked list contains the least significant digit (the ones place). 

This reverse alignment is advantageous because standard arithmetic addition also starts from the least significant digit and works its way to the left while maintaining a `carry`. Thus, we can process both lists node-by-node simultaneously, adding corresponding digits along with any carry from the previous step.

---

## 💡 Intuition

The algorithm mimics elementary school addition:

- We traverse both linked lists starting from their heads (the least significant digits).
- At each step, we sum the values of the current nodes along with a `carry` variable.
- The new digit for our result list is `sum % 10`.
- The updated carry for the next position is `sum / 10`.
- A **dummy head node** is used to simplify building the output linked list, avoiding unnecessary conditional checks for the head node.

This approach ensures we process each digit in constant time without needing to store the entire giant integer in memory.

---

## 🚀 Approach

1. **Initialize Helpers**: Create a `dummy` node to serve as the start of the result list, a pointer `temp` to track the tail of the new list, and an integer `carry` set to `0`.
2. **Iterate Through Lists**: Continue looping as long as `l1` is not empty, `l2` is not empty, OR `carry` is greater than `0`.
3. **Calculate Digit Sum**:
   - Extract `l1.val` if `l1` exists, otherwise use `0`.
   - Extract `l2.val` if `l2` exists, otherwise use `0`.
   - Add these values along with `carry` to calculate `sum`.
4. **Update Carry and Result List**:
   - Compute new `carry` as `sum / 10`.
   - Create a new node with value `sum % 10` and append it to `temp.next`.
   - Move `temp` forward.
5. **Advance Pointers**: Move `l1` and `l2` to their respective next nodes if available.
6. **Return Result**: Return `dummy.next`, which points to the head of the newly formed list.

---

## 🧠 Algorithm

1. Initialize `dummy = Node(0)`, `temp = dummy`, and `carry = 0`.
2. While `l1 != null` OR `l2 != null` OR `carry > 0`:
   1. Set `sum = carry`.
   2. If `l1` is not null:
      - `sum = sum + l1.val`
      - `l1 = l1.next`
   3. If `l2` is not null:
      - `sum = sum + l2.val`
      - `l2 = l2.next`
   4. `carry = sum / 10`
   5. `temp.next = Node(sum % 10)`
   6. `temp = temp.next`
3. Return `dummy.next`.

---

## 🔍 Dry Run

Let's trace the algorithm using `l1 = [2, 4, 3]` (representing 342) and `l2 = [5, 6, 4]` (representing 465):

| Step | `l1.val` | `l2.val` | `carry` (In) | `sum` | `sum % 10` (New Node) | `carry` (Out) | Output List |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | - | - | 0 | - | - | 0 | `[]` |
| **1** | 2 | 5 | 0 | 2 + 5 + 0 = 7 | 7 | 0 | `[7]` |
| **2** | 4 | 6 | 0 | 4 + 6 + 0 = 10 | 0 | 1 | `[7, 0]` |
| **3** | 3 | 4 | 1 | 3 + 4 + 1 = 8 | 8 | 0 | `[7, 0, 8]` |

**Termination**: Both `l1` and `l2` are `null`, and `carry` is `0`. Loop ends.  
**Result**: The returned list is `[7, 0, 8]` (representing 807), which is correct.

---

## ⚠️ Edge Cases

- **Unequal List Lengths**: One list may be longer than the other (e.g., `[9, 9]` + `[1]`). Missing values are treated as `0`.
- **Remaining Carry at the End**: Adding `[9, 9]` and `[1]` produces `[0, 0, 1]`. The loop condition `carry > 0` ensures the final carry creates an additional node at the end.
- **Single Element Zeroes**: Input like `[0]` + `[0]` correctly outputs `[0]`.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$\mathcal{O}(\max(N, M))$**: Where $N$ and $M$ are the lengths of `l1` and `l2` respectively. We iterate at most $\max(N, M) + 1$ times since we process one node from each list per iteration.

### Space Complexity
- **$\mathcal{O}(\max(N, M))$**: The length of the new linked list is at most $\max(N, M) + 1$ to store the result nodes.

---

## 🎯 Key Takeaways

- Dummy head nodes simplify linked list construction by removing boundary condition checks for the head node.
- Simulating digit-by-digit math avoids standard integer overflow issues when dealing with large numbers.
- Including condition flags like `carry > 0` directly in the loop head avoids duplicate code after traversal ends.
- Aligning problem representation (reverse order) with algorithmic direction often drastically simplifies implementation.