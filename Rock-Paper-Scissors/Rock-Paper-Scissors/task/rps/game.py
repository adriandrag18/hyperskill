import random

game = ['rock', 'paper', 'scissors']


def parse_rating():
    fin = open('rating.txt')
    d = dict()
    for line in fin:
        d.update({line.split()[0]: int(line.split()[1])})
    return d


ratings = parse_rating()
name = input('Enter your name: ')
print('Hello, ', name)
if name not in ratings.keys():
    ratings.update({name: 0})
while True:
    computer = random.choice(game)
    user = input()
    if user == '!exit':
        break
    if user == '!rating':
        print('Your rating: ', ratings[name])
        continue
    elif user not in game:
        print('Invalid input')
        continue
    c = game.index(computer)
    u = game.index(user)
    if c == u:
        print(f'There is a draw ({computer})')
        ratings[name] += 50
    elif c - u == 1 or c - u == -2:
        print(f'Sorry, but computer chose {computer}')
    else:
        print(f'Well done. Computer chose {computer} and failed')
        ratings[name] += 100
print('Bye!')
