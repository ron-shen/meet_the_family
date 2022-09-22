
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

    def get_paternal_grandmother(self):
        if not self.father or not self.father.mother:
            return None

        return self.father.mother

    def get_maternal_grandmother(self):
        if not self.mother or not self.mother.mother:
            return None

        return self.mother.mother

    def get_spouse_mother(self):
        if not self.spouse or not self.spouse.mother:
            return None

        return self.spouse.mother

    def get_paternal_aunt(self):
        grandmother = self.get_paternal_grandmother()
        if not grandmother:
            return []

        aunt = filter(
            lambda child: child.gender == Gender.female, 
            grandmother.children)

        return list(aunt)

    def get_paternal_uncle(self):
        grandmother = self.get_paternal_grandmother()
        if not grandmother:
            return []

        uncle = filter(
            lambda child: child.gender == Gender.male and self.father != child, 
            grandmother.children)
        return list(uncle)       

    def __eq__(self, other) -> bool:
        if isinstance(self, other.__class__):
            return (
                self.id == other.id and 
                self.name == other.name and
                self.gender == other.gender and
                self.mother == other.mother and
                self.father == other.father and
                self.spouse == other.spouse and 
                self.children == other.children
                )
        return False