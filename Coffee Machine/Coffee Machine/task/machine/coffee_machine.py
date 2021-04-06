class CoffeeMachine:
    espresso = {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4}
    latte = {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7}
    cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}
    coffee = [espresso, latte, cappuccino]
    instance = None

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    # def __new__(cls, *args):
    #     if cls.instance is None:
    #         cls.instance = cls.__init__(cls, *args)
    #     return cls.instance

    def buy(self):
        s = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
        if s == 'back':
            return
        elif s.isdigit():
            x = int(s) - 1
        else:
            print('Error')
            return

        if self.water >= self.coffee[x]['water'] and self.water >= self.coffee[x]['water'] \
                and self.beans >= self.coffee[x]['beans'] and self.cups >= 1:
            self.water -= self.coffee[x]['water']
            self.milk -= self.coffee[x]['milk']
            self.beans -= self.coffee[x]['beans']
            self.cups -= 1
            self.money += self.coffee[x]['cost']
            print('I have enough resources, making you a coffee!\n')
        else:
            print('I do not have enough resources, making you a coffee!\n')

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))
        print()

    def take(self):
        print(f"I gave you ${self.money}\n")
        self.money = 0

    def menu(self):
        s = input('Write action (buy, fill, take, remaining, exit):\n')
        if s == 'buy':
            self.buy()
        elif s == 'fill':
            self.fill()
        elif s == 'take':
            self.take()
        elif s == 'remaining':
            print(self)
        elif s == 'exit':
            return 0
        else:
            print('Error')
            return 0
        return 1

    def __str__(self):
        return f'The coffee machine has:\n' \
               f'{self.water} of water\n' \
               f'{self.milk} of milk\n' \
               f'{self.beans} of coffee beans\n' \
               f'{self.cups} of disposable cups\n' \
               f'{self.money} of money\n'

    def __repr__(self):
        return f'CoffeeMachine({self.water}, {self.milk}, {self.beans}, {self.cups}. {self.money})'


def main():
    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    while coffee_machine.menu():
        pass


if __name__ == '__main__':
    main()
