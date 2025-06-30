import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    '''Allows the AI Agent to read the contents of a file'''
    if working_directory is None or working_directory == "":
        return "Error: No working directory specified."
    if file_path is None or file_path == "":
        return "Error: Need a file path to get a file's content."
    
    relative_path_to_file = os.path.join(working_directory, file_path)
    abs_path_to_file = os.path.abspath(relative_path_to_file)

    if not abs_path_to_file.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_path_to_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_path_to_file) as f:
            content = f.read(MAX_CHARS)
            if f.read(1) != "":
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'

    return content