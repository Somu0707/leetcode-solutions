# 876. Middle of the Linked List

<div align="center">

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Acceptance](https://img.shields.io/badge/Acceptance-82.15%25-blue)
![Topics](https://img.shields.io/badge/Topics-2-orange)

</div>

---

# 📝 Problem Statement

Given the `head` of a singly linked list, return *the middle node of the linked list*.

If there are two middle nodes, return the second middle node.

---

# 📚 Examples

## Example 1

![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg)

```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```

## Example 2

![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg)

```
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```

---

# 📌 Constraints

- The number of nodes in the list is in the range `[1, 100]`.
- `1 <= Node.val <= 100`



---

# 🧠 AI Solution Explanation

## 💭 Thought Process

When faced with the problem of finding the middle node of a linked list, a natural first approach is to count the total number of nodes:

1. **Brute Force Approach (Two-Pass):**
   - Perform a first pass through the linked list to count the total length $N$.
   - Calculate the target middle index as $N / 2$.
   - Perform a second pass from the head up to the index $N / 2$ to reach the middle node.

While this approach works and runs in $O(N)$ time, it requires traversing the list twice. 

2. **Optimal Approach (Single-Pass):**
   - Can we find the middle node in just **one** traversal?
   - Notice that if one entity moves twice as fast as another, when the faster entity reaches the finish line, the slower entity will be exactly halfway through the journey.
   - This leads directly to the **Two-Pointer Strategy** (also known as the *Fast and Slow Pointer* or *Tortoise and Hare* algorithm).

---

## 💡 Intuition

The core insight relies on setting up two pointers starting at the same position, moving at different speeds:
- A **Slow Pointer** moving $1$ step at a time.
- A **Fast Pointer** moving $2$ steps at a time.

Because the fast pointer covers distance at twice the speed of the slow pointer:
- When the fast pointer reaches the end of the list (i.e., `null`), the slow pointer will be positioned exactly halfway through the list.
- For lists with an even number of elements, this natural movement lands the slow pointer directly on the **second middle node**, satisfying the problem requirements cleanly without extra logic.

---

## 🚀 Approach

1. Initialize two pointers, `slow` and `fast`, both pointing to the `head` of the linked list.
2. Loop through the linked list as long as `fast` is not null and `fast.next` is not null:
   - Move `slow` forward by **1 node** (`slow = slow.next`).
   - Move `fast` forward by **2 nodes** (`fast = fast.next.next`).
3. When the loop terminates (meaning `fast` reached the end), `slow` will be pointing to the middle node.
4. Return `slow`.

---

## 🧠 Algorithm

```text
1. Set slow = head
2. Set fast = head

3. While fast is not null AND fast.next is not null:
    a. Move slow to slow.next
    b. Move fast to fast.next.next

4. Return slow
```

---

## 🔍 Dry Run

Let's trace the algorithm with two examples: one with an odd number of nodes and one with an even number.

### Example 1: Odd Length `[1, 2, 3, 4, 5]`

| Step | `slow` Position (Value) | `fast` Position (Value) | Condition Check (`fast != null && fast.next != null`) |
| :--- | :--- | :--- | :--- |
| **Start** | Node 1 | Node 1 | `true` (Node 1 and Node 2 exist) |
| **Step 1** | Node 2 | Node 3 | `true` (Node 3 and Node 4 exist) |
| **Step 2** | Node 3 | Node 5 | `false` (`fast.next` is `null`) |

**End:** Loop terminates. Return `slow`, which points to **Node 3**.

---

### Example 2: Even Length `[1, 2, 3, 4, 5, 6]`

| Step | `slow` Position (Value) | `fast` Position (Value) | Condition Check (`fast != null && fast.next != null`) |
| :--- | :--- | :--- | :--- |
| **Start** | Node 1 | Node 1 | `true` (Node 1 and Node 2 exist) |
| **Step 1** | Node 2 | Node 3 | `true` (Node 3 and Node 4 exist) |
| **Step 2** | Node 3 | Node 5 | `true` (Node 5 and Node 6 exist) |
| **Step 3** | Node 4 | `null` | `false` (`fast` is `null`) |

**End:** Loop terminates. Return `slow`, which points to **Node 4** (the second middle node).

---

## ⚠️ Edge Cases

- **Single Node List (`[1]`):** `fast.next` is initially `null`. The loop condition evaluates to `false` immediately, and the algorithm correctly returns `head` (`1`).
- **Two Nodes List (`[1, 2]`):** The loop runs once. `slow` moves to `2`, and `fast` moves to `null`. The loop terminates, correctly returning the second node (`2`).
- **Even vs. Odd Node Count:** Handled seamlessly by checking both `fast != null` (handles even length) and `fast.next != null` (handles odd length) in the loop condition to avoid null pointer dereferencing.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$\mathcal{O}(N)$**: The fast pointer travels through the $N$ nodes of the list in approximately $N/2$ iterations. Hence, the list is traversed only once, making time complexity linear with respect to the number of nodes $N$.

### Space Complexity
- **$\mathcal{O}(1)$**: The algorithm only uses two pointer variables (`slow` and `fast`), consuming constant auxiliary memory regardless of the list size.

---

## 🎯 Key Takeaways

- **Fast & Slow Pointers Pattern:** Ideal for middle-finding, cycle detection (Floyd's Cycle Finding Algorithm), and finding $k$-th element from the end of linked lists.
- **Single-Pass Optimization:** Eliminates redundant iterations by maintaining ratio-based pointer speeds ($2:1$).
- **Safe Traversal:** Always check both `fast != null` and `fast.next != null` before advancing two steps to prevent null reference errors.

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
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast!=NULL && fast->next!=NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};
```

---

## 🚀 Repository

⭐ If you found this explanation helpful, consider starring the repository.

Happy Coding! 🚀