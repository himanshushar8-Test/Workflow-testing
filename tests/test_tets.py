from Tets import add, greet


def test_greet():
    assert greet("Alice") == "Hello, Alice!"


def test_add():
    assert add(2, 3) == 5
