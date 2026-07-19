from Tets import add, greet, build_summary, multiply


def test_greet():
    assert greet("Alice") == "Hello, Alice!"


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(4, 5) == 20


def test_build_summary():
    assert build_summary("Bob", 2, 3) == "Hello, Bob! Sum=5, Product=6"
