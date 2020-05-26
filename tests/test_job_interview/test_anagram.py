import unittest

from esme_lessons.job_interview.anagrams import anagram


class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        # Given
        n = '68169'
        expected_output = 98660
        # When
        output = anagram(n)

        # Then
        self.assertEqual(expected_output, output)

    def test_anagram_negative(self):
        #Given
        n = -1
        expected_output = None
        #When
        output = anagram(n)
        #Then
        self.assertEqual(expected_output, output)


