import ast
import os
import json
import configparser
import warnings

from dotsetup.exception import JSONDecodeError, VariableNotFoundError


class DotSetup:
    """A class for loading configuration variables from different file types."""

    def __init__(self):
        """Initialize an instance of the DotSetup class."""
        pass

    def load(self, variable_name, file_type='env', file_path=None):
        """
        Load a configuration variable from a file.

        Args:
            variable_name (str): The name of the variable to load.
            file_type (str): The type of file to load from ('env', 'json', 'ini', 'custom').
            file_path (str): The path to the file. If None, the default path will be used.

        Returns:
            The value of the configuration variable.

        Raises:
            ValueError: If an invalid file type is provided.
            DotSetupException: If there is an issue loading the variable.
        """
        if file_type not in ['env', 'json', 'ini', 'custom']:
            raise ValueError("Invalid file type. Supported types are 'env', 'json', 'ini', and 'custom'.")

        if file_path is None:
            file_path = self._default_file_path(file_type)

        if file_type == 'env':
            value = self._load_from_env(variable_name, file_path)
        elif file_type == 'json':
            value = self._load_from_json(variable_name, file_path)
        elif file_type == 'ini':
            value = self._load_from_ini(variable_name, file_path)
        elif file_type == 'custom':
            value = self._load_from_custom(variable_name, file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

        return value

    def _default_file_path(self, file_type):
        """Get the default file path based on the file type."""
        if file_type == 'env':
            return self._find_env_file()
        elif file_type == 'json':
            return 'config.json'
        elif file_type == 'ini':
            return 'config.ini'
        elif file_type == 'custom':
            return 'config.con'

    def _find_env_file(self):
        """Find the appropriate .env file from a list of possible names."""
        possible_names = ['.env', 'config.env']
        for name in possible_names:
            if os.path.exists(name):
                return name
        return '.env'  # Fallback to default

    def _load_from_env(self, variable_name, file_path):
        """
        Load a variable from an environment file.

        Args:
            variable_name (str): The name of the variable to load.
            file_path (str): The path to the environment file.

        Returns:
            The value of the variable.

        Raises:
            VariableNotFoundError: If the variable is not found.
            FileNotFoundError: If the environment file is not found.
        """
        if os.path.exists(file_path):
            with open(file_path, 'r') as env_file:
                for line in env_file:
                    key, value = line.strip().split('=')
                    if key == variable_name:
                        return value
                raise VariableNotFoundError(variable_name, file_path)
        else:
            raise FileNotFoundError("env", file_path)

    def _load_from_json(self, variable_name, file_path):
        """
        Load a variable from a JSON file.

        Args:
            variable_name (str): The name of the variable to load.
            file_path (str): The path to the JSON file.

        Returns:
            The value of the variable.

        Raises:
            VariableNotFoundError: If the variable is not found.
            FileNotFoundError: If the JSON file is not found.
            JSONDecodeError: If there is an error decoding JSON.
        """
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    nested_keys = variable_name.split('.')
                    for key in nested_keys:
                        if isinstance(data, dict):
                            data = data.get(key, {})
                        else:
                            raise VariableNotFoundError(variable_name, file_path)
                    return data
            else:
                raise FileNotFoundError("JSON", file_path)
        except json.decoder.JSONDecodeError:
            raise JSONDecodeError(file_path)

    def _load_from_ini(self, variable_name, file_path):
        """
        Load a variable from an INI file.

        Args:
            variable_name (str): The name of the variable to load.
            file_path (str): The path to the INI file.

        Returns:
            The value of the variable.

        Raises:
            VariableNotFoundError: If the variable is not found.
            FileNotFoundError: If the INI file is not found.
        """
        if os.path.exists(file_path):
            config = configparser.ConfigParser()
            config.read(file_path)
            sections = variable_name.split('.')
            if sections[0] in config:
                value = config[sections[0]]
                for key in sections[1:]:
                    value = value.get(key, {})
                if value:
                    return value
                else:
                    raise VariableNotFoundError(variable_name, file_path)
            else:
                raise VariableNotFoundError(variable_name, file_path)
        else:
            raise FileNotFoundError("INI", file_path)

    def _load_from_custom(self, variable_name, file_path):
        """
        Load a variable from a custom file.

        Args:
            variable_name (str): The name of the variable to load.
            file_path (str): The path to the custom file.

        Returns:
            The value of the variable or None if not found.

        Raises:
            FileNotFoundError: If the custom file is not found.
            VariableNotFoundError: If the variable is not found in the custom file.
        """
        if os.path.exists(file_path):
            with open(file_path, 'r') as custom_file:
                data = custom_file.readlines()
                try:
                    parsed_data = self._parse_custom_format(data)
                except (SyntaxError, ValueError) as e:
                    raise JSONDecodeError(file_path) from e
                nested_keys = variable_name.split('.')
                for key in nested_keys:
                    if key in parsed_data:
                        parsed_data = parsed_data[key]
                    else:
                        warnings.warn(f"Variable '{variable_name}' not found in the custom file.")
                        return None
                return parsed_data
        else:
            raise FileNotFoundError("Custom", file_path)

    def _parse_custom_format(self, lines):
        """
        Parse the custom file content.

        Args:
            lines (list): List of lines from the custom file.

        Returns:
            Parsed data based on your specific custom format.
        """
        parsed_data = {}
        current_dict = parsed_data  # Track the current dictionary

        for line in lines:
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue

            # Check if the line contains an equal sign
            if '=' in line:
                # Split the line into key and value
                key, value = line.split('=', 1)

                # Check if the key already exists in the dictionary
                if key in current_dict:
                    # If yes, convert the value to a list and append the new value
                    existing_value = current_dict[key]
                    if not isinstance(existing_value, list):
                        existing_value = [existing_value]
                    existing_value.append(self._parse_single_value(value))
                    current_dict[key] = existing_value
                else:
                    current_dict[key] = self._parse_single_value(value)
            elif line.startswith("{") and line.endswith("}"):
                # Handle nested dictionaries
                nested_dict = self._parse_nested_values(line)
                current_dict.update(nested_dict)
            else:
                # Handle cases where there is no equal sign
                current_dict[line] = None

        return parsed_data

    def _parse_nested_values(self, value):
        """
        Parse nested values enclosed in curly braces.

        Args:
            value (str): String containing nested values.

        Returns:
            Parsed nested values.
        """
        # Remove curly braces and split values
        values = value[1:-1].split(',')

        # Parse each value in the list
        parsed_values = [self._parse_single_value(v.strip()) for v in values]

        return parsed_values

    def _parse_single_value(self, value):
        """
        Parse a single value.

        Args:
            value (str): String containing a single value.

        Returns:
            Parsed value with the same data type.
        """
        try:
            # Try to evaluate the value using ast.literal_eval
            parsed_value = ast.literal_eval(value)

            # Check if the parsed value is a dictionary
            if isinstance(parsed_value, dict):
                return parsed_value
            else:
                return value
        except (ValueError, SyntaxError):
            # If literal_eval fails, return the value as a string
            return value
