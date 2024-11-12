# Person model class representing a generic person with basic attributes.
class Person:
    def __init__(self, id, name, age, address):
        """
        Initialize a person with name, age, and address.
        :param id: Unique ID for the person
        :param name: Name of the person
        :param age: Age of the person
        :param address: Address of the person
        """
        self.person_id = id
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f"Person(id={self.person_id}, name='{self.name}', age={self.age}, address='{self.address}')"
