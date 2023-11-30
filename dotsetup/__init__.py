import json
import os
import warnings

class DotSetupParser:
    def __init__(self, file_path):
        self.file_extension = file_path.split('.')[-1].lower()
        self.data = self.parse(file_path)

    def parse(self, file_path):
        if self.file_extension == 'env':
            return self.parse_env(file_path)
        elif self.file_extension == 'ini':
            return self.parse_ini(file_path)
        elif self.file_extension == 'json':
            return self.parse_json(file_path)
        else:
            raise ValueError(f"Unsupported file type: {self.file_extension}")

    def parse_env(self, file_path):
        result = {}
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if '=' in line:
                    key, value = map(str.strip, line.split('=', 1))
                    result[key] = value
        return result

    def parse_ini(self, file_path):
        result = {}
        with open(file_path, 'r') as file:
            current_section = None
            for line in file:
                line = line.strip()
                if line.startswith('[') and line.endswith(']'):
                    current_section = line[1:-1]
                    result[current_section] = {}
                elif '=' in line and current_section is not None:
                    key, value = map(str.strip, line.split('=', 1))
                    result[current_section][key] = value
        return result

    def parse_json(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

class DotSetup:
    def __init__(self):
        self.project_root = os.getcwd()
        self.config_data = self.load_files()

    def load_files(self):
        config_data = {}
        self.load_file(config_data, 'env', ".env")
        self.load_file(config_data, 'ini', "config.ini")
        self.load_file(config_data, 'json', "config.json")
        return config_data

    def load_file(self, config_data, file_type, file_name):
        file_path = os.path.join(self.project_root, file_name)
        if os.path.isfile(file_path):
            config_data[file_type] = DotSetupParser(file_path)

    def load(self, key, file_type='env'):
        key_upper = key.upper()
        if file_type in self.config_data and key_upper in self.config_data[file_type].data:
            return self.config_data[file_type].data[key_upper]
        return None

# Example usage:
ds = DotSetup()
value_env = ds.load('version', file_type='env')
print(value_env)
