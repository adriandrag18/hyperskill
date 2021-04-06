# HARD
list1 = [[el, el + 1, el + 2] for el in range(10)]
list2 = [list(range(el, 2 * el, 2)) for el in range(12, 40, 9)]
list3 = [[*range(el, 4 * el, 50)] for el in range(123, 324, 50)]
list4 = [[*range(el, 10 * el, -243)] for el in range(-123, -324, -4)]
# liste care contin alte liste precum [[1, 2, 3], [2, 3, 4], ...]

# creaza o lista care sa contina toate subliste din listele de mai sus(list1, list2, list3, list4)
# care au primul element un numar par
# exemplu: daca am avea liste list1 = [[1, 2], [2, 4]]
#                             list2 = [[1,2,34], [-2], [3], [12, 99, -1]]
# lista rezultata ar fi resulted_list = [[2, 4], [-2], [12, 99, -1]]
# (sublista [2, 4] incepe cu 2 care e par, la fel si celelalte 3 subliste)
# le spun subliste pentru ca sunt in interiorul altei liste dar pentru python nu sunt cu nimic
# diferite de ate liste
