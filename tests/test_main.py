import unittest
from main import parse_todo

class Tests(unittest.TestCase):
    def test_aliases_and_comments(self):
        report = parse_todo("# comment\np abcdef1 first\ns abcdef2 second\n")
        self.assertTrue(report["valid"])
        self.assertEqual([x["action"] for x in report["entries"]], ["pick", "squash"])
    def test_invalid_hash(self):
        report = parse_todo("pick nope message\n")
        self.assertFalse(report["valid"])
        self.assertIn("hexadecimal", report["errors"][0])
    def test_squash_without_parent_warns(self):
        report = parse_todo("squash abcdef1 first\n")
        self.assertEqual(len(report["warnings"]), 1)
    def test_exec_requires_command(self):
        self.assertFalse(parse_todo("exec\n")["valid"])

if __name__ == "__main__":
    unittest.main()
