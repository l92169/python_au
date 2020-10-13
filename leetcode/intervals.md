# Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals = sorted(intervals)
    prev = float("-inf")
    count = 0
    for i in intervals:
        if i[0]>=prev:
            prev = i[1]
        else:
            count +=1
            prev = min(prev,i[1])
    return count
```

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key = lambda x: x[0])
    merge = []
    for i in intervals:
        if not merge or merge[-1][1]<i[0]:
            merge.append(i)
        else:
            merge[-1][1] = max(merge[-1][1],i[1])
    return merge
```