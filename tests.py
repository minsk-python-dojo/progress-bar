from unittest import TestCase

from progress import generate_progess_string, LEFT_BOUND, RIGHT_BOUND
from exceptions import InvalidLengthParameterValue


class TestGenerateProgressString(TestCase):
    def test_progress_string_startswith_open_bracket(self):
        progress = 1
        length = 3
        progress_bar = generate_progess_string(progress, length)
        self.assertEqual(progress_bar[0], LEFT_BOUND)

    def test_progress_string_endswith_close_bracket(self):
        progress = 3
        length = 6
        progress_bar = generate_progess_string(progress, length)
        closing_bracket_index: int = progress_bar.index(RIGHT_BOUND)
        self.assertEqual(progress_bar[closing_bracket_index], RIGHT_BOUND)

    def test_progress_string_has_correct_length(self):
        progress_bar_len = 30
        progress_bar = generate_progess_string(quantity=3,
                                               length=progress_bar_len)
        progress_string = progress_bar[1:progress_bar.index(RIGHT_BOUND)]
        self.assertEqual(len(progress_string), progress_bar_len)

    def test_progress_string_has_correct_space_quantity(self):
        progress_bar_len = 16
        progress_bar_quantity = 11
        progress_bar = generate_progess_string(quantity=progress_bar_quantity,
                                               length=progress_bar_len)
        progress_string = progress_bar[1:progress_bar.index(RIGHT_BOUND)]
        expected = progress_bar_len - progress_bar_quantity
        actual = progress_string.count(' ')
        self.assertEqual(actual, expected)

    def test_generate_progess_string_raises_exeption_if_length_less_than_one(
        self):
        progress = 42
        progress_length = -5

        with self.assertRaises(InvalidLengthParameterValue):
            generate_progess_string(progress, progress_length)

    def test_generate_progess_string_contains_50_percents_if_progress_equals_50_and_length_equals_100(
        self):
        progress = 50
        progress_length = 100
        expected_suffix = '50.0%'
        result = generate_progess_string(progress, progress_length)
        suffix_index = result.index(expected_suffix)
        actual_suffix = result[suffix_index:]
        self.assertEquals(actual_suffix, expected_suffix)
