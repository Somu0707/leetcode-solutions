## 💭 Thought Process

When thinking about how browser history works in real life:
1. Moving backward in history goes to the previously visited page.
2. Moving forward goes to a page visited prior to going backward.
3. Visiting a new page while somewhere in the middle of the history overwrites and clears all "forward" pages.

A naive initial thought might be to use a single array or two stacks (`backStack` and `forwardStack`). While two stacks work, a doubly linked list is a very intuitive structure here because browser navigation naturally requires **bidirectional movement** (backwards and forwards) from a **current position**. 

By maintaining a pointer to the current page in a doubly linked list, we can move backward using `prev` pointers and forward using `next` pointers in constant time per step. Furthermore, visiting a new URL simply truncates the forward linked nodes and attaches the new page directly to the current node.

---

## 💡 Intuition

A **Doubly Linked List (DLL)** is uniquely suited for this problem because:
- **Bi-directional Traversal**: Each node holds links to both its predecessor (`prev`) and successor (`next`), allowing easy traversal backward and forward.
- **Dynamic Insertion and Truncation**: When visiting a new page from the middle of the history, the forward history becomes invalid. With a DLL, we can detach all nodes forward of `curr` in $O(1)$ time (or by freeing memory) and seamlessly append the new node.

---

## 🚀 Approach

1. **Initialization**: 
   * Create a node for the `homepage`.
   * Maintain a pointer `curr` pointing to this initial node.

2. **`visit(url)`**:
   * Clear all nodes after `curr` (the forward history) to free memory and avoid invalid references.
   * Create a new node containing `url`.
   * Link `curr` to this new node bi-directionally (`curr.next = newNode`, `newNode.prev = curr`).
   * Advance `curr` to point to `newNode`.

3. **`back(steps)`**:
   * Traverse backward using `curr.prev` until either `steps` becomes $0$ or `curr.prev` becomes `null` (reaching the beginning of history).
   * Return the URL of the node `curr` lands on.

4. **`forward(steps)`**:
   * Traverse forward using `curr.next` until either `steps` becomes $0$ or `curr.next` becomes `null` (reaching the end of history).
   * Return the URL of the node `curr` lands on.

---

## 🧠 Algorithm

```text
Class Node:
    url: String
    prev: Node
    next: Node

Class BrowserHistory:
    Initialize(homepage):
        curr = Node(homepage)

    Function visit(url):
        // Free forward nodes if any
        temp = curr.next
        while temp is not null:
            nextnode = temp.next
            delete temp
            temp = nextnode
        
        // Create and attach new node
        newNode = Node(url)
        curr.next = newNode
        newNode.prev = curr
        curr = newNode

    Function back(steps):
        while steps > 0 and curr.prev is not null:
            curr = curr.prev
            steps = steps - 1
        return curr.url

    Function forward(steps):
        while steps > 0 and curr.next is not null:
            curr = curr.next
            steps = steps - 1
        return curr.url
```

---

## 🔍 Dry Run

Let's walk through a sequence of operations:

1. **Initialize** with `"leetcode.com"`:
   * History: `[leetcode.com]`
   * Pointer: `curr` $\rightarrow$ `"leetcode.com"`

2. **`visit("google.com")`**:
   * History: `"leetcode.com"` $\leftrightarrow$ `"google.com"`
   * Pointer: `curr` $\rightarrow$ `"google.com"`

3. **`visit("facebook.com")`**:
   * History: `"leetcode.com"` $\leftrightarrow$ `"google.com"` $\leftrightarrow$ `"facebook.com"`
   * Pointer: `curr` $\rightarrow$ `"facebook.com"`

4. **`back(1)`**:
   * Move `curr` 1 step back.
   * Pointer: `curr` $\rightarrow$ `"google.com"`
   * Returns: `"google.com"`

5. **`visit("linkedin.com")`**:
   * Deletes `"facebook.com"` (forward history discarded).
   * History: `"leetcode.com"` $\leftrightarrow$ `"google.com"` $\leftrightarrow$ `"linkedin.com"`
   * Pointer: `curr` $\rightarrow$ `"linkedin.com"`

6. **`back(5)`**:
   * Try to move 5 steps back, but hits boundary (`curr.prev == null`) after 2 steps at `"leetcode.com"`.
   * Pointer: `curr` $\rightarrow$ `"leetcode.com"`
   * Returns: `"leetcode.com"`

---

## ⚠️ Edge Cases

- **`steps` exceeds available history**: Handled by checking `curr.prev != NULL` (for `back`) and `curr.next != NULL` (for `forward`), stopping prematurely at the boundary without throwing null pointer exceptions.
- **Visiting a new URL from the middle of history**: Forward history must be properly detached and cleaned up to prevent memory leaks and invalid state navigation.
- **Single-node history**: Initialized with just the homepage; `back` and `forward` safely return the homepage without moving.

---

## ⏱️ Complexity Analysis

### Time Complexity

- **`BrowserHistory(homepage)`**: $\mathcal{O}(1)$ to allocate the initial node.
- **`visit(url)`**: $\mathcal{O}(K)$ time where $K$ is the number of forward nodes deleted. In amortized terms across operations, each node is created once and deleted at most once, making it $\mathcal{O}(1)$ amortized per call.
- **`back(steps)`**: $\mathcal{O}(\min(\text{steps}, N))$ where $N$ is the length of the history traversed.
- **`forward(steps)`**: $\mathcal{O}(\min(\text{steps}, N))$ where $N$ is the length of the history traversed.

### Space Complexity

- **$\mathcal{O}(N)$**, where $N$ is the maximum number of URLs visited and retained in the linked list history.

---

## 🎯 Key Takeaways

- **Doubly Linked Lists** are ideal for bidirectional linear tracking where forward and backward moves happen incrementally.
- Explicit pointer management ensures smooth $O(1)$ navigation and clean branch truncation when history diverges.
- Boundary conditions (head and tail pointers being `null`) must always guard step-based traversal loops.