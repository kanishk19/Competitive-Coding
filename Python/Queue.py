from collections import deque

queue = deque(['Aman'])
queue.append('Kanishk')
queue.append('Suraj')

print queue

queue.popleft()

print queue