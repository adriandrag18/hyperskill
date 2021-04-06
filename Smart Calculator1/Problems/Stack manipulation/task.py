n = int(input())
stack = []
for _ in range(n):
    s = input()
    if s == 'POP':
        stack.pop()
    else:
        stack.append(s.split()[1])

while stack:
    print(stack.pop())
