#!/usr/bin/env python3
# pylint: disable=C0114,C0116


def generate_progess_string(quantity: int, lenght: int) -> str:
    space_quantity = lenght - quantity
    result = '[' + '#' * quantity + ' ' * space_quantity + ']'
    return result


def display_progress(progress_string: str) -> None:
    print(progress_string)


def main():
    progress = 0
    progress_lenght = 3
    progress_bar = generate_progess_string(progress, progress_lenght)
    display_progress(progress_bar)


if __name__ == '__main__':
    main()
