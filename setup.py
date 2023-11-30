from setuptools import setup, find_packages
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get the version from the environment variable
version = os.getenv("VERSION")

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name='runix',
    version=version,
    description='A high-level Python web framework for web development.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='contactus@fiaz.dev',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'runix = runix.cli:create',
        ],
    },
    install_requires=[
        'click',
        # Add other dependencies here
    ],
)
