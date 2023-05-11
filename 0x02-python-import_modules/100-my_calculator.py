#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1 as calc
    from sys import argv, exit
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if argv[2] == '+':
        ans = calc.add(int(argv[1]), int(argv[3]))
        print('{} + {} = {}'.format(int(argv[1]), int(argv[3]), ans))
    elif argv[2] == '-':
        ans = calc.sub(int(argv[1]), int(argv[3]))
        print('{} - {} = {}'.format(int(argv[1]), int(argv[3]), ans))
    elif argv[2] == '*':
        ans = calc.mul(int(argv[1]), int(argv[3]))
        print('{} * {} = {}'.format(int(argv[1]), int(argv[3]), ans))
    elif argv[2] == '/':
        ans = calc.div(int(argv[1]), int(argv[3]))
        print('{} / {} = {}'.format(int(argv[1]), int(argv[3]), ans))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
