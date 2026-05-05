# User function Template for python3


class Ds:
    def __init__(self, start=0, end=0, index=0):
        self.start = start
        self.end = end
        self.index = index


class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    # only a meeting can be started after it ends so 1,5 and 5,6 not possible but 6,7 possible as after 5 6 will be available
    # but the question is we can follow any order such that we maximise the number of meetings
    # being greedy we try to take the faster meetings , the meeting ending faster we can accomodidate
    # somehting like sort based on the endings coz we can arrange in the way they end and the ones which end faster
    def maximumMeetings(self, start, end):
        # code here
        # create a data structure which can store the three variables start and end and the ds should be sorted based on the end time
        n = len(start)
        meetings = [Ds(start[i], end[i], i + 1) for i in range(n)]
        # after this this gonna look alike [{1,2,1},{3,4,2},{0,6,3},....]
        # next sort by the end time
        meetings.sort(key=lambda x: x.end)
        # and the array looks like [{1,2,1},{3,4,2},{}]
        # as the meeting however gonna start
        count = 1
        end_time = meetings[0].end
        for i in range(1, n):
            if meetings[i].start > end_time:
                count = count + 1
                end_time = meetings[i].end
        return count
