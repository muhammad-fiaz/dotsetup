
from setuptools import setup, find_packages
from dotsetup.version import get_Version


version = "0.0.2"
get_Version(version)


with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name='dotsetup',
    version=version,
    description='A simple setup tool for Python projects to manage environment variables and configurations ands '
                'settings.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Muhammad Fiaz',
    author_email='fiazatbusiness@gmail.com',
    url='https://github.com/muhammad-fiaz/dotsetup',
    license='MIT',
    packages=find_packages(),
    entry_points={},
    install_requires=[


    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='configuration management environment variables setup tool',
    project_urls={
        'Source': 'https://github.com/muhammad-fiaz/dotsetup',
        'Bug Reports': 'https://github.com/muhammad-fiaz/dotsetup/issues',
        'Buy me a Coffee!': 'https://buymeacoffee.com/muhammadfiaz',
        'Patreon': 'https://patreon.com/muhammadfiaz',
        'Ko-fi': 'https://ko-fi.com/muhammadfiaz',
        'GitHub Sponsors': 'https://github.com/sponsors/muhammad-fiaz',
        'Open Collective': 'https://opencollective.com/muhammadfiaz',
    },
)
