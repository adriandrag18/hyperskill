s = input()
brackets_open = 0
for ch in s:
    if ch == '(':
        brackets_open += 1
    if ch == ')':
        brackets_open -= 1
    if brackets_open < 0:
        break

if brackets_open:
    print('ERROR')
else:
    print('OK')
