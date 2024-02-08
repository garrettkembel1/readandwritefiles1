import csv

employee_data = open('employee_data.csv', 'r')

csv_file = csv.reader(employee_data)

#this will skip the first record which is the header
next(csv_file)

highly_efficient_individuals = []
low_efficient_individuals = []

employee_40 = []
employee_30 = []
employee_20 = []

count_20 = 0
count_30 = 0
count_40 = 0

for rec in csv_file:
    efficiency = float(rec[5])/float(rec[4])
    age = int(rec[2])
    name = rec[1]
    
    if efficiency >= 2:
        highly_efficient_individuals.append(name)
    elif efficiency <= 1:
        low_efficient_individuals.append(name)


    # Count employees by age group and store names
    if 30 <= age <= 39:
        count_30 += 1
        employee_30.append(name)
    elif 20 <= age <= 29:
        count_20 += 1
        employee_20.append(name)
    elif age >= 40:
        count_40 += 1
        employee_40.append(name)


print('Highly Efficient Individuals:')
for name in highly_efficient_individuals:
    print(name)
print('\n')

print('Low Efficiency Individuals:')
for name in low_efficient_individuals:
    print(name)
print('\n')

# Print employees in their 40s and count
print('Employees in their 40s:')
for name in employee_40:
    print(name)
print('\n')
print(f"Total Number of Employees in their 40's: {count_40}",'\n')

# Print employees in their 30s and count
print('Employees in their 30s:')
for name in employee_30:
    print(name)
print('\n')
print(f"Total Number of Employees in their 30's: {count_30}",'\n')

# Print employees in their 20s and count
print('Employees in their 20s:')
for name in employee_20:
    print(name)
print('\n')
print(f"Total Number of Employees in their 20's: {count_20}")

   