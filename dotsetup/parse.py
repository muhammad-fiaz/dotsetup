# parse.py
import os
import json
import configparser
from dotsetup.exception import DotSetupException, FileNotFoundError, VariableNotFoundError, JSONDecodeError


class DotSetup:
    """A class for loading configuration variables from different file types."""

    def __init__(self):
        pass

    def load(self, variable_name, file_type='env', file_path=None):
        """
        Load a configuration variable from a file.

        Args:
            variable_name (str): The name of the variable to load.
            file_type (str): The type of file to load from ('env', 'json', 'ini').
            file_path (str): The path to the file. If None, the default path will be used.

        Returns:
            The value of the configuration variable.

        Raises:
            ValueError: If an invalid file type is provided.
            DotSetupException: If there is an issue loading the variable.
        """
        if file_type not in ['env', 'json', 'ini']:
            raise ValueError("Invalid file type. Supported types are 'env', 'json', and 'ini'.")

        if file_path is None:
            file_path = self._default_file_path(file_type)

        if file_type == 'env':
            value = self._load_from_env(variable_name, file_path)
        elif file_type == 'json':
            value = self._load_from_json(variable_name, file_path)
        elif file_type == 'ini':
            value = self._load_from_ini(variable_name, file_path)

        return value

    def _default_file_path(self, file_type):
        """Get the default file path based on the file type."""
        if file_type == 'env':
            return self._find_env_file()
        elif file_type == 'json':
            return 'config.json'
        elif file_type == 'ini':
            return 'config.ini'

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
