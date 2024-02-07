import csv

#open the file and creates a file object
employee_data = open('employee_data.csv', 'r')

csv_file = csv.reader(employee_data)

#this will skip the first record which is the header
next(csv_file)

for rec in csv_file:
    salary = float(rec[3])
    bonus = float(rec[7]) * salary
    pay = salary + bonus
    #print(rec)
    print('\n')
    print(f'Name: {rec[1]}')
    print(f'Salary: $ {salary:.2f}')
    print(f'Bonus: $ {bonus:.2f}')
    print(f'Pay: $ {pay:.2f}')
   