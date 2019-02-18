## Animal is a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    something = "lol"
    def __init__(self, Animal_something):
        self.something = Animal_something
    def print_something(self):
        print(self.something)
    pass

## Dog is-a/inherits from Animal and has-a __init__ that takes self and name params 
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name-attribute; get name-attribute from Dog and set it to variable "name"
        self.name = name

## Cat is-a/inherits from Animal and has-a __init__ that takes self and name params
class Cat(Animal):
    def __init__(self, name):
        ## get name-attribute from self-attribute and set it to variable "name"
        self.name = name
    def print_name(self):
        print(self.name)


## Person is-a/inherits from object and has-a __init__ that takes self and name params
class Person(object):
    def __init__(self, name):
        ## get name-attribute from Person and set it to variable "name"
        self.name = name
        ## Person has-a pet of some kind 
        self.pet = None 
    def print_name(self):
        print(self.name)
    def print_pet(self):
        print(self.pet.name)

## Employee is-a/inherits from Person and has-a __init__ that takes self, name, salary params 
class Employee(Person):
    def __init__(self, name, salary):
        ## super refers to parent class "Person" and runs __init__ of parent class "Person"
        super(Employee, self).__init__(name)
        ## get salary-attribute from Employee and set it to salary
        self.salary = salary

## Fish is-a/inherits from object
class Fish(object):
    pass

## Salmon is-a/inherits from Fish
class Salmon(Fish):
    pass

## Halibut is-a/inherits from Fish
class Halibut(Fish):
    pass

## rover is-a/instance of Dog and name-attribute is set to "Rover"
rover = Dog("Rover")

## satan is-a/instance Cat and name-attribute is set to "Satan"
satan = Cat("Satan")
satan.print_name()
satan.print_something()
## mary is-a/instance of Person and name-attribute is set to "Mary"
mary = Person("Mary")

## get pet-attribute from instance mary and set it to "satan"
mary.pet = satan

## frank is-a/instance of Employee, name-attribute is set to "Frank", salary-attribute is set to "120000"
frank = Employee("Frank", 120000)

## set pet-attribute of instance "frank" to "rover"
frank.pet = rover
frank.print_name()
frank.print_pet()
## instance "flipper" is-a/inherits from Fish
flipper = Fish()

## instance "crouse" is-a/inherits from Salmon
crouse = Salmon()

## instance "harry" is-a/inherits from Halibut
harry = Halibut()
