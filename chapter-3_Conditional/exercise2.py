hours = input('Enter Hours: ')

try:
    hourly_work = int(hours)

except:
    print('Error! please enter numeric input')
    quit()

rate = input('Enter Rate: ')

try:
    hourly_rate = float(rate)
except:
    print('Error! please enter numeric input')
    quit()

employee_pay = hours * rate
print('Pay: ', employee_pay)