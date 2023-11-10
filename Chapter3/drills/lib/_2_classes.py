# == INSTRUCTIONS ==
#
# In these exercises you will build small classes.
#
# The first ones will be familiar, do them without looking at your previous
# work. The later ones will be more complex.
#
# Here is an example of some exercise instructions and a solution.
#
# Class name: ExampleGreeter
# Purpose: say hello and goodbye to a user with a given name
# Methods:
#   1. Name: __init__
#      Arguments: one, a string representing a name
#   2. Name: say_hello
#      Arguments: none
#      Returns: a string like 'Hello, NAME!'
#   3. Name: say_goodbye
#      Arguments: none
#      Returns: a string like 'Goodbye, NAME!'
# Example usage:
#   > greeter = ExampleGreeter('Bobby')
#   > greeter.say_hello()
#   'Hello, Bobby!'
#   > greeter.say_goodbye()
#   'Goodbye, Bobby!'
#
# Example solution:
# class ExampleGreeter():
#     def __init__(self, name):
#         self.name = name
#     def say_hello(self):
#         return 'Hello, ' + self.name + '!'
#     def say_goodbye(self):
#         return 'Goodbye, ' + self.name + '!'



# == EXERCISES ==

# Class name: Greeter
# Purpose: say various greetings to a user with a given name
# Methods:
#   1. Name: hello
#      Arguments: one, a string representing a name
#      Returns: a string like 'Hello, NAME!'
#   2. Name: goodbye
#      Arguments: one, a string representing a name
#      Returns: a string like 'Goodbye, NAME!'
#   3. Name: good_night
#      Arguments: one, a string representing a name
#      Returns: a string like 'Good night, NAME!'
#   4. Name: good_morning
#      Arguments: one, a string representing a name
#      Returns: a string like 'Good morning, NAME!'
# Example usage:
#   > greeter = Greeter()
#   > greeter.hello('Bobby')
#   'Hello, Bobby!'
#   > greeter.goodbye('Bobby')
#   'Goodbye, Bobby!'
#   > greeter.good_night('Bobby')
#   'Good night, Bobby!'
#   > greeter.good_morning('Bobby')
#   'Good morning, Bobby!'
class Greeter():
    def hello(self, name):
        return f'Hello, {name}!'
    
    def goodbye(self, name):
        return f'Goodbye, {name}!'
    
    def good_night(self, name):
        return f'Good night, {name}!'
    
    def good_morning(self, name):
        return f'Good morning, {name}!'



# Class name: Basket
# Purpose: store a list of items
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: one item of any type
#      Returns: nothing
#   3. Name: list_items
#      Arguments: none
#      Returns: a list of all the items that have been added
# Example usage:
#   > basket = Basket()
#   > basket.add('apple')
#   > basket.add('banana')
#   > basket.add('orange')
#   > basket.list_items()
#   ['apple', 'banana', 'orange']
class Basket():
    def __init__(self):
        self.items = []

    def add(self, one):
        self.items.append(one)

    def list_items(self):
        return self.items

# Class name: Calculator
# Purpose: perform simple calculations and track the history
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: two numbers
#      Returns: the result of adding the two numbers
#   3. Name: multiply
#      Arguments: two numbers
#      Returns: the result of multiplying the first by the second
#   4. Name: subtract
#      Arguments: two numbers
#      Returns: the result of subtracting the second from the first
#   5. Name: divide
#      Arguments: two numbers
#      Returns: the result of dividing the first by the second
#   6. Name: list_history
#      Arguments: none
#      Returns: a list of all the previous results calculations
# Example usage:
#   > calculator = Calculator()
#   > calculator.add(1, 2)
#   3
#   > calculator.multiply(3, 4)
#   12
#   > calculator.subtract(5, 6)
#   -1
#   > calculator.divide(7, 8)
#   0.875
#   > calculator.list_history()
#   [3, 12, -1, 0.875]
class Calculator():
    def __init__(self):
        self.calculation_history = []
    
    def add(self, number1, number2):
        result = number1 + number2
        self.calculation_history.append(result)
        return result
    
    def multiply(self, number1, number2):
        result = number1 * number2
        self.calculation_history.append(result)
        return result
    
    def subtract(self, number1, number2):
        result = number1 - number2
        self.calculation_history.append(result)
        return result
    
    def divide(self, number1, number2):
        result = number1/number2
        self.calculation_history.append(result)
        return result
    
    def list_history(self):
        return self.calculation_history
    

# Class name: Cohort
# Purpose: store a list of students
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add_student
#      Arguments: one dictionary representing a student
#      Returns: nothing
#   3. Name: list_students
#      Arguments: none
#      Returns: a list of all the students that have been added
#   4. Name: list_employed_by
#      Arguments: one string, the name of an employer
#      Returns: a list of all the students who work for that employer
# Example usage:
#   > cohort = Cohort()
#   > cohort.add_student({'name' : 'Jo', 'employer' : 'NASA'})
#   > cohort.add_student({'name' : 'Alex', 'employer' : 'NASA'})
#   > cohort.add_student({'name' : 'Bobby', 'employer' : 'Google'})
#   > cohort.list_students()
#   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}, {'name' : 'Bobby', 'employer' : 'Google'}]
#   > cohort.list_employed_by('NASA')
#   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}]
class Cohort():
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        return self.students
    
    def list_employed_by(self, employer):
        employed_students = [student for student in self.students if student.get('employer') == employer]
        return employed_students

# Class name: Person
# Purpose: store a person's name, pets and addresses
# Methods:
#   1. Name: __init__
#      Arguments: one complex dictionary, see below for structure.
#   2. Name: get_work_address
#      Arguments: none
#      Returns: the work address in a nice format
#   3. Name: get_home_address
#      Arguments: none
#      Returns: the home address in a nice format
#   4. Name: get_pets
#      Arguments: none
#      Returns: a nice summary of the person's pets
# Example usage:
#   > person = Person({
#       'name' : 'Alex',
#       'pets' : [
#         {'name' : 'Arthur', 'animal' : 'cat'},
#         {'name' : 'Judith', 'animal' : 'dog'},
#         {'name' : 'Gwen', 'animal' : 'goldfish'}
#       ],
#       'addresses' : [
#         {'name' : 'work', 'building' : '50', 'street' : 'Commercial Street'},
#         {'name' : 'home', 'building' : '10', 'street' : 'South Street'}
#       ]
#     })
#   > person.get_work_address()
#   '50 Commercial Street'
#   > person.get_home_address()
#   '10 South Street'
#   > person.get_pets()
#   'Alex has 3 pets: a cat called Arthur, a dog called Judith, a goldfish called Gwen'
class Person:
    def __init__(self, data):
        self.name = data['name']
        self.pets = data['pets']
        self.addresses = data['addresses']

    def get_work_address(self):
        work_address = next((addr for addr in self.addresses if addr['name'] == 'work'))
        return f"{work_address['building']} {work_address['street']}"

    def get_home_address(self):
        home_address = next((addr for addr in self.addresses if addr['name'] == 'home'))
        return f"{home_address['building']} {home_address['street']}"

    def get_pets(self):
        pet_count = len(self.pets)
        pet_descriptions = [f"a {pet['animal']} called {pet['name']}" for pet in self.pets]
        return f"{self.name} has {pet_count} pets: {', '.join(pet_descriptions)}"

# class Person:
#     def __init__(self, data):
#         self.name = data['name']
#         self.pets = data['pets']
#         self.addresses = data['addresses']

#     def get_work_address(self):
#         for address in self.addresses:
#             if address['name'] == 'work':
#                 return f"{address['building']} {address['street']}"

#     def get_home_address(self):
#         for address in self.addresses:
#             if address['name'] == 'home':
#                 return f"{address['building']} {address['street']}"

#     def get_pets(self):
#         pet_names = [pet['name'] for pet in self.pets]
#         pet_animals = [pet['animal'] for pet in self.pets]
#         pet_summary = ", ".join([f"a {animal} called {name}" for name, animal in zip(pet_names, pet_animals)])
#         return f"{self.name} has {len(self.pets)} pets: {pet_summary}"