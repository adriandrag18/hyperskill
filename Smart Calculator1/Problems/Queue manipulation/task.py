from collections import deque
queue = deque()
for _ in range(int(input())):
    s = input()
    if s == 'DEQUEUE':
        queue.popleft()
    else:
        queue.append(s[8:])

while queue:
    print(queue.popleft())
