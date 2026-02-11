class Solution(object):
    def insert(self, intervals, newInterval):
        result = []

        for interval in intervals:
            # Case 1: interval is completely before newInterval
            if interval[1] < newInterval[0]:
                result.append(interval)

            # Case 2: interval is completely after newInterval
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval

            # Case 3: overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        # add the last interval
        result.append(newInterval)
        return result


intervals=[[1,3],[6,9]]
newInterval=[2,5]

obj=Solution()
print(obj.insert(intervals,newInterval))
