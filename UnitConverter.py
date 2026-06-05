"""CLI entry — control layer only."""

from control.flow import run_conversion


def main():
    input_str = input("Insert value for converting (ex: meter:2.5): ")
    print(run_conversion(input_str))


if __name__ == "__main__":
    main()
