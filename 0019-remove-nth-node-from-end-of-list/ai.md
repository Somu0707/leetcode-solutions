## 💭 Thought Process

When approaching the problem of removing the $n$-th node from the end of a linked list, a natural first thought is to calculate the total length of the list, say $L$. Once $L$ is known, the $n$-th node from the end corresponds to the $(L - n + 1)$-th node from the start.

To implement this brute-force approach:
1. Traverse the entire list once to count $L$.
2. Traverse the list a second time up to node $(L - n)$ to update its `.next` pointer, bypassing the target node.

While this works, it requires **two passes** through the linked list. 

To achieve a **single-pass** solution, we can ask: *Is there a way to locate the target node relative to the end of the list while traversing forward?*

By maintaining a fixed separation distance of $n$ nodes between two pointers, we can find the target node without knowing the total length beforehand.

---

## 💡 Intuition

The key insight is using a **Two-Pointer (Fast & Slow)** technique with a fixed gap:

1. If a fast pointer (`curr`) is advanced $n$ nodes ahead of a slow pointer (`prev`), the gap between them is exactly $n$ nodes.
2. If both pointers are then advanced together at the same speed, this gap of $n$ nodes is maintained.
3. When `curr` reaches the end of the list (i.e., `curr->next == NULL`), `prev` will be positioned at the node directly **before** the $n$-th node from the end.
4. From this position, removing the target node requires a simple pointer re-assignment (`prev->next = prev->next->next`).

This approach achieves the goal in a single traversal with constant space complexity.

---

## 🚀 Approach

1. **Initialize Pointers**: Place both pointers, `prev` and `curr`, at the `head` of the list.
2. **Create the Gap**: Advance `curr` forward by $n$ steps.
3. **Check Head Removal**: If `curr` becomes `NULL` after taking $n$ steps, it means $n$ equals the total length of the list. In this case, the node to be removed is the `head` itself, so return `head->next`.
4. **Slide the Window**: Advance both `curr` and `prev` together one node at a time until `curr->next` becomes `NULL`. At this point, `curr` is at the last node, and `prev` is at the node just before the target node.
5. **Delete Target Node**: Adjust `prev->next` to point to `prev->next->next`, bypassing the target node.
6. **Return Result**: Return the original `head`.

---

## 🧠 Algorithm

1. Initialize `prev = head` and `curr = head`.
2. Repeat $n$ times:
   - Move `curr = curr.next`
3. If `curr` is `null`:
   - Return `head.next` (removing the head node)
4. While `curr.next` is not `null`:
   - Move `curr = curr.next`
   - Move `prev = prev.next`
5. Set `prev.next = prev.next.next`
6. Return `head`

---

## 🔍 Dry Run

### Input
- List: `1 -> 2 -> 3 -> 4 -> 5`
- `n = 2`

| Step | Action | `prev` Position | `curr` Position | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Initial** | Start pointers at head | Node `1` | Node `1` | Gap = 0 |
| **Advance Fast (1/2)** | `curr = curr.next` | Node `1` | Node `2` | Step 1 |
| **Advance Fast (2/2)** | `curr = curr.next` | Node `1` | Node `3` | Step 2 (Gap of $n=2$ established) |
| **Check Null** | `curr == NULL`? | Node `1` | Node `3` | Not NULL, proceed to simultaneous movement |
| **Loop Iteration 1** | Move both | Node `2` | Node `4` | `curr.next` (Node 5) is not NULL |
| **Loop Iteration 2** | Move both | Node `3` | Node `5` | `curr.next` is NULL, loop terminates |
| **Deletion** | `prev.next = prev.next.next` | Node `3` | Node `5` | Node `3` now points to Node `5` |

### Output List
- `1 -> 2 -> 3 -> 5`

---

## ⚠️ Edge Cases

- **Removing the Head Node ($n = \text{length}$)**: After advancing `curr` by $n$ steps, `curr` reaches `NULL`. The algorithm detects this condition immediately and returns `head->next`, correctly removing the first element.
- **Single Element List ($sz = 1, n = 1$)**: Moving `curr` forward 1 step makes it `NULL`. The head is removed, returning `NULL` (an empty list).
- **Removing the Tail Node ($n = 1$)**: The `curr` pointer advances to the last node while `prev` stops at the second-to-last node. Setting `prev->next = NULL` correctly removes the tail.

---

## ⏱️ Complexity Analysis

### Time Complexity
$\mathcal{O}(N)$ — The algorithm performs a single pass over the linked list of length $N$. Each pointer moves at most $N$ steps.

### Space Complexity
$\mathcal{O}(1)$ — Only two pointer variables (`prev` and `curr`) are used, requiring constant auxiliary space.

---

## 🎯 Key Takeaways

- **Two-Pointer Offset Strategy**: Maintaining a fixed gap between two pointers is a standard technique for single-pass distance problems in linear data structures.
- **Single Pass Traversal**: Avoids duplicate operations like calculating total size prior to processing.
- **Implicit Length Calculation**: The offset naturally calculates positions relative to the end of a structure without explicit counting.
- **Boundary Node Handling**: Always handle boundary cases (head and tail deletions) explicitly to avoid null pointer dereferences.