from bdb import set_trace
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

    """
        - create member
        - if family_tree is empty
            - return SPOUSE_ADDITION_FAILED
        - if family_tree is not empty
            - if member already exists
                - return SPOUSE_ADDITION_FAILED
            - spouse should be a valid entity
            - if not spouse:
                - return PERSON_NOT_FOUND
            - if spouse.gender == member.gender:
                - return SPOUSE_ADDITION_FAILED
            - if spouse is already married:
                - return SPOUSE_ADDITION_FAILED
            - if all conditions match
                - set_spouse for member
                - set_spouse for spouse
                - create an entry for spouse
                - return SPOUSE_ADDITION_SUCCEDED
    """

    def add_spouse(self, name, gender, spouse_name):
        _id = len(self.family_tree.keys()) + 1
        member = Member(_id, name, gender)

        if not self.family_tree:
            return constants.SPOUSE_ADDITION_FAILED

        if name in self.family_tree:
            return constants.SPOUSE_ADDITION_FAILED

        spouse = self.family_tree.get(spouse_name, None)
        if not spouse:
            return constants.PERSON_NOT_FOUND
        if spouse.gender == member.gender or spouse.spouse is not None:
            return constants.SPOUSE_ADDITION_FAILED

        try:
            member.set_spouse(self.family_tree[spouse.name])
            spouse.set_spouse(member)
            self.family_tree[name] = member
            return constants.SPOUSE_ADDITION_SUCCEEDED
        except ValueError:
            return constants.SPOUSE_ADDITION_FAILED
        