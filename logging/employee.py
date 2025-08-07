import logging

# Set up logging
logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

class Employee:
    '''A sample Employee Class'''

    def __init__(self, first, last):  # ✅ Corrected from _init_ to __init__
        self.first = first
        self.last = last

        # Log the creation of an employee using the properties
        logging.info(f'Created Employee: {self.fullname} - {self.email}')

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


# Creating employee instances
emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')
