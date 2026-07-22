## 💭 Thought Process

When faced with merging two sorted linked lists, a brute-force approach might involve copying all node values into an array, sorting the array, and then building a new linked list from scratch. However, this strategy completely ignores the fact that both input lists are **already sorted**, leading to unnecessary $O((N + M) \log(N + M))$ sorting time and $O(N + M)$ extra space.

To optimize, we can leverage the pre-sorted property of both lists. At any step, the next smallest element in our merged list must be the smaller of the two current head nodes of `list1` and `list2`. This leads to a Two-Pointer / Two-Cursor strategy: compare the elements at the front of each list, append the smaller node to our result, and move that list's pointer forward. Repeat this until one list is exhausted, then append the remainder of the other list.

---

## 💡 Intuition

The key insight is that merging two sorted linked lists is identical to the **merge step** in the Merge Sort algorithm:

1. **Exploiting Pre-Sorted Order**: Since both lists are monotonically non-decreasing, we only ever need to look at the current heads of both lists to determine the globally smallest unplaced node.
2. **In-Place Pointer Splicing**: Instead of creating new nodes, we can simply re-wire the existing `next` pointers. This gives us an optimal $O(1)$ auxiliary space complexity.
3. **Dummy Node Trick**: Managing the head of a dynamic linked list often requires extra conditional checks for the very first node. Introducing a **dummy node** acts as a temporary anchor, allowing us to treat all node insertions uniformly.

---

## 🚀 Approach

1. **Handle Base Cases**: If either `list1` or `list2` is `NULL`, directly return the non-null list.
2. **Initialize Anchor**: Create a stack-allocated `dummy` node and a pointer `merge` initialized to point to `dummy`.
3. **Compare and Stitch**:
   - Loop while both `list1` and `list2` are non-null.
   - Compare `list1->val` and `list2->val`.
   - Attach the smaller (or equal) node to `merge->next`.
   - Advance the corresponding list pointer (`list1` or `list2`).
   - Advance the `merge` pointer to `merge->next`.
4. **Append Remaining Nodes**: Once the loop exits, at least one list will be exhausted. Connect the remaining non-null list directly to `merge->next`.
5. **Return Result**: Return `dummy.next`, which points to the true head of the newly merged sorted list.

---

## 🧠 Algorithm

1. IF list1 is null, RETURN list2.
2. IF list2 is null, RETURN list1.
3. CREATE dummy node.
4. SET merge = pointer to dummy node.
5. WHILE list1 is not null AND list2 is not null:
    - IF list1.val <= list2.val:
        - SET merge.next = list1
        - SET list1 = list1.next
    - ELSE:
        - SET merge.next = list2
        - SET list2 = list2.next
    - SET merge = merge.next
6. IF list1 is not null:
    - SET merge.next = list1
   ELSE:
    - SET merge.next = list2
7. RETURN dummy.next

---

## 🔍 Dry Run

Let's trace the execution for `list1 = [1, 2, 4]` and `list2 = [1, 3, 4]`:

* **Initialization**:
  - `dummy` node created. `merge` $\rightarrow$ `dummy`.
  - `list1` points to `1`, `list2` points to `1`.

* **Iteration 1**:
  - Compare `list1.val (1)` and `list2.val (1)`. They are equal.
  - Set `merge.next` $\rightarrow$ `list1 (1)`.
  - Advance `list1` to `2`, advance `merge` to `1`.

* **Iteration 2**:
  - Compare `list1.val (2)` and `list2.val (1)`. `list2` is smaller.
  - Set `merge.next` $\rightarrow$ `list2 (1)`.
  - Advance `list2` to `3`, advance `merge` to `1`.

* **Iteration 3**:
  - Compare `list1.val (2)` and `list2.val (3)`. `list1` is smaller.
  - Set `merge.next` $\rightarrow$ `list1 (2)`.
  - Advance `list1` to `4`, advance `merge` to `2`.

* **Iteration 4**:
  - Compare `list1.val (4)` and `list2.val (3)`. `list2` is smaller.
  - Set `merge.next` $\rightarrow$ `list2 (3)`.
  - Advance `list2` to `4`, advance `merge` to `3`.

* **Iteration 5**:
  - Compare `list1.val (4)` and `list2.val (4)`. They are equal.
  - Set `merge.next` $\rightarrow$ `list1 (4)`.
  - Advance `list1` to `NULL`, advance `merge` to `4`.

* **Loop Termination**:
  - `list1` is now `NULL`. Exit loop.

* **Attach Remaining**:
  - `list2` is not `NULL` (points to `4`).
  - Set `merge.next` $\rightarrow$ `list2 (4)`.

* **Final Return**:
  - Return `dummy.next`, which represents `[1, 1, 2, 3, 4, 4]`.

---

## ⚠️ Edge Cases

- **Both Lists Empty (`list1 = [], list2 = []`)**: Handled by initial check (`list1 == NULL`), returning `list2` (`NULL`).
- **One List Empty (`list1 = [], list2 = [0]`)**: Immediately returns the non-empty list without unnecessary loop iterations.
- **Lists of Unequal Lengths**: The `while` loop terminates as soon as the shorter list ends, and the remaining nodes of the longer list are attached in $O(1)$ time.
- **Duplicate Elements**: The `<=` condition ensures stability and handles identical elements seamlessly.

---

## ⏱️ Complexity Analysis

### Time Complexity
$\mathcal{O}(N + M)$, where $N$ and $M$ are the number of nodes in `list1` and `list2` respectively. In the worst case, we compare elements from both lists until one is exhausted, performing a single pass over the nodes.

### Space Complexity
$\mathcal{O}(1)$ auxiliary space. The algorithm reuses existing node pointers and modifies them in-place, requiring only a dummy node and pointers.

---

## 🎯 Key Takeaways

- Dummy nodes eliminate special-case code for head node initialization in linked list problems.
- Taking advantage of pre-sorted inputs reduces time complexity from $O(K \log K)$ to linear time $O(K)$.
- In-place pointer manipulation avoids unnecessary dynamic memory allocation, achieving optimal space usage.
- This comparison-based merging technique serves as the core foundation for the Divide and Conquer **Merge Sort** algorithm on lists.