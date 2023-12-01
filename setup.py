from setuptools import setup, find_packages

version = "0.0.0"


with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(

    name='dotsetup',
    version=version,
    description='A simple setup tool for Python projects to manage environment variables and configuration files.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Muhammad Fiaz',
    author_email='contact@muhammadfiaz.com',
    packages=find_packages(),
    entry_points={

    },
    install_requires=[

        # Add other dependencies here
    ],
)
