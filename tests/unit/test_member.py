import pytest
from family.member import Member
from family.member import Gender

@pytest.mark.usefixtures("member")
class TestMember:

    def test_init(self, member):
        #check instance
        assert isinstance(member, Member)

        #check attributes
        assert member.id == 1
        assert member.name == "Tony"
        assert member.gender == Gender.male
        assert member.mother == None
        assert member.father == None
        assert member.spouse == None
        assert member.children == []

        #edege case for gender

    def test_set_mother(self, member):
        mother_demo_a = "mother_demo_a"
        mother_demo_b = Member(2, "MotherDemoB", "Male")
        mother_demo_c = Member(3, "Mom", "Female")

        #error case
        with pytest.raises(ValueError):
            member.set_mother(mother_demo_a)
            member.set_mother(mother_demo_b)

        #success case
        member.set_mother(mother_demo_c)
        assert member.mother.name == "Mom"
        assert member.mother.gender == Gender.female

    def test_set_father(self, member):
        father_demo_a = "father_demo_a"
        father_demo_b = Member(2, "FatherDemoB", "Female")
        mother_demo_c = Member(3, "Dad", "Male")

        #error case
        with pytest.raises(ValueError):
            member.set_father(father_demo_a)
            member.set_father(father_demo_b)

        #success case
        member.set_father(mother_demo_c)
        assert member.father.name == "Dad"
        assert member.father.gender == Gender.male

    def test_set_spouse(self, member):
        spouse_demo_a = "father_demo_a"
        spouse_demo_b = Member(2, "spouse_demo_b", "Male")
        spouse_demo_c = Member(3, "spouse", "Female")

        #error case
        with pytest.raises(ValueError):
            member.set_spouse(spouse_demo_a)
            member.set_spouse(spouse_demo_b)

        #success case
        member.set_spouse(spouse_demo_c)
        assert member.spouse.name == "spouse"
        assert member.spouse.gender == Gender.female

    def test_add_child(self, member):
        child_demo_a = "child_demo_a"
        child_demo_b = Member(2, "Daugther", "Female")

        #error case
        with pytest.raises(ValueError):
            member.set_spouse(child_demo_a)

        #success case
        member.add_child(child_demo_b)
        assert len(member.children) == 1
        assert member.children[0].name == "Daugther"
        assert member.children[0].gender == Gender.female

    def test_get_paternal_grandmother(self):
        member = Member(5, "Newmember", "Male")
        father = Member(9, "Newmember", "Male")
        grandmother = Member(11, "Newmember_grandmother", "Female")
        #error case
        assert member.get_paternal_grandmother() == None

        member.father = father
        assert member.get_paternal_grandmother() == None

        member.father.mother = grandmother
        assert member.get_paternal_grandmother() == grandmother

    def test_get_maternal_grandmother(self):
        member = Member(5, "Newmember", "Male")
        mother = Member(9, "Newmember", "Female")
        grandmother = Member(11, "Newmember_grandmother", "Female")
        #error case
        assert member.get_maternal_grandmother() == None

        member.mother = mother
        assert member.get_maternal_grandmother() == None

        member.mother.mother = grandmother
        assert member.get_maternal_grandmother() == grandmother

    def test_get_spouse_mother(self):
        member = Member(5, "Newmember", "Male")
        spouse = Member(9, "Newmember", "Female")
        spouse_mother = Member(11, "spouse_mother", "Female")
        #error case
        assert member.get_spouse_mother() == None

        member.spouse = spouse
        assert member.get_spouse_mother() == None

        member.spouse.mother = spouse_mother
        assert member.get_spouse_mother() == spouse_mother

    def test_get_paternal_aunt(self, member, mocker):
        mocker.patch("family.member.Member.get_paternal_grandmother", return_value=Member(10, "test", "Female"))
        
        #check for None value
        assert member.get_paternal_aunt() == None






