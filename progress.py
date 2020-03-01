#!/usr/bin/env python3
# pylint: disable=C0114,C0116

import time
import sys
from exceptions import InvalidLengthParameterValue

LEFT_BOUND = '['
RIGHT_BOUND = ']'


def generate_progess_string(quantity: int,
                            length: int,
                            progress_symbol: str = '#') -> str:
    if length < 1:
        raise InvalidLengthParameterValue
    percent: float = (quantity / length) * 100
    percent_str = f'{percent}%'
    space_quantity: int = length - quantity
    result: str = (LEFT_BOUND + progress_symbol * quantity +
                   ' ' * space_quantity + RIGHT_BOUND + ' ' + percent_str)
    return result


def display_progress(progress_string: str) -> None:
    print(f'\r{progress_string}', end='')


def main():
    for progress in range(1, 11):
        progress_bar = generate_progess_string(progress, 10)
        display_progress(progress_bar)
        sys.stdout.flush()
        time.sleep(0.5)
    print('')


if __name__ == '__main__':
    main()
