## 💭 Thought Process

When approaching the problem of detecting a cycle in a linked list, our first instinct might be to track the nodes we have already visited:

1. **Brute Force (Hash Set Approach):** 
   We could traverse the list and store each node's memory address in a hash set. At each step, we check if the current node is already present in the set. If it is, we found a cycle. If we reach the end of the list (`null`), there is no cycle. 
   - **Why it's inefficient:** While this runs in $O(N)$ time, it requires $O(N)$ extra memory to store the nodes, violating the optimal $O(1)$ auxiliary space condition.

2. **Optimized Observation (Two Pointers):**
   How can we detect a cycle without storing past nodes? Consider two runners on a circular track—one running fast and one running slow. Even if the fast runner starts at the same point, because they move at different speeds, the fast runner will eventually lap the slow runner and meet them again. 
   
   If the track is straight (has an end), the fast runner simply reaches the finish line. This real-world concept translates directly to **Floyd's Cycle-Finding Algorithm** (also known as the Tortoise and Hare algorithm).

---

## 💡 Intuition

The core insight relies on using two pointers moving at different speeds:
- A **slow pointer** (Tortoise) that moves **1 step** at a time.
- A **fast pointer** (Hare) that moves **2 steps** at a time.

If there is no cycle, the fast pointer will eventually reach the end of the list (`null`). 

If a cycle exists, both pointers will eventually enter the cycle. Once inside the loop, with every iteration, the distance between the fast and slow pointers decreases by exactly 1 node (since `2 - 1 = 1`). Because the gap shrinks by 1 step continuously, the fast pointer is guaranteed to catch up to the slow pointer without skipping over it.

---

## 🚀 Approach

1. **Initialize Pointers:** Place both `slow` and `fast` pointers at the `head` of the linked list.
2. **Traverse the List:** Loop as long as `fast` and `fast.next` are not `null` (ensuring we don't cause a null pointer exception when moving 2 steps ahead).
3. **Advance Pointers:**
   - Move `slow` forward by 1 node.
   - Move `fast` forward by 2 nodes.
4. **Check for Intersection:** After moving, check if `slow` and `fast` point to the exact same node memory address.
   - If `slow == fast`, a cycle is detected; return `true`.
5. **Termination:** If the loop ends because `fast` or `fast.next` becomes `null`, the list has an end; return `false`.

---

## 🧠 Algorithm

1. Initialize `slow = head` and `fast = head`.
2. While `fast` is not NULL and `fast.next` is not NULL:
   1. `slow = slow.next`
   2. `fast = fast.next.next`
   3. If `slow == fast`:
      - Return `true` (Cycle detected)
3. Return `false` (Reached end of list)

---

## 🔍 Dry Run

Let's trace the algorithm using an example: `head = [3, 2, 0, -4]`, where `-4` points back to `2` (node at index 1).

| Step | `slow` Location (Value) | `fast` Location (Value) | Condition (`slow == fast`) | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Start** | Node `3` | Node `3` | `3 == 3` (Initial state) | Continue |
| **Step 1** | Node `2` (moves 1) | Node `0` (moves 2) | `2 == 0` (False) | Continue |
| **Step 2** | Node `0` (moves 1) | Node `2` (moves -4 -> 2) | `0 == 2` (False) | Continue |
| **Step 3** | Node `-4` (moves 1) | Node `-4` (moves 0 -> -4) | `-4 == -4` (**True**) | **Return `true`** |

---

## ⚠️ Edge Cases

- **Empty List (`head == null`):** The condition `fast != null` fails immediately, and the algorithm correctly returns `false`.
- **Single Node without Cycle (`1 -> null`):** `fast.next` is `null`, the loop terminates, and it returns `false`.
- **Single Node with Cycle (`1 -> 1`):** `slow` moves to `1`, `fast` moves to `1`, `slow == fast` evaluates to `true`, correctly returning `true`.
- **Two Nodes without Cycle (`1 -> 2 -> null`):** `fast.next.next` becomes `null` on the first iteration, loop terminates safely, returning `false`.

---

## ⏱️ Complexity Analysis

### Time Complexity
- **$O(N)$**, where $N$ is the total number of nodes in the linked list.
  - If there is **no cycle**, the fast pointer reaches the end in $N/2$ steps $\rightarrow O(N)$.
  - If there is a **cycle**, the fast pointer enters the cycle first, and the slow pointer enters shortly after. The fast pointer catches up in at most $K$ steps (where $K$ is the length of the cycle, $K \le N$) $\rightarrow O(N)$.

### Space Complexity
- **$O(1)$** constant extra space, as we only maintain two pointer references (`slow` and `fast`) regardless of the size of the linked list.

---

## 🎯 Key Takeaways

- **Floyd's Cycle Detection** is the standard optimal technique for detecting loops using $O(1)$ auxiliary memory.
- **Relative Speed Strategy:** Moving pointers at relative speed difference of 1 guarantees they will meet inside a loop without stepping over each other.
- **Defensive Pointer Checks:** Always validate both `fast` and `fast.next` in the loop condition to avoid null pointer dereferencing errors.
- **Space vs. Time Tradeoff:** While a Hash Set offers a straightforward solution, fast/slow pointers reduce auxiliary space from $O(N)$ to $O(1)$.