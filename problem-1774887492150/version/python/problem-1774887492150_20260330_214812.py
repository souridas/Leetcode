# Last updated: 3/30/2026, 9:48:12 PM
# max heap problem
1from collections import defaultdict
2import heapq
3class EventManager:
4
5    def __init__(self, events: list[list[int]]):
6        self.active_events=defaultdict(int)
7        self.heap=[]
8        for id,priority in events:
9            self.active_events[id]=priority
10            heapq.heappush(self.heap,(-priority,id))
11        
12
13    def updatePriority(self, eventId: int, newPriority: int) -> None:
14        self.active_events[eventId]=newPriority
15        heapq.heappush(self.heap,(-newPriority,eventId))
16       
17    def pollHighest(self) -> int:
18        while self.heap:
19            poll_priority,poll_id=self.heap[0]
20            if poll_id in self.active_events and self.active_events[poll_id]==-poll_priority:
21                heapq.heappop(self.heap)
22                del self.active_events[poll_id]
23                return poll_id
24            else:
25                heapq.heappop(self.heap)
26        return -1
27        
28        
29        
30
31
32# Your EventManager object will be instantiated and called as such:
33# obj = EventManager(events)
34# obj.updatePriority(eventId,newPriority)
35# param_2 = obj.pollHighest()