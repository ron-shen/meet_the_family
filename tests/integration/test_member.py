import pytest
from family.member import Member, Gender

@pytest.mark.usefixtures("member_integration")
class TestMember:
    def test_set_methods(self, member):
        # test parents 
        assert self.member.mother.name == "Mother"
        assert self.member.father.name == "Dad"
        assert self.member in self.member.father.children
        assert self.member in self.member.mother.children

        # test siblings
        assert len(self.member.mother.children) == 5
        assert self.brother_a in self.member.mother.children
        assert self.brother_b in self.member.mother.children
        assert self.sister_a in self.member.mother.children
        assert self.sister_b in self.member.mother.children
        assert len(self.member.father.children) ==  5
        assert self.brother_a in self.member.father.children
        assert self.brother_b in self.member.father.children
        assert self.sister_a in self.member.father.children
        assert self.sister_b in self.member.father.children

        # test spouse
        assert self.member.spouse.name == "Wife"

        # test paternal/maternal aunts and uncles
        assert len(self.member.mother.mother.children) == 5
        assert self.mothers_brother_a in self.member.mother.mother.children
        assert self.mothers_brother_b in self.member.mother.mother.children
        assert self.mothers_sister_a in self.member.mother.mother.children
        assert self.mothers_sister_b in self.member.mother.mother.children
        assert self.mother in self.member.mother.mother.children
        assert len(self.member.father.mother.children) == 5
        assert self.fathers_brother_a in self.member.father.mother.children
        assert self.fathers_brother_b in self.member.father.mother.children
        assert self.fathers_sister_a in self.member.father.mother.children
        assert self.fathers_sister_b in self.member.father.mother.children
        assert self.father in self.member.father.mother.children

        # # test children
        assert len(self.member.children) == 4
        assert self.son_a in self.member.children
        assert self.son_b in self.member.children
        assert self.daughter_a in self.member.children
        assert self.daughter_b in self.member.children

    def test_get_relationship_methods(self):
        assert len(self.member.get_relationship("paternal_aunt")) == 2
        assert len(self.member.get_relationship("paternal_uncle")) == 2
        assert len(self.member.get_relationship("maternal_aunt")) == 2
        assert len(self.member.get_relationship("maternal_uncle")) == 2
        assert len(self.member.get_relationship("siblings")) == 4
        assert len(self.member.get_relationship("son")) == 2
        assert len(self.member.get_relationship("daughter")) == 2
        assert len(self.member.spouse.get_relationship("brother_in_law")) == 2
        assert len(self.member.spouse.get_relationship("sister_in_law")) == 2


