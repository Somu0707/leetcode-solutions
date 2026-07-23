## 💭 Thought Process

When approaching this problem, an initial naive idea might be to copy all the node values into an auxiliary array or list, separate the elements at odd and even positions, and then construct a brand-new linked list. 

While this brute-force approach works, it requires $\mathcal{O}(N)$ extra memory to store the nodes. The problem explicitly requires an **$\mathcal{O}(1)$ space complexity** solution. To achieve this, we must re-link the existing nodes directly in memory without allocating new ones.

Notice that the nodes in the linked list alternate between odd and even positions ($1^{\text{st}}$ node is odd, $2^{\text{nd}}$ is even, $3^{\text{rd}}$ is odd, and so on). This means:
- An odd node's next node in the odd chain is `odd.next.next`.
- An even node's next node in the even chain is `even.next.next`.

By splitting the list into two sublists—one for odd-indexed nodes and one for even-indexed nodes—we can construct both sublists simultaneously in a single traversal and then concatenate them at the end.

---

## 💡 Intuition

The core idea is to maintain two pointers (`odd` and `even`) that iterate through the list concurrently, building two independent sublists:
1. **Odd Sublist**: Contains nodes at indices $1, 3, 5, \dots$
2. **Even Sublist**: Contains nodes at indices $2, 4, 6, \dots$

Because the even nodes sit between the odd nodes, we can advance `odd` by pointing its `next` pointer to `even.next`, and advance `even` by pointing its `next` pointer to the new `odd.next`. 

To join the two sublists together at the end, we keep a permanent reference to the head of the even sublist (`even_start`). Once the traversal finishes, setting `odd.next = even_start` links the end of the odd chain directly to the beginning of the even chain.

---

## 🚀 Approach

1. **Base Case Check**: If the list is empty (`head == NULL`) or contains only a single node (`head.next == NULL`), no reordering is needed; return `head`.
2. **Initialize Pointers**:
   - `odd`: Point to `head` (the $1^{\text{st}}$ node).
   - `even`: Point to `head.next` (the $2^{\text{nd}}$ node).
   - `even_start`: Save the `even` pointer so we remember where the even sublist begins.
3. **Partition Loop**: Iterate as long as `even` and `even.next` are not `NULL`:
   - Point `odd.next` to `even.next` (bypassing the current even node to reach the next odd node).
   - Advance `odd` to `odd.next`.
   - Point `even.next` to `odd.next` (bypassing the next odd node to reach the next even node).
   - Advance `even` to `even.next`.
4. **Combine Sublists**: Attach `even_start` to `odd.next` to place the even sublist immediately after the odd sublist.
5. **Return**: Return `head`, which now points to the fully rearranged list.

---

## 🧠 Algorithm

```text
Algorithm: Rearrange Linked List into Odd and Even Sublists

1. IF head is NULL or head.next is NULL THEN
2.     RETURN head
3. END IF

4. SET odd = head
5. SET even = head.next
6. SET even_start = even

7. WHILE even is NOT NULL AND even.next is NOT NULL DO
8.     odd.next = even.next
9.     odd = odd.next
10.    even.next = odd.next
11.    even = even.next
12. END WHILE

13. odd.next = even_start

14. RETURN head
```

---

## 🔍 Dry Run

Let's trace the algorithm using the input list: `[1 -> 2 -> 3 -> 4 -> 5]`

### Initialization
- `odd` = Node(1)
- `even` = Node(2)
- `even_start` = Node(2)

```text
Odd list:   1
Even list:  2 -> 3 -> 4 -> 5
```

---

### Step 1
- **Condition Check**: `even` (2) $\neq$ NULL and `even.next` (3) $\neq$ NULL. (True)
- `odd.next = even.next` $\rightarrow$ Node(1) points to Node(3)
- `odd = odd.next` $\rightarrow$ `odd` moves to Node(3)
- `even.next = odd.next` $\rightarrow$ Node(2) points to Node(4)
- `even = even.next` $\rightarrow$ `even` moves to Node(4)

```text
Odd chain:  1 -> 3
Even chain: 2 -> 4 -> 5
```

---

### Step 2
- **Condition Check**: `even` (4) $\neq$ NULL and `even.next` (5) $\neq$ NULL. (True)
- `odd.next = even.next` $\rightarrow$ Node(3) points to Node(5)
- `odd = odd.next` $\rightarrow$ `odd` moves to Node(5)
- `even.next = odd.next` $\rightarrow$ Node(4) points to NULL (since Node(5).next is NULL)
- `even = even.next` $\rightarrow$ `even` moves to NULL

```text
Odd chain:  1 -> 3 -> 5
Even chain: 2 -> 4 -> NULL
```

---

### Step 3 (Loop Termination)
- **Condition Check**: `even` is NULL. Loop terminates.
- **Link Chains**: `odd.next = even_start` $\rightarrow$ Node(5) points to Node(2).

```text
Final List: 1 -> 3 -> 5 -> 2 -> 4 -> NULL
```

---

## ⚠️ Edge Cases

- **Empty List (`head == NULL`)**: Safely caught by the initial check; returns `NULL`.
- **Single Node (`head.next == NULL`)**: Caught by the initial check; returns `head` as no reordering is required.
- **Two Nodes (`1 -> 2`)**: Loop condition `even.next != NULL` fails immediately. `odd.next` is set to `even_start` (which is already `even`), keeping the order as `1 -> 2`.
- **Odd vs. Even total length**: The loop condition `even != NULL && even.next != NULL` handles both odd and even length lists cleanly without throwing `NULL` pointer dereference errors.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$\mathcal{O}(N)$**: Each node in the linked list is visited once during the single traversal loop.

### Space Complexity
- **$\mathcal{O}(1)$**: The algorithm only uses a constant number of pointers (`odd`, `even`, `even_start`) and modifies node links in-place.

---

## 🎯 Key Takeaways

- **In-Place Manipulation**: Modifying pointer links directly avoids allocating extra memory, satisfying strict $\mathcal{O}(1)$ space constraints.
- **Preserving References**: Storing the head of a sub-chain (`even_start`) before modifying links is critical to avoid losing access to partitioned segments.
- **Multi-pointer Traversal**: Using multiple synchronized pointers allows splitting and reweaving dynamic data structures efficiently in a single pass.
- **Safe Termination**: Checking both `even != NULL` and `even.next != NULL` prevents dangling or null pointer dereferencing regardless of whether the list length is odd or even.