############################################### TEST UNIT #################################################################
from dotsetup import DotSetup
from dotsetup import DotSetupException, FileNotFoundError, VariableNotFoundError, JSONDecodeError


# main.py

from dotsetup import DotSetup, DotSetupException, FileNotFoundError, VariableNotFoundError, JSONDecodeError

# Your code here
ds = DotSetup()

value_env_custom = ds.load('VERSION', file_type='env')
print(f"Value from ENV (custom path): {value_env_custom}")
# Load from custom file
value_custom = ds.load('Numbers', file_type='custom', file_path="config.con")
print(f"Value from Custom File: {value_custom}")
# example.py





