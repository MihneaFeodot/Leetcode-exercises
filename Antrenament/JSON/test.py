import json
import subprocess

class Person:

    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def print_into(self):
        print(self.name, self.weight, self.age)

    def get_older(self, years):
        self.age += years

    def save_to_json(self, filename):
        person_dict = {'name': self.name, 'age': self.age, 'weight': self.weight}
        with open(filename, 'w') as f:
            f.write(json.dumps(person_dict, indent=2))

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())

        self.name = data['name']
        self.weight = data['weight']
        self.age = data['age']


p2 = Person(None, None, None)

p2.load_from_json("Antrenament/JSON/p1_data.json")

p2.print_into()