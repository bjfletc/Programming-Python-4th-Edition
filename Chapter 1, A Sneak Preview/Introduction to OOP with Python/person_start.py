# Using Classes
# OOP is easy to use in Python, thanks largely to Python’s dynamic typing model. In fact,
# it’s so easy that we’ll jump right into an example: Example 1-14 implements our database
# records as class instances rather than as dictionaries.

class Person:

    def __init__(self, name, age, pay=0, job=None):

        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    brandon = Person('Brandon Fletcher', 24, 20000, 'software')
    print(bob.name, sue.pay, brandon.job)

    print(bob.name.split()[-1])
    brandon.pay *= 1.10
    print(brandon.pay)
