# DotSetup
[![PyPI Version](https://img.shields.io/pypi/v/dotsetup)](https://pypi.org/project/dotsetup/)
[![Python Versions](https://img.shields.io/pypi/pyversions/dotsetup)](https://pypi.org/project/dotsetup/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/pypi/dm/dotsetup)](https://pypi.org/project/dotsetup/)
[![Last Commit](https://img.shields.io/github/last-commit/muhammad-fiaz/dotsetup)](https://github.com/muhammad-fiaz/dotsetup)
[![GitHub Issues](https://img.shields.io/github/issues/muhammad-fiaz/dotsetup)](https://github.com/muhammad-fiaz/dotsetup/issues)
[![GitHub Stars](https://img.shields.io/github/stars/muhammad-fiaz/dotsetup)](https://github.com/muhammad-fiaz/dotsetup/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/muhammad-fiaz/dotsetup)](https://github.com/muhammad-fiaz/dotsetup/network)

**DotSetup** is a Python package designed for flexible configuration management, supporting `.ini`, `.json`, `.env`, and custom file types. Simplify the storage and retrieval of settings in your projects effortlessly.

## Table of Contents
1. [DotSetup](#dotsetup)
2. [Features](#features)
3. [Installation](#installation)
4. [Getting Started](#getting-started)
    - [Simple Example](#simple-example)
    - [Breaking down Example](#breaking-down-example)
    - [Custom Path for File Types](#custom-path-for-file-types)
    - [Nested Configurations](#nested-configurations)
5. [Custom File Syntax](#custom-file-syntax)
6. [Contributing](#contributing)
7. [Code of Conduct](#code-of-conduct)
8. [License](#license)
9. [Support the Project](#support-the-project)


## Features

- **Multi-format Support:** Seamlessly handle configurations from files like `.ini`, `.json`, `.env`, and custom file types.
- **Intuitive API:** Easy-to-use methods for 🔄 loading, accessing, and saving configurations.
- **File Type Extension:** Customize DotSetup to support additional file types beyond the included formats.
- **Nested Configurations:** Load nested configurations from files like `.ini` and `.json` files.
- **Custom File Syntax:** Define your own syntax for custom file types.
- **Custom File Path:** Load configurations from a custom path for different file types.
- **Error Handling:** Handle errors that may occur when loading configurations.
- **Lightweight:** DotSetup is a lightweight package with no external dependencies.
- **Cross-Platform:** DotSetup is compatible with Windows, macOS, and Linux.
- **Open-Source:** DotSetup is an open-source project licensed under the MIT License.


## Installation

```bash
pip install dotsetup
```

## Getting Started
To get started with DotSetup, follow these steps:

Import the DotSetup class in your Python script or project to get started.

## **Simple Example**:
```python
from dotsetup import DotSetup

# Initialize DotSetup
ds = DotSetup()

# Load from env file
value_env = ds.load('version', file_type='env')
print(f"Value from JSON File: {value_env}")
    
```
the above example loads the value of the variable `version` from the `.env` file in the root folder of the project.

## **Breaking down Example:**
```python
from dotsetup import DotSetup, DotSetupException, FileNotFoundError, VariableNotFoundError, JSONDecodeError

def main():
    # Initialize DotSetup
    ds = DotSetup()

    try:
        # Load from JSON file
        value_json = ds.load('database', file_type='json')
        print(f"Value from JSON File: {value_json}")
    except (FileNotFoundError, VariableNotFoundError, JSONDecodeError) as e:
        print(f"Error: {e}")

    try:
        # Load from ENV file with default path
        value_env = ds.load('DATABASE_URL', file_type='env')
        print(f"Value from ENV (default path): {value_env}")
    except (FileNotFoundError, VariableNotFoundError) as e:
        print(f"Error: {e}")

    try:
        # Load from custom file
        value_custom = ds.load('num2', file_type='custom', file_path='config.con')
        print(f"Value from Custom File: {value_custom}")
    except (FileNotFoundError, VariableNotFoundError, JSONDecodeError) as e:
        print(f"Error: {e}")

    try:
        # Load from INI file
        value_ini = ds.load('section1.option1', file_type='ini')
        print(f"Value from INI File: {value_ini}")
    except (FileNotFoundError, VariableNotFoundError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
here you can also see how to handle errors that may occur when loading configurations.
## Custom Path for File Types
To load configurations from a custom path for different file types:
    
```python  
from dotsetup import DotSetup
ds = DotSetup()

# Load configuration from the specified custom path
value = ds.load('key_name', file_type='type', file_path='path/to/config.con')

```
The default path for the env file is `.env` in the root folder. The default path for the ini file is `config.ini` in the root folder, and the default path for the json file is `config.json` in the root folder. For the custom file, the default path is `config.con` in the root folder. Alternatively, you can specify your own path using the file_path parameter

## Nested Configurations
you can also load the nested configuration from the json and ini files by using the dot notation for example

**json Example:**
```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "username": "user",
    "password": "password"
  },
  "api_key": "your_api_key"
}

```
```python
from dotsetup import DotSetup
ds = DotSetup()
# Load value from nested JSON file
value_json = ds.load('database.host', file_type='json', file_path='config.json')
print(f"Value from JSON File: {value_json}")
```

## Custom File Syntax
DotSetup supports custom file types. To use a custom file type, you must define a custom file syntax. The custom file syntax is a dictionary that maps variable names to their values. 

```
USERNAME="johndoe"
PASSWORD="mysecretpassword"
API_KEY="abc123"
NUMBER=1
Numbers={1,2,3,4,5}
num2=(1,2)
num3=[1,2,3]
num4=1.2
str="Hello World"
str2=("Hello World","Hello World")
str3=["Hello World","Hello World"]
LINKS=["https://www.google.com","https://www.facebook.com","https://www.twitter.com"]
LINKS2={"KEY":"https://www.google.com","KEY2":"https://www.facebook.com"}
```
In this example, variables and values are defined using the format key=value. You can define your own syntax for custom files with custom file extension(**filename.custom_extension**) based on your project's requirements. Make sure to follow this syntax when defining your custom file syntax.

## Contributing
Contributions are welcome! Before contributing, please read our Contributing Guidelines to ensure a smooth and collaborative development process.

## Code of Conduct

Please review our Code of Conduct to understand the standards of behavior we expect from contributors and users of this project.

## License
This project is licensed under the [MIT License](). See [LICENSE](LICENSE) for more details.

## Support the Project
<br>
<div align="center">

  <h5> <strong> 💰 You can help me improve more by a little support </strong></h5>
  

[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/muhammadfiaz) [![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://patreon.com/muhammadfiaz) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/muhammadfiaz)
[![Sponsor muhammad-fiaz](https://img.shields.io/badge/Sponsor-%231EAEDB.svg?&style=for-the-badge&logo=GitHub-Sponsors&logoColor=white)](https://github.com/sponsors/muhammad-fiaz)
</div>


## Happy Coding ❤️

