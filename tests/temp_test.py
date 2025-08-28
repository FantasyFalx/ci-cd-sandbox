import pytest
from main import main


def test_1():
    num = 15
    assert num == main()
    
def test_2():
    num = 22
    assert num != main()