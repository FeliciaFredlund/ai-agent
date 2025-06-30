# Test AI Agent functions

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file_content import write_file
from config import MAX_CHARS

class TestFunctions(unittest.TestCase):
    def test_get_files_info(self):
        print("\n\nTesting get_files_info()")
        print("========================")
        
        slash_bin = get_files_info("calculator", "/bin")
        print("/bin (outside working directory)")
        print(slash_bin)
        self.assertIn('Error: Cannot list "/bin"', slash_bin)
        self.assertNotIn("pstree", slash_bin)
        print("========================")
        
        not_directory = get_files_info("calculator", "main.py")
        print("main.py (not a directory)")
        print(not_directory)
        self.assertEqual('Error: "main.py" is not a directory', not_directory)
        print("========================")

        parent_folder = get_files_info("calculator", "../")
        print("../ (parent folder outside working directory)")
        print(parent_folder)
        self.assertIn('Error: Cannot list "../" as', parent_folder)
        self.assertNotIn("requirements.txt", parent_folder)
        print("========================")
        
        current_folder = get_files_info("calculator", ".")
        print(". (current folder aka working directory)")
        print(current_folder)
        self.assertIn("pkg", current_folder)
        self.assertIn("is_dir=True", current_folder)
        self.assertIn("main.py", current_folder)
        self.assertIn("is_dir=False", current_folder)
        self.assertNotIn("render.py", current_folder)
        print("========================")
        
        pkg = get_files_info("calculator", "pkg")
        print("pkg (directory in working directory)")
        print(pkg)
        self.assertIn("calculator.py", pkg)
        self.assertIn("is_dir=False", pkg)
        self.assertIn("render.py", pkg)
        print("========================")


    def test_get_file_content(self):
        print("\n\nTesting get_file_content()")
        print("========================")

        slash_bin_slash_cat = get_file_content("calculator", "/bin/cat")
        print("/bin/cat")
        print(slash_bin_slash_cat)
        self.assertEqual(slash_bin_slash_cat, 'Error: Cannot read "/bin/cat" as it is outside the permitted working directory')
        print("========================")

        not_file = get_file_content("calculator", "pkg")
        print("pkg - not a file")
        print(not_file)
        self.assertEqual(not_file, 'Error: File not found or is not a regular file: "pkg"')
        print("========================")

        lorem = get_file_content("calculator", "lorem.txt")
        print("lorem.txt")
        print(lorem[:50], "[...]", lorem[-55:])
        self.assertTrue(lorem.startswith("Lorem ipsum dolor sit amet,"))
        self.assertTrue(lorem.endswith(f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]'))
        self.assertTrue(len(lorem) < MAX_CHARS + 60)
        print("========================")

        main = get_file_content("calculator", "main.py")
        print("main.py")
        print(main[:50], "[...]", main[-55:])
        self.assertIn("def main()", main)
        self.assertIn("calculator = Calculator()", main)
        self.assertNotIn('print("AI Code Agent")', main)
        print("========================")

        calculator = get_file_content("calculator", "pkg/calculator.py")
        print("pkg/calculator.py")
        print(calculator[:50], "[...]", calculator[-55:])
        self.assertIn("def _apply_operator(self, operators, values)", calculator)
        self.assertIn("class Calculator:", calculator)
        self.assertNotIn('def render:', calculator)
        print("========================")
        

    def test_write_file(self):
        print("\n\nTesting write_file()")
        print("========================")

        not_writable = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print("/tmp/temp.txt")
        print(not_writable)
        self.assertEqual(not_writable, f'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory')
        print("========================")

        not_a_file = write_file("calculator", "pkg", "this shouldn't work")
        print("pkg/")
        print(not_a_file)
        self.assertEqual(not_a_file, 'Error: pkg is not a file.')
        print("========================")

        lorem2 = write_file("calculator", "lorem2.txt", "wait, this isn't lorem ipsum")
        print("lorem2.txt")
        print(lorem2)
        self.assertEqual(lorem2, 'Successfully wrote to "lorem2.txt" (28 characters written)')
        print("========================")

        morelorem = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print("pkg/morelorem.txt")
        print(morelorem)
        self.assertEqual(morelorem, 'Successfully wrote to "pkg/morelorem.txt" (26 characters written)')
        print("========================")


if __name__ == "__main__":
    unittest.main()