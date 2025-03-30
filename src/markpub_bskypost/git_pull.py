#!/usr/bin/env python3
import subprocess
import os

def git_pull():
    try:
        result = subprocess.run(["git", "pull"], capture_output=True, text=True, check=True)
        print(result.stdout)
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return 1

def main():
    repo_name = 'technosocial-praxis'
    if not repo_name in os.getcwd():
        print("Do not forget to `git pull` in the local repository directory.")
        return -1

    git_pull()

if __name__ == "__main__":
    exit(main())

