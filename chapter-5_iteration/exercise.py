total = 0
count = 0
average = 0

while True:
    userInp = input('Enter a number: ')

    if userInp == 'done':
        break

    try:
        inp = int(userInp)
        total = total + inp
        count = count + 1
        average = total / count

    except ValueError:
        print('invalid input')

print(total, count, average)
