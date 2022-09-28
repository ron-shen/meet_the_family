import pytest
from family.member import Member
from family.family_tree import FamilyTree

@pytest.fixture(scope="class")
def member():
    member = Member(1, "Tony", "Male")
    return member

@pytest.fixture(scope="class")
def family():
    return FamilyTree()

@pytest.fixture(scope="class")
def member_integration(request):
        request.cls.member = Member(1, "Zim", "Male")
        request.cls.mother = Member(2, "Mother", "Female")
        request.cls.father = Member(3, "Dad", "Male")
        request.cls.mothers_sister_a = Member(4, "MaternalAuntA", "Female")
        request.cls.mothers_sister_b = Member(5, "MaternalAuntB", "Female")
        request.cls.mothers_brother_a = Member(6, "MaternalUncleA", "Male")
        request.cls.mothers_brother_b = Member(7, "MaternalUncleB", "Male")
        request.cls.fathers_sister_a = Member(8, "PaternalAuntA", "Female")
        request.cls.fathers_sister_b = Member(9, "PaternalAuntB", "Female")
        request.cls.fathers_brother_a = Member(10, "PaternalUncleA", "Male")
        request.cls.fathers_brother_b = Member(11, "PaternalUncleB", "Male")
        request.cls.spouse = Member(12, "Wife", "Female")
        request.cls.brother_a = Member(13, "BrotherA", "Male")
        request.cls.brother_b = Member(14, "BrotherB", "Male")
        request.cls.sister_a = Member(15, "SisterA", "Female")
        request.cls.sister_b = Member(16, "SisterB", "Female")
        request.cls.son_a = Member(17, "SonA", "Male")
        request.cls.son_b = Member(18, "SonB", "Male")
        request.cls.daughter_a = Member(19, "DaughterA", "Female")
        request.cls.daughter_b = Member(20, "DaughterB", "Female")
        request.cls.paternal_grandmother = Member(21, "PaternalGrandmother", "Female")
        request.cls.maternal_grandmother = Member(22, "MaternalGrandmother", "Female")

        # adding our parents
        request.cls.member.set_mother(request.cls.mother)
        request.cls.member.set_father(request.cls.father)

        # adding our siblings
        request.cls.father.add_child(request.cls.brother_a)
        request.cls.father.add_child(request.cls.brother_b)
        request.cls.father.add_child(request.cls.sister_a)
        request.cls.father.add_child(request.cls.sister_b)
        request.cls.father.add_child(request.cls.member)
        request.cls.mother.add_child(request.cls.brother_a)
        request.cls.mother.add_child(request.cls.brother_b)
        request.cls.mother.add_child(request.cls.sister_a)
        request.cls.mother.add_child(request.cls.sister_b)
        request.cls.mother.add_child(request.cls.member)

        # add spouse
        request.cls.member.set_spouse(request.cls.spouse)
        request.cls.spouse.set_spouse(request.cls.member)

        # adding our paternal aunt/uncles
        request.cls.paternal_grandmother.add_child(request.cls.fathers_sister_a)
        request.cls.paternal_grandmother.add_child(request.cls.fathers_sister_b)
        request.cls.paternal_grandmother.add_child(request.cls.fathers_brother_a)
        request.cls.paternal_grandmother.add_child(request.cls.fathers_brother_b)
        request.cls.paternal_grandmother.add_child(request.cls.father)
        request.cls.father.set_mother(request.cls.paternal_grandmother)

        # adding our maternal aunt/uncles
        request.cls.maternal_grandmother.add_child(request.cls.mothers_sister_a)
        request.cls.maternal_grandmother.add_child(request.cls.mothers_sister_b)
        request.cls.maternal_grandmother.add_child(request.cls.mothers_brother_a)
        request.cls.maternal_grandmother.add_child(request.cls.mothers_brother_b)
        request.cls.maternal_grandmother.add_child(request.cls.mother)
        request.cls.mother.set_mother(request.cls.maternal_grandmother)

        # adding our sons and daughters
        request.cls.member.add_child(request.cls.son_a)
        request.cls.member.add_child(request.cls.son_b)
        request.cls.member.add_child(request.cls.daughter_a)
        request.cls.member.add_child(request.cls.daughter_b)