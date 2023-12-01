############################################### TEST UNIT #################################################################
'''
from dotsetup import DotSetup, DotSetupException, FileNotFoundError, VariableNotFoundError, JSONDecodeError

def main():
    # Initialize DotSetup
    ds = DotSetup()

    try:
        # Load from JSON file
        value_json = ds.load('database.host', file_type='json', file_path='config.json')
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
        value_ini = ds.load('section1.option1', file_type='ini', file_path='config.ini')
        print(f"Value from INI File: {value_ini}")
    except (FileNotFoundError, VariableNotFoundError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

'''