import os

def git_init():
    os.system("git init")

def git_add():
    os.system("git add .")

def git_remote_add(url):
    os.system(f"git remote add origin {url}")

def git_pull_allow_unrelated():
    os.system("git pull origin main --allow-unrelated-histories")

def git_push():
    os.system("git push origin main")

if __name__ == "__main__":
    # User input for the repository URL
    url = input("Enter theaaaa repository URL: ")

    # Perform git commands
    git_init()
    git_add()
    git_remote_add(url)
    git_pull_allow_unrelated()
    git_push()
