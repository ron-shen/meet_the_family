
from enum import Enum
 
class Gender(Enum):
    male = "Male"
    female = "Female"


class Member:
    def __init__(self, id, name, gender):
        self.id = id
        self.name = name
        self.gender = Gender(gender)
        self.mother = None
        self.father = None
        self.spouse = None
        self.children = []

    def set_mother(self, mother):
        if not isinstance(mother, Member):
            raise ValueError("mother must be a Member object")

        if mother.gender == Gender.male:
            raise ValueError("mother cannot be male")

        self.mother = mother

    def set_father(self, father):
        if not isinstance(father, Member):
            raise ValueError("father must be a Member object")

        if father.gender == Gender.female:
            raise ValueError("father cannot be female")

        self.father = father

    def set_spouse(self, spouse):
        if not isinstance(spouse, Member):
            raise ValueError("spouse must be a Member object")

        if spouse.gender == self.gender:
            raise ValueError("spouse must be a opposite gender")

        self.spouse = spouse

    def add_child(self, child):
        if not isinstance(child, Member):
            raise ValueError("spouse must be a Member object")

        self.children.append(child)