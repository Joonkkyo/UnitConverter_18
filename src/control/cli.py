"""Console entry point — `unit-converter` script after pip install -e."""

from control.flow import run_conversion


def main() -> None:
    input_str = input("Insert value for converting (ex: meter:2.5): ")
    print(run_conversion(input_str))
