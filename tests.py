from unittest import TestCase

from progress import generate_progess_string


class TestGenerateProgressString(TestCase):
    def test_progress_string_startswith_open_bracket(self):
        progress = 1
        lenght = 3
        progress_bar = generate_progess_string(progress, lenght)        
        self.assertEqual(progress_bar[0], '[')

    def test_progress_string_endswith_close_bracket(self):
        progress = 3
        lenght = 6
        progress_bar = generate_progess_string(progress, lenght)
        self.assertEqual(progress_bar[-1], ']') 

    def test_progress_string_has_correct_lenght(self):
        progress_bar_len = 30
        progress_bar = generate_progess_string(quantity = 3, lenght = progress_bar_len)
        progress_string = progress_bar[1:progress_bar.index(']')]
        self.assertEqual(len(progress_string), progress_bar_len)

    def test_progress_string_has_correct_space_quantity(self):
        progress_bar_len = 16
        progress_bar_quantity = 11
        progress_bar = generate_progess_string(
            quantity=progress_bar_quantity, 
            lenght=progress_bar_len
        )
        progress_string = progress_bar[1:progress_bar.index(']')]
        expected = progress_bar_len - progress_bar_quantity
        actual = progress_string.count(' ')
        self.assertEqual(actual, expected)