from family.member import Member
from family import constants

class FamilyTree:
    def __init__(self):
        self.family_tree = {}

    def add_child(self, name, gender, mother_name=None):
        id = len(self.family_tree.keys()) + 1
        member = Member(id, name, gender)
        if not self.family_tree:
            self.family_tree[name] = member
            return constants.CHILD_ADDITION_SUCCEEDED

        if name in self.family_tree:
            return constants.CHILD_ADDITION_FAILED

        mother = self.family_tree.get(mother_name, None)
        if not mother:
            return constants.PERSON_NOT_FOUND

        father = mother.spouse
        if not father:
            return constants.CHILD_ADDITION_FAILED

        member.set_mother(mother)
        member.set_father(father)
        mother.add_child(member)
        father.add_child(member)
        self.family_tree[name] = member
        return constants.CHILD_ADDITION_SUCCEEDED
        