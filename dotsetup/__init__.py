"""
__init__.py

This module initializes the dotsetup package and provides a main function to check
for the latest version and display a message if a newer version is available.

"""

from dotsetup.parse import DotSetup
from dotsetup.exception import DotSetupException, FileNotFoundError, VariableNotFoundError, JSONDecodeError
from .version import current_version, latest_version, get_latest_release_version

def check_version():
    """
    Check for the latest version of dotsetup and display a message if a newer version is available.
    """
    if latest_version > current_version:
        print(f"A newer version ({latest_version}) of dotsetup is available. Consider upgrading.")

if __name__ == "__main__":
    # Call the check_version function when this script is executed directly
    check_version()
