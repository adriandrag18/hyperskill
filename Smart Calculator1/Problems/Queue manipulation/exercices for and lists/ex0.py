numbers = list(range(5, 100, 7))  # e o lista la fel ca [1, 2, 3] doar ca nu e clar cate elemente
                                  # are sau cate sunt

# printeaza toate elementele pare
# printeaza apoi toate elementele divizible cu 10 sau divizibile cu 8

# HINT: exemplu de verficare paritate
rest = 10 % 2  # operatorul % reprezinta restul impartirii lui 10 la 2
number = 4
if number % 2 == 0:  # daca restul impartirii la 2 este 0 atunci este par
    print(number, "este par")
else:
    print(number, "este impar")
