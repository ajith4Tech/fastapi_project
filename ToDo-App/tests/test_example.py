'''
Testing: This is a test written using pytest.
Pytest: It is a testing framework for Python which works both unit
and integration testing.
'''
import pytest

def test_equal_or_not_equal():
    assert 3!=1
    assert 3==3

def test_is_instance():
    assert isinstance('This is a string', str)
    assert not isinstance('10', int)

def test_boolean():
    validated = True
    assert validated is True
    assert(100 == 100)
    
def test_type():
    assert type(100) == int
    assert type('This is a string') == str

def test_greater_than_and_less_than():
    assert 3 > 2
    assert 3 < 4
    
def test_list():
    num_list = [1,2,3]
    any_list = [False, False]
    assert 1 in num_list
    assert 4 not in num_list
    assert all(num_list)
    assert not any(any_list)
    

class Student:
    def __init__(self, first_name: str, last_name:str, major:str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years


@pytest.fixture
def default_student():
    return Student('John', 'Doe', 'Computer Science', 4)


def test_person_initialization(default_student):
    
    assert default_student.first_name == 'John', 'First name should be John'
    assert default_student.last_name == 'Doe', 'Last name should be Doe'
    assert default_student.major == 'Computer Science', 'Major should be Computer Science'
    assert default_student.years == 4
    
    