import pytest


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return []


@pytest.fixture
def append_first(order, first_entry):
    order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    print(append_first)
    print(order)
    print(first_entry)
    assert order == [first_entry]


# def test_string_and_int(order, first_entry):
#     order.append(2)
#     assert order == [first_entry, 2]