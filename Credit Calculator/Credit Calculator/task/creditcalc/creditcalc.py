import math
import argparse


def main():
    parser = argparse.ArgumentParser(description='Credit Calculator')
    parser.add_argument('--type', help='differentiated or annuity payment')
    parser.add_argument('--principal', type=int, help='the credit principal')
    parser.add_argument('--periods', type=int, help='the number of months needed to repay the credit')
    parser.add_argument('--payment', type=float, help='the monthly payment')
    parser.add_argument('--interest', type=float, help='is specified without a percent sign')
    args = parser.parse_args()
    if (args.principal and args.principal < 0) or (args.payment and args.payment < 0) or \
            (args.periods and args.periods < 0) or (args.interest and args.interest < 0):
        print('Incorrect parameters')
    if not args.interest:
        print('Incorrect parameters')
        exit()
    if args.type != 'diff' and args.type != 'annuity':
        print('Incorrect parameters')
    elif args.type == 'annuity':
        args.interest = args.interest / 1200
        if not args.principal and args.payment and args.periods:
            args.principal = math.floor(args.payment * ((1 + args.interest) ** args.periods - 1) /
                                        (args.interest * (1 + args.interest) ** args.periods))
            print(f'Your credit principal = {args.principal}!')
        elif args.principal and not args.payment and args.periods:
            args.payment = math.ceil(args.principal * args.interest * (1 + args.interest) ** args.periods /
                                     ((1 + args.interest) ** args.periods - 1))
            print(f'Your annuity payment = {args.payment}!')
        elif args.principal and args.payment and not args.periods:
            args.periods = math.ceil(math.log(
                args.payment / (args.payment - args.interest * args.principal), 1 + args.interest))
            years, months = divmod(args.periods, 12)
            print('You need', end=' ')
            if years:
                print(years, 'years', end=' ')
            if months:
                print(months, 'months ', end=' ')
            print('to repay this credit!')
        else:
            print('Incorrect parameters')
            exit()
        overpayment = round(args.periods * args.payment - args.principal)
        print(f'Overpayment = {overpayment}')
    elif args.type == 'diff':
        if not (args.principal and args.periods):
            print('Incorrect parameters')
            exit()
        args.interest = args.interest / 1200
        total = 0
        for m in range(1, args.periods + 1):
            payment = math.ceil(args.principal / args.periods
                                + args.interest * (args.principal * (1 - (m - 1) / args.periods)))
            total += payment
            print(f'Month {m}: paid out {payment}')
        overpayment = total - args.principal
        print(f'Overpayment = {overpayment}')


if __name__ == '__main__':
    main()
