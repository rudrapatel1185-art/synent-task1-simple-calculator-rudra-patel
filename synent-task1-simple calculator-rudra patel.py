
"""
Simple Command-Line Calculator
Supports: Addition, Subtraction, Multiplication, Division
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "+": ("Addition",       add),
    "-": ("Subtraction",    subtract),
    "*": ("Multiplication", multiply),
    "/": ("Division",       divide),
}


def get_number(prompt):
    """Prompt the user until a valid number is entered."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"  ✗ '{raw}' is not a valid number. Please try again.")


def get_operator():
    """Prompt the user until a valid operator is entered."""
    ops = " / ".join(OPERATIONS)
    while True:
        raw = input(f"  Operator ({ops}): ").strip()
        if raw in OPERATIONS:
            return raw
        print(f"  ✗ '{raw}' is not a valid operator. Choose from: {ops}")


def format_number(n):
    """Display as int when the result is a whole number."""
    return int(n) if n == int(n) else n


def main():
    print("=" * 40)
    print("       Simple CLI Calculator")
    print("  Type 'q' at any prompt to quit.")
    print("=" * 40)

    while True:
        print()

        # --- First operand ---
        raw = input("  First number (or 'q' to quit): ").strip()
        if raw.lower() == "q":
            break
        try:
            a = float(raw)
        except ValueError:
            print(f"  ✗ '{raw}' is not a valid number.")
            continue

        # --- Operator ---
        op_symbol = get_operator()

        # --- Second operand ---
        b = get_number("  Second number: ")

        # --- Calculate ---
        name, func = OPERATIONS[op_symbol]
        try:
            result = func(a, b)
            print(f"\n  {format_number(a)} {op_symbol} {format_number(b)} "
                  f"= {format_number(result)}")
        except ZeroDivisionError as e:
            print(f"  ✗ Error: {e}")

        # --- Continue? ---
        print()
        again = input("  Another calculation? (y / n): ").strip().lower()
        if again != "y":
            break

    print("\n  Goodbye!\n")


if __name__ == "__main__":
    main()