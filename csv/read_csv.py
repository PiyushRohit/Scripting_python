import csv

with open('test.csv', mode='r') as employee_file:
    employee_reader = csv.reader(employee_file)
    for row in employee_reader:
        print(f"{row[0]:<20} {row[1]:<20} {row[2]}")
