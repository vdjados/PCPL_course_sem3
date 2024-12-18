import unittest

class TestProgramFunctions(unittest.TestCase):
    
    def setUp(self):
        self.languages, self.operators, self.many_to_many_operators, self.many_to_many_languages, self.operators_languages = create_examples()

    def test_get_languages_starting_with_J(self):
        expected_result = [
            {
                "language_name": "Java",
                "operators": [
                    {"symbol": "++", "description": "Increment (Unary)"},
                    {"symbol": "--", "description": "Decrement (Unary)"}
                ]
            },
            {
                "language_name": "JavaScript",
                "operators": [
                    {"symbol": "&&", "description": "Logical AND"},
                    {"symbol": "||", "description": "Logical OR"}
                ]
            }
        ]
        result = get_languages_starting_with_J(self.languages, self.operators)
        self.assertEqual(result, expected_result)

    def test_get_languages_with_max_operators(self):
        expected_result = [
            {"language_name": "Python", "operators_count": 4},
            {"language_name": "C++", "operators_count": 3},
            {"language_name": "Java", "operators_count": 2},
            {"language_name": "JavaScript", "operators_count": 2}
        ]
        result = get_languages_with_max_operators(self.languages, self.operators)
        self.assertEqual(result, expected_result)

    def test_get_operators_by_language(self):
        expected_result = [
            {
                "language_name": "C++",
                "operators": [
                    {"symbol": "+", "description": "Addition"},
                    {"symbol": "!", "description": "Logical NOT (Unary)"},
                    {"symbol": "~", "description": "Bitwise NOT (Unary)"}
                ]
            },
            {
                "language_name": "Java",
                "operators": [
                    {"symbol": "++", "description": "Increment (Unary)"},
                    {"symbol": "--", "description": "Decrement (Unary)"}
                ]
            },
            {
                "language_name": "JavaScript",
                "operators": [
                    {"symbol": "&&", "description": "Logical AND"},
                    {"symbol": "||", "description": "Logical OR"}
                ]
            },
            {
                "language_name": "Python",
                "operators": [
                    {"symbol": "+", "description": "Addition"},
                    {"symbol": "-", "description": "Subtraction"},
                    {"symbol": "*", "description": "Multiplication"},
                    {"symbol": "/", "description": "Division"}
                ]
            }
        ]
        result = get_operators_by_language(self.many_to_many_languages, self.many_to_many_operators, self.operators_languages)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
