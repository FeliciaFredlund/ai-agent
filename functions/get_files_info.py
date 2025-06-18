def get_files_info(working_directory, directory = None):
    files_info = ""
    # if directory is outside working_directory.
    # return this string
    # f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # if directory is not a directory
    # return this string
    # f'Error: "{directory}" is not a directory'

    # If any errors are raised by the standard library functions,
    # catch them and instead return a string describing the error.
    # Always prefix error strings with "Error:".

    # Format for the string if no errors occured:
    # - README.md: file_size=1032 bytes, is_dir=False
    # - src: file_size=128 bytes, is_dir=True
    # - package.json: file_size=1234 bytes, is_dir=False
    return files_info