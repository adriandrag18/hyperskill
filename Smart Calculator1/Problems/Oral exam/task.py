from collections import deque
queue = deque()
for _ in range(int(input())):
    s = input()
    if s == 'PASSED':
        print(queue.popleft())
    elif s == 'EXTRA':
        queue.append(queue.popleft())
    else:
        queue.append(s[6:])
