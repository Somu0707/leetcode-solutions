README_PROMPT = """
You are a senior Software Engineer and DSA mentor.

Generate a professional GitHub README for the following LeetCode solution.

Requirements:

1. Problem Summary (2-3 lines)
2. Intuition
3. Approach
4. Dry Run
5. Time Complexity
6. Space Complexity
7. Key Learning
8. Include the original C++ solution inside a markdown code block.

Problem Name:
{problem_name}

C++ Solution:

{code}

Return ONLY markdown.
"""