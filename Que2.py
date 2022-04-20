print ('Enter income: ')
income = float(input())
deduction = 10000
taxable_income = income-deduction
print ('Enter number of dependents: ')
dependents = int(input())
taxable_income = taxable_income - 3000 * dependents
tax = taxable_income/5.0
round (tax ,2)
print ('Tax: ')
print(tax)