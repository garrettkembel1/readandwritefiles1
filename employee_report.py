import csv

employee_data = open('employee_data.csv', 'r')

csv_file = csv.reader(employee_data)

#this will skip the first record which is the header
next(csv_file)


for rec in csv_file:
    efficiency = float(rec[5])/float(rec[4])
    age = float(rec[2])
    #bonus = float(rec[7]) * salary
    #pay = salary + bonus
    #print(rec)
    if efficiency >2:
        print('Highly Efficent Individuals','\n')
        print(rec[1])
        #print(f'Salary: $ {salary:.2f}')
        #print(f'Bonus: $ {bonus:.2f}')
        #print(f'Pay: $ {pay:.2f}')
    elif efficiency <1:
        print('Low Efficency Individuals','\n')
        print(rec[1])

    
    if age