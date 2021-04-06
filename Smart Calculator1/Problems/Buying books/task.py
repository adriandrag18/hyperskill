n = int(input())

book_stack = []

for _ in range(n):
    s = input()
    if s[:3] == 'BUY':
        book_stack.append(s[4:])
    else:
        print(book_stack.pop())
