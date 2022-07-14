def is_one_digit(n):
    if int(n) == n and -10 < n < 10:
        return True
    return False


def check(x, y, oper):
    msg = ''
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and oper == '*':
        msg += msg_7
    if (x == 0 or y == 0) and oper in opers_without_division:
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

available_opers = '+-*/'
opers_without_division = '+-*'

memory = 0

while True:
    print(msg_0)
    calc = input()

    try:
        x, oper, y = calc.split(' ', 3)
    except ValueError:
        continue
    try:
        if x == 'M':
            x = memory
            if y == 'M':
                y = memory
            else:
                y = float(y)
        else:
            x = float(x)
            if y == 'M':
                y = memory
            else:
                y = float(y)

    except ValueError:
        print(msg_1)
        continue

    if oper not in available_opers:
        print(msg_2)
        continue

    check(x, y, oper)

    result = 0
    try:
        match oper:
            case '+':
                result = x + y
            case '-':
                result = x - y
            case '*':
                result = x * y
            case '/':
                result = x / y
        print(result)
    except ZeroDivisionError:
        print(msg_3)
        continue

    answer = ''
    while answer != 'y' and answer != 'n':
        print(msg_4)
        answer = input()
        if answer == 'y':
            if is_one_digit(result):

                msg_index = 10
                answer = ''

                while answer != 'y' and answer != 'n' or msg_index <= 12:
                    print(locals().get(f'msg_{msg_index}'))
                    answer = input()
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index += 1
                        else:
                            memory = result
                            break
                    elif answer == 'n':
                        break
            else:
                memory = result

            break

    answer = ''
    while answer != 'y' and answer != 'n':
        print(msg_5)
        answer = input()
    if answer == 'n':
        break
