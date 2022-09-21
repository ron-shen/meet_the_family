import pytest
from family.member import Member

@pytest.fixture
def member():
    member = Member(1, "Tony", "Male")
    return member
