import os

def get_files_info(working_directory: str, directory: str) -> str:
    if working_directory is None:
        return "Error: No working directory specified."
    if directory is None or directory == "":
        directory = "."

    relative_path_to_directory = os.path.join(working_directory, directory)
    abs_path_to_directory = os.path.abspath(relative_path_to_directory)

    if not abs_path_to_directory.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_path_to_directory):
        return f'Error: "{directory}" is not a directory'


    files_info = []
    for filename in os.listdir(abs_path_to_directory):
        try:
            path = os.path.join(abs_path_to_directory, filename)
            file_size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            files_info.append(f"- {filename}: {file_size=} bytes, {is_dir=}")
        except Exception as e:
            return "Error: there was an error while listing files. See more info: {e}"

    return "\n".join(files_info)