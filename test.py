import unittest
from questions import questions, answers


class TestQuestions(unittest.TestCase):
    def test_questions_have_answers(self):
        """
        Test that all the questions have a
        corresponding answer.
        """
        for key, question in enumerate(questions):#
            try:
                self.assertTrue(answers[key] in question['choices'])
            except AssertionError:
                raise AssertionError('Question exists without an answer')


if __name__ == '__main__':
    unittest.main()
