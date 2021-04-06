variables = dict()


def compute(s):
    li = []
    el = ''
    for ch in s:
        # print(ch, el)
        if ch == ' ':
            if el != '':
                li.append(el)
                el = ''
            continue
        if ch == '+' or ch == '-':
            if el != '':
                li.append(el)
                el = ''
            li.append(ch)
            continue
        el += ch
    if el != '':
        li.append(el)
    sign, result = 1, 0
    # print(li)
    for el in li:
        if el == '+':
            continue
        if el == '-':
            sign *= -1
            continue
        try:
            var = int(el)
        except ValueError:
            try:
                var = variables[el]
            except KeyError:
                if invalid(s):
                    raise NameError('Invalid identifier')
                else:
                    raise ValueError('Unknown variable')
        result += sign * var
        sign = 1

    return result


def invalid(s):
    if s.isalpha():
        return False
    return True


def main():
    while True:
        s = input()
        if s == '':
            continue
        elif s[0] == '/':
            if s == '/exit':
                break
            elif s == '/help':
                print('The program calculates the sum of numbers')
                continue
            else:
                print('Unknown command')
                continue
        s = s.split('=')
        if len(s) == 1:
            try:
                print(compute(s[0]))
            except NameError:
                print('Invalid identifier')
            except ValueError:
                print('Unknown variable')
        else:
            if invalid(s[0].strip()):
                print(s[0].strip())
                print('Invalid identifier')
                continue
            if len(s) == 2:
                try:
                    variables[s[0].strip()] = compute(s[1].strip())
                except NameError:
                    print('Invalid identifier')
                except ValueError:
                    print('Unknown variable')
            else:
                print("Invalid assignment")

    print('Bye!')


if __name__ == '__main__':
    main()
