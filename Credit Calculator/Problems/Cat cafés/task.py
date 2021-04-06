m = 0
name = ''
while True:
    s = input().split()
    if s[0] == 'MEOW':
        break
    elif int(s[1]) > m:
        m = int(s[1])
        name = s[0]
print(name)
