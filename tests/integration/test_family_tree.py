import pytest
from family.member import Member, Gender
from unittest.mock import Mock
from family.family_tree import FamilyTree
from family import constants
from family.member import Member


@pytest.mark.usefixtures("family")
class TestFamilyTree:
    def test_add_child(self, family):
        assert family.add_child("Father", "Male") == constants.CHILD_ADDITION_SUCCEEDED
        assert family.family_tree["Father"].name == "Father"

        assert family.add_child("Zim", "Male", "Mother") == constants.PERSON_NOT_FOUND
        assert family.add_child("Zim", "Male", "Father") == constants.CHILD_ADDITION_FAILED


        mother = Member(2, "Mother", "Female")
        mother.set_spouse(family.family_tree["Father"])
        family.family_tree["Father"].set_spouse(mother)
        family.family_tree["Mother"] = mother

        assert family.add_child("Zim", "Male", "Mother") == constants.CHILD_ADDITION_SUCCEEDED
        assert family.add_child("Zim", "Male", "Mother") == constants.CHILD_ADDITION_FAILED
        assert family.family_tree.get("Zim", None) is not None


    def add_spouse(self):
        pass

    def test_get_relationship(self):
        pass
        










