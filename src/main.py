def greet(name: str) -> str:
    if not name or not name.strip():
        raise ValueError("name is required")
    return f"Hello, {name}"


if __name__ == "__main__":
    print(greet("world"))
