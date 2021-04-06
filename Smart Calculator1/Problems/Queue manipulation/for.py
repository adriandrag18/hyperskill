my_list = [1, 2, [1, 2, "as", []], "al patrulea element"]
print(my_list)
print(my_list[0])
print(my_list[3])

lst = [1, 2, 3]
print(lst)

inputs = []
n = 0
inp = "1"
while inp != "":
    inp = input()
    inputs.append(inp)
    n = n + 1
inputs.remove("")
print(inputs)

for el in inputs:
    print(el)
