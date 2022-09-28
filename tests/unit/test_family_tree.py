import pytest
from family.member import Member, Gender
from unittest.mock import Mock
from family.family_tree import FamilyTree
from family import constants
from . import create_fake_member


@pytest.mark.usefixtures("family")
class TestFamilyTree:
    def test_init(self, family):
        assert family.family_tree == {}

    def test_add_child(self, mocker, family):
        mocker.patch("family.member.Member.set_mother")
        mocker.patch("family.member.Member.set_father")
        mocker.patch("family.member.Member.add_child")
        #if tree is empty
        res = family.add_child("Zim", "Male", "Mother")
        assert len(family.family_tree) == 1
        assert res == constants.CHILD_ADDITION_SUCCEEDED

        mother = create_fake_member(id=2, name="Mother", gender="Female")
        father = create_fake_member(id=2, name="Father", gender="Male")
        assert family.add_child("Zim2", "Male", "Mother") == constants.PERSON_NOT_FOUND

        family.family_tree['Mother'] = mother
        assert family.add_child("Zim2", "Male", "Mother") == constants.CHILD_ADDITION_FAILED
        family.family_tree['Father'] = father
        family.family_tree['Father'].spouse = mother
        family.family_tree['Mother'].spouse = father
        assert family.add_child("Zim2", "Male", "Mother") == constants.CHILD_ADDITION_SUCCEEDED

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
    def test_add_spouse(self, mocker, family):
        mocker.patch("family.member.Member.set_spouse")
        #empty
        assert family.add_spouse("Zim", "Male", "Mother") == constants.SPOUSE_ADDITION_FAILED

        dummy_member = create_fake_member(id=0, name="DummyMember", gender=Gender.male)
        family.family_tree["DummyMember"] = dummy_member #used for passing empty family_tree logic
        spouse_a = create_fake_member(id=2, name="Zim", gender=Gender.male)
        spouse_b = create_fake_member(id=3, name="FakeMember", gender=Gender.female)
        spouse_c = create_fake_member(id=4, name="MarriedMember", gender=Gender.male, spouse=spouse_b)

        assert family.add_spouse("Wife", "Female", "Zim") == constants.PERSON_NOT_FOUND
        family.family_tree["Zim"] = spouse_a
        family.family_tree["FakeMember"] = spouse_b   
        family.family_tree["MarriedMember"] = spouse_c

        assert family.add_spouse("Wife", "Female", "Zim") == constants.SPOUSE_ADDITION_SUCCEEDED
        assert family.add_spouse("Wife", "Female", "FakeMember") == constants.SPOUSE_ADDITION_FAILED   
        assert family.add_spouse("Wife", "Female", "MarriedMember") == constants.SPOUSE_ADDITION_FAILED  
        assert family.add_spouse("Wife", "Female", "Zim") == constants.SPOUSE_ADDITION_FAILED  


    def test_get_relationship(self):
        pass
        










