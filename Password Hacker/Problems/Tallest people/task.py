def tallest_people(**kwargs):
    height_max = max(kwargs.values())
    li = []
    for name, height in kwargs.items():
        if height == height_max:
            li.append((name, height))
    li.sort(key=lambda a: a[0])
    for name, height in li:
        print(f'{name} : {height}')
