import os
import subprocess
from google.genai import types

schema_run_python_files = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file, located in the working directory, and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file being executed, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional arguments to pass to the Python file.",
                items=types.Schema(
                    type=types.Type.STRING,
                    description='Optional argument to pass to the Python file, such as "5 + 8" or "10 - 5 * (3 + 2)".'
                )
            )
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory: str, file_path: str, args: list = None) -> str:
    '''Allows the AI Agent to execute a Python file'''
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