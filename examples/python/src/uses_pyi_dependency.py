from python_lib.dependency import greet


def main() -> None:
    message: int = greet("World")
    print(message)
