# 2. Add Two Numbers

<div align="center">

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-brightgreen)
![Acceptance](https://img.shields.io/badge/Acceptance-48.92%25-blue)
![Topics](https://img.shields.io/badge/Topics-3-orange)

</div>

---

# 📝 Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

# 📚 Examples

## Example 1

![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

## Example 2

```
Input: l1 = [0], l2 = [0]
Output: [0]
```

## Example 3

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

---

# 📌 Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.



---

# 🧠 AI Solution Explanation

## 💭 Thought Process

When approaching this problem, a naive first attempt might be to convert both linked lists into standard integer types, add them together, and then construct a new linked list from the resulting sum. 

However, this approach quickly fails due to variable size limits. The problem constraints state that lists can contain up to 100 nodes. A 100-digit number far exceeds the capacity of standard 64-bit primitive types (`long long` or `unsigned long long`), leading to integer overflow.

By observing how addition is performed by hand, we notice that digits are processed from right to left (least significant to most significant), keeping track of a carry value. Since the problem naturally gives us the numbers in **reverse order**, the heads of the lists represent the least significant digits. This allows us to simulate elementary school addition digit-by-digit in a single pass without needing to convert the entire list into an integer.

---

## 💡 Intuition

The core insight is to traverse both linked lists simultaneously from head to tail, building a new linked list digit-by-digit while maintaining a running `carry`.

- **Digit-by-digit simulation**: At any position, the new digit's value is `(val1 + val2 + carry) % 10`.
- **Carry propagation**: The new carry value transferred to the next higher place value is `(val1 + val2 + carry) / 10`.
- **Dummy Node Pattern**: Using a sentinel (dummy) node at the beginning simplifies pointer management, eliminating the need for special checks when inserting the very first node of the result list.

---

## 🚀 Approach

1. **Initialize Helpers**: Create a `dummy` node to serve as the anchor for the result list, and maintain a pointer `temp` to track the tail of the new list. Initialize `carry` to `0`.
2. **Iterate with Conditions**: Traverse as long as there is still a node to process in `l1`, a node in `l2`, or a remaining `carry > 0`.
3. **Calculate Current Sum**:
   - Extract the value from `l1` if `l1` is not null, then move `l1` forward.
   - Extract the value from `l2` if `l2` is not null, then move `l2` forward.
   - Add the previous `carry` to the sum.
4. **Update Carry and Create Node**:
   - Calculate the new carry: `carry = sum / 10`.
   - Create a new node with value `sum % 10` and append it to `temp.next`.
   - Advance `temp` to point to the newly added node.
5. **Return Result**: Return `dummy.next`, which points to the actual head of the sum list.

---

## 🧠 Algorithm

1. Initialize `dummy` node, set `temp = dummy`, and set `carry = 0`.
2. While `l1` is not null OR `l2` is not null OR `carry` is not 0:
    1. Set `sum = carry`.
    2. If `l1` is not null:
        - Add `l1.val` to `sum`.
        - Advance `l1 = l1.next`.
    3. If `l2` is not null:
        - Add `l2.val` to `sum`.
        - Advance `l2 = l2.next`.
    4. Update `carry = sum / 10`.
    5. Create `newNode` with value `sum % 10`.
    6. Attach `temp.next = newNode` and advance `temp = temp.next`.
3. Return `dummy.next`.

---

## 🔍 Dry Run

Let's walk through an example: `l1 = [2, 4, 3]` and `l2 = [5, 6, 4]`.

| Iteration | `l1.val` | `l2.val` | Incoming `carry` | Total `sum` | New Digit (`sum % 10`) | New `carry` (`sum / 10`) | Result List State |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Start** | - | - | - | - | - | 0 | `[]` |
| **1** | 2 | 5 | 0 | $2 + 5 + 0 = 7$ | **7** | **0** | `[7]` |
| **2** | 4 | 6 | 0 | $4 + 6 + 0 = 10$ | **0** | **1** | `[7 -> 0]` |
| **3** | 3 | 4 | 1 | $3 + 4 + 1 = 8$ | **8** | **0** | `[7 -> 0 -> 8]` |

**End Condition**: `l1` is NULL, `l2` is NULL, and `carry` is 0. Traversal ends.
**Output**: `[7, 0, 8]` (representing $342 + 465 = 807$).

---

## ⚠️ Edge Cases

- **Unequal Length Lists**: One list runs out of nodes before the other (e.g., `[9, 9]` + `[1]`). Handled by checking `l1 != NULL` and `l2 != NULL` independently; missing nodes default to `0`.
- **Extra Carry at the End**: The addition produces a carry that extends the result length (e.g., `[5]` + `[5]` = `[0, 1]`). Including `carry` in the `while` loop condition ensures a final node is created for any remaining carry.
- **Single Zero Inputs**: `[0]` + `[0]` outputs `[0]` correctly without looping infinitely.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$\mathcal{O}(\max(N, M))$**: Where $N$ is the number of nodes in `l1` and $M$ is the number of nodes in `l2`. The loop runs at most $\max(N, M) + 1$ times because we process each node from both lists at most once.

### Space Complexity
- **$\mathcal{O}(\max(N, M))$**: The algorithm creates a new linked list to store the result, which contains at most $\max(N, M) + 1$ nodes. Auxiliary pointer space is $\mathcal{O}(1)$.

---

## 🎯 Key Takeaways

- **Simulate Basic Arithmetic**: Complex large-number additions can be performed digit-by-digit to avoid integer overflow issues.
- **Dummy Heads Simplify Lists**: Using dummy nodes removes redundant dynamic memory edge-case handling for the head node.
- **Loop Condition Flexibility**: Combining multiple exit conditions (`l1`, `l2`, and `carry`) inside a single `while` loop reduces code duplication.

---

# 💻 C++ Solution

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
         ListNode *dummy = new ListNode(); 
        ListNode *temp = dummy; 
        
        int carry = 0;
        
        while( (l1 != NULL || l2 != NULL) || carry) {
            int sum = 0; 
            if(l1 != NULL) {
                sum += l1->val; 
                l1 = l1 -> next; 
            }
            
            if(l2 != NULL) {
                sum += l2 -> val; 
                l2 = l2 -> next; 
            }
            
            sum += carry; 
            carry = sum / 10; 
            ListNode *node = new ListNode(sum % 10); 
            temp -> next = node; 
            temp = temp -> next; 
        }
        return dummy -> next; 
    }
};
```

---

## 🚀 Repository

⭐ If you found this explanation helpful, consider starring the repository.

Happy Coding! 🚀