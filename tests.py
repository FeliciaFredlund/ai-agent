# Test AI Agent functions

import unittest
from functions.get_files_info import get_files_info

class TestFunctions(unittest.TestCase):
    def test_get_files_info(self):
        print("Testing get_files_info()")
        print("========================")
        not_directory = get_files_info("calculator", "main.py")
        print("main.py (not a directory)")
        print(not_directory)
        self.assertIn("Error:", not_directory)
        self.assertIn(" is not a directory", not_directory)

        slash_bin = get_files_info("calculator", "/bin")
        print("/bin (outside working directory)")
        print(slash_bin)
        self.assertIn("Error:", slash_bin)
        self.assertNotIn("ls", slash_bin)

        parent_folder = get_files_info("calculator", "../")
        print("../ (parent folder outside working directory)")
        print(parent_folder)
        self.assertIn("Error: Cannot list", parent_folder)
        self.assertNotIn("requirements.txt", parent_folder)
        
        current_folder = get_files_info("calculator", ".")
        print(". (current folder aka working directory)")
        print(current_folder)
        self.assertIn("pkg", current_folder)
        self.assertIn("is_dir=True", current_folder)
        self.assertIn("main.py" in current_folder)
        self.assertIn("is_dir=False", current_folder)
        self.assertNotIn("render.py" in current_folder)
        
        pkg = get_files_info("calculator", "pkg")
        print("pkg (directory in working directory)")
        print(pkg)
        self.assertIn("calculator.py", pkg)
        self.assertIn("is_dir=False", pkg)
        self.assertIn("render.py", pkg)
        print("========================")


if __name__ == "__main__":
    unittest.main()