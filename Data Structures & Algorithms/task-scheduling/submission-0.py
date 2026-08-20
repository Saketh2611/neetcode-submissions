from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()          # cooldown queue: (available_time, remaining_count, task)
        cycles = 0

        freq = Counter(tasks)

        # max heap using negative frequency
        heap = []
        for task, count in freq.items():
            heapq.heappush(heap, (-count, task))

        while heap or q:
            cycles += 1

            # execute task if available
            if heap:
                count, task = heapq.heappop(heap)
                count += 1   # reduce count (since negative)

                if count != 0:
                    q.append((cycles + n, count, task))

            # check cooldown queue
            if q and q[0][0] == cycles:
                _, count, task = q.popleft()
                heapq.heappush(heap, (count, task))

        return cycles
