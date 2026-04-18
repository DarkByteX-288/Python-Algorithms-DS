
## 📚 Practice Platforms
- [LeetCode](https://leetcode.com)
- [HackerRank](https://hackerrank.com)
- [Codeforces](https://codeforces.com)
- [NeetCode 150](https://neetcode.io/practice)

## 💡 Featured Implementations
- **Arrays**: Two Sum, Best Time to Buy/Sell Stock
- **Linked Lists**: Reverse Linked List, Merge Two Sorted Lists
- **Trees**: Binary Tree Inorder Traversal, Maximum Depth
- **Sorting**: QuickSort, MergeSort (with visualizations)
- **Graphs**: BFS, DFS, Shortest Path

## 📈 Progress Tracking

| Topic | Problems Solved | Time | Space | Notes |
|-------|-----------------|------|-------|-------|
| Arrays | 25/50 | O(n) avg | O(1) | Sliding window |
| Strings | 18/40 | O(n) | O(n) | Two pointers |
| Trees | 12/30 | O(n) | O(h) | Recursion |

## 🎯 How to Use

1. **Daily Practice**: Pick 2-3 problems from `solutions/`
2. **Add Solutions**: Create file like `arrays/problem_name.py`
3. **Document Complexity**: Add time/space analysis in docstring
4. **Track Progress**: Update progress table above

## Example Solution
```python
# arrays/two_sum.py
def two_sum(nums, target):
    """
    LeetCode #1: Two Sum
    Time: O(n), Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

## 🤝 Contributing
1. Fork the repo
2. Create feature branch: `git checkout -b feature/problem-name`
3. Commit: `git commit -m "Add two sum solution"`
4. Push & PR

## 📝 Learning Resources
- [Algorithm Visualizer](https://algorithm-visualizer.org)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com)
- [Grokking Algorithms](https://www.amazon.com/Grokking-Algorithms-illustrated-programmers-curious/dp/1617292230)

## License
MIT License - feel free to use for learning & interviews.
