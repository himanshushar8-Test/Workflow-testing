def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(greet("GitHub Actions"))
    print(add(2, 3))
