import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list = None) -> str:
    '''Allows the AI Agent to run a Python file'''
    if working_directory is None or working_directory == "":
        return "Error: No working directory specified."
    if file_path is None or file_path == "":
        return "Error: Need a file path."
    
    relative_path_to_file = os.path.join(working_directory, file_path)
    abs_path_to_file = os.path.abspath(relative_path_to_file)

    if not abs_path_to_file.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'    
    if not os.path.exists(abs_path_to_file):
        return f'Error: File "{file_path}" not found.'
    if not abs_path_to_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        commands = ["python3", abs_path_to_file]
        if args:
            commands.extend(args)

        completed_process = subprocess.run(
            commands,
            timeout = 30,
            capture_output = True,
            text = True,
            cwd = os.path.abspath(working_directory)
        )

        output = []
        if completed_process.stdout:
            output.append(f"STDOUT:\n{completed_process.stdout}")
        if completed_process.stderr:
            output.append(f"STDERR:\n{completed_process.stderr}")
        if completed_process.returncode != 0:
            output.append(f"\nProcess exited with code {completed_process.returncode}")
        
        if len(output) == 0:
            output.append("No output produced.")

        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"