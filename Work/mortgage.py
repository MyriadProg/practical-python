# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000.0
months_paid = 1

while principal > 0:
    if months_paid <= 12:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
        
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    months_paid = months_paid + 1


print('Total paid ', round(total_paid, 2), end='')
print('  ', end='')
print('Months paid', months_paid)