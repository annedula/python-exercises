def compute_pay(hours, rate):
    print("In compute pay", hours, rate)
    if hours > 40:
        rp = 40 * rate
        oth = hours - 40
        otp = oth * (rate * 1.5)
        pay = rp + otp
    else:
        pay = hours * rate
    print("Returning",pay)
    return pay

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

pay = compute_pay(hours, rate)
print("Pay: ", pay)