"""CLI entry — delegates to ECB modules."""

from boundary.input import parse_input, validate_raw
from entity.converter import convert_all


def main():
    input_str = input("Insert value for converting (ex: meter:2.5): ")

    error = validate_raw(input_str)
    if error:
        print(error)
        return

    unit, value = parse_input(input_str)
    results = convert_all(unit, value)

    for target_unit, converted in results.items():
        print(f"{value} {unit} = {converted} {target_unit}")


if __name__ == "__main__":
    main()
