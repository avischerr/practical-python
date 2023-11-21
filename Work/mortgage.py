# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment = payment + extra_payment
    else:
        payment = 2684.11

    principal = round(principal * (1+rate/12) - payment, ndigits=2)
    total_paid = round(total_paid + payment, ndigits=2)

    print(f'{month} | {total_paid:0.2f} | {principal:0.2f}') 

    month += 1

