import csv

with open('test.csv', mode='a', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['Piyush Rohit', 'RTL design', 'July'])
    employee_writer.writerow(['Ankur Mishra', 'RTL Verification', 'June'])
