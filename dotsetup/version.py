import urllib.request
import json

def get_latest_release_version(repo_owner: str, repo_name: str) -> str:
    """
    Retrieve the latest release version of a GitHub repository.

    Parameters:
    - repo_owner (str): The username or organization name on GitHub.
    - repo_name (str): The name of the repository on GitHub.

    Returns:
    - str: The latest release version or '0.0.0' if unable to fetch.
    """
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'
    with urllib.request.urlopen(url) as response:
        if response.getcode() == 200:
            release_info = json.loads(response.read())
            return release_info.get('tag_name', '0.0.0')
        else:
            return '0.0.0'

# Replace 'muhammad-fiaz' and 'dotsetup' with your GitHub username and repository name
repo_owner = 'muhammad-fiaz'
repo_name = 'dotsetup'
current_version = "0.0.1"
latest_version = get_latest_release_version(repo_owner, repo_name)
