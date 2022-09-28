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


    def test_add_spouse(self):
        pass

    def test_get_relationship(self):
        pass
        










