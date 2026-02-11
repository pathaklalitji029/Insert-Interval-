# Insert-Interval-
we have  a list of intervals that are sorted and non-overlapping,where One new interval is to insert the new interval into the list such that the intervals remain sorted and any overlapping intervals are merged.

# Apporach to solve the problem

1.Create an empty list result to store final intervals.

2.Traverse each interval from the given list:-
  If the current interval ends before the new interval starts
   add it directly to result

  If the current interval starts after the new interval ends
   add the new interval first, then treat the current interval as the new one

  If both intervals overlap
    merge them by updating the start and end of the new interval

3.After traversal, add the final new interval to result.

4.Return the result list.

# Time complexity is O(n)

# Space complexity  is O(n)
