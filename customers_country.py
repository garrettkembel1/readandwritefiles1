import csv

#open the file and creates a file object
customers = open('customers.csv', 'r')
outfile = open('customers_country.csv', 'w')

csv_file = csv.reader(customers)

csv_file1 = csv.writer(outfile)

outfile.write('Full Name, Country\n')

#this will skip the first record which is the header
next(csv_file)

for rec in csv_file:
    #print(rec)
    
    outfile.write(f'{rec[1]} {rec[2]}, {rec[4]}\n')


outfile.close()
