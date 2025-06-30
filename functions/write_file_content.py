import os
from google.genai import types

schema_write_file_content = types.FunctionDeclaration(
    name="write_file_content",
    description="Writes content to a file, located in the working directory, and returns the number of characters written. If the file already exists, it will be overwritten. Creates the file and directories if they don't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file being written to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be written to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)

def write_file_content(working_directory: str, file_path: str, content: str) -> str:
    '''Allows the AI Agent to write to files'''
    if file_path is None or file_path == "":
        return "Error: Need a file path to write to a file's content."
    
    relative_path_to_file = os.path.join(working_directory, file_path)
    abs_path_to_file = os.path.abspath(relative_path_to_file)

    if not abs_path_to_file.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if os.path.exists(abs_path_to_file):
            if not os.path.isfile(abs_path_to_file):
                return f'Error: {file_path} is not a file.'
        else:
            directories = os.path.dirname(abs_path_to_file)
            if not os.path.exists(directories):
                os.makedirs(directories)
                
        with open(abs_path_to_file, 'w') as f:
            f.write(content)
    except Exception as e:
        return f'Error writing file "{file_path}": {e}'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'