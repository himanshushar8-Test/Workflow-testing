import argparse


def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def build_summary(name: str, a: int, b: int) -> str:
    return f"{greet(name)} Sum={add(a, b)}, Product={multiply(a, b)}"


def main() -> None:
    parser = argparse.ArgumentParser(description="A simple Python demo script")
    parser.add_argument("--name", default="GitHub Actions", help="Name to greet")
    parser.add_argument("--a", type=int, default=2, help="First number")
    parser.add_argument("--b", type=int, default=3, help="Second number")
    args = parser.parse_args()

    print(build_summary(args.name, args.a, args.b))


if __name__ == "__main__":
    main()
