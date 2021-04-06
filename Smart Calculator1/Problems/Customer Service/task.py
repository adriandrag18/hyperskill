from collections import deque
problems = deque()
for _ in range(int(input())):
    s = input()
    if s == 'SOLVED':
        problems.popleft()
    else:
        problems.append(s.split()[1])

while problems:
    print(problems.popleft())
