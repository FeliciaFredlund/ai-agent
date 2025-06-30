import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    '''Allows the AI Agent to write to files'''
    if working_directory is None or working_directory == "":
        return "Error: No working directory specified."
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