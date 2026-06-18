minimum = None
maximum = None

while True:
        inp = input('Enter a number: ')

        if inp == 'done':
            break
        
        try:
            num = int(inp)

            if maximum is None or num > maximum:
                maximum = num

            if minimum is None or num < minimum:
                minimum = num

        except ValueError:
            print('Invalid input')

print(minimum, maximum)

