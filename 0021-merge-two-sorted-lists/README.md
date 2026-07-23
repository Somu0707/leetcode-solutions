# 21. Merge Two Sorted Lists

<div align="center">

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Acceptance](https://img.shields.io/badge/Acceptance-68.6%25-blue)
![Topics](https://img.shields.io/badge/Topics-2-orange)

</div>

---

# 📝 Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

---

# 📚 Examples

## Example 1

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

## Example 2

```
Input: list1 = [], list2 = []
Output: []
```

## Example 3

```
Input: list1 = [], list2 = [0]
Output: [0]
```

---

# 📌 Constraints

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.



---

# 🧠 AI Solution Explanation

## 💭 Thought Process

When faced with merging two linked lists, a initial brute-force strategy might be to dump all values from both lists into an array, sort the array using a standard sorting algorithm, and construct a brand new linked list from the sorted values.

While simple, this naive approach completely ignores a crucial property given in the problem: **both input lists are already sorted**. Sorting an unsorted array of size $N + M$ takes $O((N + M) \log(N + M))$ time and requires $O(N + M)$ extra memory.

To optimize, we can use the two-pointer strategy (similar to the merge step in Merge Sort):
1. Compare the current nodes at the heads of both lists.
2. The smaller node must come first in our merged list.
3. Rewire pointers in-place rather than allocating new memory.

This observation allows us to solve the problem in a single linear pass using constant extra space.

---

## 💡 Intuition

The key insight is to build the merged list incrementally by selecting the smallest available element from the heads of `list1` and `list2`. 

A common challenge in linked list manipulation is handling the head of the new list—specifically, setting up the initial head node requires additional conditional checks. To elegantly bypass this edge case, we introduce a **dummy node**. The dummy node serves as a stationary reference point before the actual start of our merged list, making pointer management clean and uniform throughout the iteration.

Because both input lists are already sorted, we only ever need to look at the current front nodes of each list to decide which node comes next.

---

## 🚀 Approach

1. **Handle Base Cases:** If either input list is empty (`NULL`), return the other list immediately since no merging is required.
2. **Initialize Dummy Node:** Create a dummy node on the stack to act as a anchor for the merged list. Create a `merge` pointer initialized to point to this dummy node.
3. **Iterate and Compare:** Traverse both lists simultaneously using a `while` loop that continues as long as both `list1` and `list2` are not `NULL`.
   - Compare `list1->val` and `list2->val`.
   - Attach the node with the smaller (or equal) value to `merge->next`.
   - Advance the pointer of the list from which the node was chosen.
   - Advance the `merge` pointer forward (`merge = merge->next`).
4. **Attach Remaining Nodes:** When the loop finishes, at least one list will be exhausted. Simply attach the non-empty list (if any) directly to `merge->next`.
5. **Return Result:** Return `dummy.next`, which points to the true head of the merged sorted linked list.

---

## 🧠 Algorithm

1. Check if `list1` is null -> return `list2`.
2. Check if `list2` is null -> return `list1`.
3. Create a `dummy` node and set a `current` pointer to `dummy`.
4. While `list1` is not null AND `list2` is not null:
   - If `list1.val` <= `list2.val`:
     - Set `current.next` = `list1`
     - Move `list1` to `list1.next`
   - Else:
     - Set `current.next` = `list2`
     - Move `list2` to `list2.next`
   - Move `current` to `current.next`
5. If `list1` is not null, set `current.next` = `list1`.
6. Else, set `current.next` = `list2`.
7. Return `dummy.next`.

---

## 🔍 Dry Run

Let's trace the algorithm with `list1 = [1, 2, 4]` and `list2 = [1, 3, 4]`:

* **Initialization:**
  * `dummy` = `[-1]`, `merge` points to `dummy`.
  * `list1` -> `1`, `list2` -> `1`.

* **Step 1:** Compare `list1->val` (1) and `list2->val` (1).
  * `1 <= 1` is True.
  * Connect `merge->next` to `list1` (Node `1`).
  * Advance `list1` to `2`. Advance `merge` to Node `1`.

* **Step 2:** Compare `list1->val` (2) and `list2->val` (1).
  * `2 <= 1` is False.
  * Connect `merge->next` to `list2` (Node `1`).
  * Advance `list2` to `3`. Advance `merge` to Node `1`.

* **Step 3:** Compare `list1->val` (2) and `list2->val` (3).
  * `2 <= 3` is True.
  * Connect `merge->next` to `list1` (Node `2`).
  * Advance `list1` to `4`. Advance `merge` to Node `2`.

* **Step 4:** Compare `list1->val` (4) and `list2->val` (3).
  * `4 <= 3` is False.
  * Connect `merge->next` to `list2` (Node `3`).
  * Advance `list2` to `4`. Advance `merge` to Node `3`.

* **Step 5:** Compare `list1->val` (4) and `list2->val` (4).
  * `4 <= 4` is True.
  * Connect `merge->next` to `list1` (Node `4`).
  * Advance `list1` to `NULL`. Advance `merge` to Node `4`.

* **Loop Termination & Cleanup:**
  * Loop ends because `list1` is `NULL`.
  * `list2` still has Node `4`. Attach remaining `list2` to `merge->next`.

* **Final Result:**
  * Return `dummy.next` -> `[1 -> 1 -> 2 -> 3 -> 4 -> 4]`.

---

## ⚠️ Edge Cases

- **Both Lists Empty (`list1 = [], list2 = []`):** Handled by initial check `if (list1 == NULL) return list2;`, correctly returning `NULL`.
- **One List Empty (`list1 = [], list2 = [0]`):** Immediately returns `list2` without entering any loops.
- **Lists of Unequal Lengths:** Handled automatically after the `while` loop by appending the non-empty list directly to the end of the merged list in $O(1)$ time.
- **Lists with Duplicate Values:** Handled seamlessly by using `<=`, preserving stability and relative order.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$\mathcal{O}(N + M)$**, where $N$ and $M$ are the number of nodes in `list1` and `list2` respectively. In the worst case, we traverse every node from both lists exactly once.

### Space Complexity
- **$\mathcal{O}(1)$** auxiliary space. The algorithm splices existing nodes in-place by adjusting pointer references without creating any new node allocations.

---

## 🎯 Key Takeaways

- **Dummy Nodes Simplify Code:** Using a dummy node avoids writing special conditional logic for setting the head of a linked list.
- **Exploit Input Properties:** Taking advantage of the fact that inputs are already sorted reduces time complexity from $O(K \log K)$ to $O(K)$.
- **In-Place Mutation:** Re-pointing existing links allows optimal $O(1)$ space complexity compared to constructing brand-new list instances.
- **Two-Pointer Paradigm:** Comparing pointers at the front of sorted structures is a fundamental building block for merge operations across data structures.

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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == NULL) return list2;
        if (list2 == NULL) return list1;
        ListNode dummy(-1);
        ListNode* merge = &dummy;
        // list1 = list1->next;
        while(list1 != NULL && list2 != NULL){
            if(list1->val <= list2->val){
                merge->next = list1;
                list1 = list1->next;
            }
            else {
                merge->next = list2;
                list2 = list2->next;
            }
            merge = merge->next;
        }
        if(list1) merge->next = list1;
        else merge->next = list2;
        return dummy.next;
    }
};
```

---

## 🚀 Repository

⭐ If you found this explanation helpful, consider starring the repository.

Happy Coding! 🚀