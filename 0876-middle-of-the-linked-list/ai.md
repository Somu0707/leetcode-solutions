## 💭 Thought Process

When asked to find the middle node of a linked list, a straightforward brute-force approach comes to mind:

1. Traverse the entire linked list to count the total number of nodes, $N$.
2. Calculate the middle index as $\lfloor N / 2 \rfloor$.
3. Traverse the list a second time up to index $\lfloor N / 2 \rfloor$ to locate and return the middle node.

While this $O(N)$ approach works and uses $O(1)$ extra space, it requires **two full passes** over the linked list. 

To optimize this into a **single pass**, we can ask: *Can we determine the midpoint while traversing the list for the first time?*

Imagine two runners on a track starting at the same line. If Runner A moves at twice the speed of Runner B, by the time Runner A crosses the finish line, Runner B will be exactly halfway through the track. This observation forms the core of the optimal solution.

---

## 💡 Intuition

The fast and slow pointer technique (often called the **Tortoise and Hare** algorithm) is ideal for this problem.

- **Why it works:** By advancing the `fast` pointer two steps for every one step the `slow` pointer moves, the ratio of distances traveled by `slow` and `fast` remains $1:2$. When `fast` reaches the end of the list, `slow` is guaranteed to be at the midpoint.
- **Handling Even Lengths:** For lists with an even number of nodes, there are two middle nodes. The condition `fast != null && fast.next != null` naturally ensures that `slow` lands on the **second middle node**, satisfying the problem requirements without needing extra conditional checks.

---

## 🚀 Approach

1. **Initialize Pointers:** Create two pointers, `slow` and `fast`, both initially pointing to the `head` of the linked list.
2. **Traverse the List:** Loop while `fast` is not `null` and `fast.next` is not `null`:
   - Advance `slow` by one step (`slow = slow.next`).
   - Advance `fast` by two steps (`fast = fast.next.next`).
3. **Return Result:** When the loop terminates, `slow` will point to the middle node. Return `slow`.

---

## 🧠 Algorithm

```text
1. Set slow = head
2. Set fast = head
3. While fast is not null AND fast.next is not null:
    a. slow = slow.next
    b. fast = fast.next.next
4. Return slow
```

---

## 🔍 Dry Run

Let's trace the algorithm with an even-length linked list: `1 -> 2 -> 3 -> 4 -> 5 -> 6`

| Step | `slow` Node | `fast` Node | Condition Check (`fast != null && fast.next != null`) | Action |
| :--- | :--- | :--- | :--- | :--- |
| **Start** | `1` | `1` | `fast` (1) and `fast.next` (2) are non-null | Enter Loop |
| **1** | `2` | `3` | `fast` (3) and `fast.next` (4) are non-null | Enter Loop |
| **2** | `3` | `5` | `fast` (5) and `fast.next` (6) are non-null | Enter Loop |
| **3** | `4` | `null` | `fast` is `null` | Terminate Loop |

**Final Result:** `slow` points to node `4` (the second middle node), which is returned.

---

## ⚠️ Edge Cases

- **Single Node List (`[1]`):** The condition `fast.next != null` is false initially. The loop does not run, and the algorithm correctly returns `slow` (head).
- **Two Nodes List (`[1, 2]`):** The loop runs once. `slow` moves to `2`, `fast` becomes `null`. The loop ends, returning `2` (the second middle node).
- **Odd Number of Nodes (`[1, 2, 3]`):** `fast` lands on the last node (`3`), so `fast.next` is `null`. The loop terminates with `slow` at exact middle node `2`.
- **Even Number of Nodes (`[1, 2, 3, 4]`):** `fast` moves out of bounds to `null`. The loop terminates with `slow` at second middle node `3`.

---

## ⏱️ Complexity Analysis

### Time Complexity
**$O(N)$**: The fast pointer traverses the list in steps of 2, reaching the end in approximately $N/2$ iterations. Thus, the list is traversed only once, resulting in linear time complexity.

### Space Complexity
**$O(1)$**: The algorithm only uses two pointer variables (`slow` and `fast`), requiring constant auxiliary space.

---

## 🎯 Key Takeaways

- **Fast & Slow Pointers:** A powerful pattern for finding middle elements, cycle detection, and $k$-th element from the end in linked lists.
- **Single Pass Efficiency:** Relative pointer speed allows finding proportional positions without knowing the total size beforehand.
- **Safe Boundary Conditions:** Checking both `fast != null` and `fast.next != null` prevents null pointer errors when advancing two steps at a time.