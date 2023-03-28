import unittest
from format_chat import transform_lines

class TestTransformLines(unittest.TestCase):

    def test_header_processing(self):
        input_lines = [
            "# ChatGPT4 - Some description goes here - 16\n",
            "* **Date of conversation:** March 26, 2023\n",
            "* Analyze some ideas of famous people on current events.\n",
            "> **User1**\n",
            "Text text text text\n",
            "> **ChatGPT**\n",
            "Text text text.\n",
        ]
        expected_output = [
            "# ChatGPT4 - Some description goes here - 16\n",
            "* **Date of conversation:** March 26, 2023\n",
            "* Analyze some ideas of famous people on current events.\n",
            "> **User1**\n",
            ">\n",
            "> Text text text text\n",
            "\n",
            "> **ChatGPT**\n",
            ">\n",
            "> Text text text.\n",
        ]
        expected_output = "".join(expected_output)
        input_result = "".join(transform_lines(input_lines))
        self.assertEqual(input_result, expected_output)

    def test_correct_blockquote_format(self):
        input_lines = [
            "> **ChatGPT**\n",
            "Text text text.\n",
            "\n",
            "Text text text text\n",
            "\n",
            "Text text..\n",
        ]
        expected_output = [
            "> **ChatGPT**\n",
            ">\n",
            "> Text text text.\n",
            ">\n",
            "> Text text text text\n",
            ">\n",
            "> Text text..\n",
        ]
        expected_output = "".join(expected_output)
        input_result = "".join(transform_lines(input_lines))
        self.assertEqual(input_result, expected_output)

    def test_no_duplicate_chatgpt(self):
        input_lines = [
            "> **ChatGPT**\n",
            "Text1\n",
            "\n",
            "text2\n",
            "> **User**\n",
            "text3\n",
            "> **ChatGPT**\n",
        ]
        expected_output = [
            "> **ChatGPT**\n",
            ">\n",
            "> Text1\n",
            ">\n",
            "> text2\n",
            "\n",
            "> **User**\n",
            ">\n",
            "> text3\n",
            "\n",
            "> **ChatGPT**\n",
            ">\n",
        ]
        expected_output = "".join(expected_output)
        input_result = "".join(transform_lines(input_lines))
        self.assertEqual(input_result, expected_output)

if __name__ == '__main__':
    unittest.main()