import os
import random
import subprocess
from datetime import datetime, timedelta

# Repository Path
repo_path = os.getcwd()  # Assumes you're running the script inside the repo

# Number of commits
num_commits = 500  # Adjust as needed
start_date = datetime(2010, 1, 1)
end_date = datetime(2025, 12, 31)

# Function to run shell commands
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()

# Ensure it's a Git repository
if not os.path.exists(os.path.join(repo_path, ".git")):
    print("Initializing Git repository...")
    run_command("git init")
    run_command('git config user.name "Yashwanth Pandi"')
    run_command('git config user.email "pandiyashwanth@gmail.com"')

# Generate commits
for _ in range(num_commits):
    random_days = random.randint(0, (end_date - start_date).days)
    commit_date = start_date + timedelta(days=random_days)
    formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Modify a dummy file
    with open("contribution.txt", "a") as f:
        f.write(f"Commit on {formatted_date}\n")
    
    # Set commit date
    env = {
        "GIT_COMMITTER_DATE": formatted_date,
        "GIT_AUTHOR_DATE": formatted_date,
    }
    
    # Add, commit, and push
    run_command("git add .")
    run_command(f'git commit --date="{formatted_date}" -m "Commit on {formatted_date}"')
    
print("All commits created successfully!")

# Push to GitHub
print("Pushing commits to GitHub...")
run_command("git branch -M main")
run_command("git remote add origin git@github.com:YashwanthPandi/Cloud-Security-Risk-Management-Framework.git")
run_command("git push -u origin main --force")

print("Done! Check your GitHub contributions graph in a few minutes.")
