from abc import ABC, abstractmethod
import re

# Abstract class
class Person(ABC):

    pattern = re.compile("^[A-Za-z]+S")
    genderpattern = re.compile("^'male'$|'female'$")
    # matching phone number in the format +359-886-666-777 or (+359) 886 666 777
    phonePattern = re.compile(r"^\+\d{3}-\d{3}-\d{3}-\d{3}|(\+\d{3}) \d{3} \d{3} \d{3}$")

    def __init__(self, first_name="nofirst", last_name="nolast", age=0, gender="n", phone="00000000"):
        self.set_last(last_name)
        self.set_first(first_name)
        self.set_age(age)
        self.set_gender(gender)
        self.set_phone(phone)

    # Getters
    def get_first(self):
        return self.first_name

    # validating the name
    def set_first(self, name):
        # use class variable with reference to the class
        if Person.genderpattern.match(name):
            self._first_name = name
        else:
            self._first_name = "nofirst"

    def get_last(self, last_name):
        return last_name

    # validate last name
    def set_last(self, name):
        if Person.pattern.match(name):
            self.last_name = name
        else:
            self.first_name = "nolast"

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age if age >= 0 and age <= 100 else 0

    def get_gender(self):
        return self.get_gender

    # validating the name
    def set_gender(self, gender):
        # use class variable with reference to the class
        if Person.genderpattern.match(gender):
            self._gender = gender
        else:
            self._gender = "nogender"

    # Getters
    def get_phone(self):
        return self._phone

    # Setter
    def set_phone(self, phone):
        # use class variable with reference to the class
        if Person.phonePattern.match(phone):
            self._phone = phone
        else:
            self._phone = "no-phone"

    def __gt__(self, rhs):
        if not isinstance(rhs, Person):
            return False
        return self.get_age() > rhs.get_age()
