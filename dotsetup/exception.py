# exception.py

class DotSetupException(Exception):
    """Base exception for DotSetup-related errors."""
    pass


class FileNotFoundError(DotSetupException):
    """Exception raised when a file is not found."""

    def __init__(self, file_type, file_path):
        self.file_type = file_type
        self.file_path = file_path
        super().__init__(f"{file_type} file not found. Please make sure the file exists at {file_path}.")


class VariableNotFoundError(DotSetupException):
    """Exception raised when a variable is not found in a file."""

    def __init__(self, variable_name, file_path):
        self.variable_name = variable_name
        self.file_path = file_path
        super().__init__(f"Variable '{variable_name}' not found in {file_path}.")


class JSONDecodeError(DotSetupException):
    """Exception raised when there is an error decoding JSON."""

    def __init__(self, file_path):
        self.file_path = file_path
        super().__init__(f"Error decoding JSON in {file_path}. Please ensure the file is properly formatted.")
