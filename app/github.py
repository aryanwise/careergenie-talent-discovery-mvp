import requests
import os
from dotenv import load_dotenv
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def search_users(query, per_page=10):
    url = "https://api.github.com/search/users"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    params = {"q": query, "per_page": per_page}
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Stops execution if there's an error (4xx or 5xx)
    return response.json().get("items", [])

def get_user_details(username):
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    return requests.get(url, headers=headers).json()


def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    return requests.get(url, headers=headers).json()


# testing 
if __name__ == "__main__":
    # Test 1: Verify Token Loading
    if not GITHUB_TOKEN:
        print("❌ Error: GITHUB_TOKEN not found. Check your .env file.")
    else:
        print("✅ Token loaded successfully.")

        try:
            # Test 2: Search Users
            print("Testing search_users...")
            users = search_users("octocat", per_page=1)
            username = users[0]['login']
            print(f"✅ Search successful. Found: {username}")

            # Test 3: Get Details
            print(f"Testing get_user_details for {username}...")
            details = get_user_details(username)
            print(f"✅ Details retrieved. Name: {details.get('name')}")

            # Test 4: Get Repos
            print(f"Testing get_user_repos for {username}...")
            repos = get_user_repos(username)
            print(f"✅ Repos retrieved. Count: {len(repos)}")

        except Exception as e:
            print(f"❌ An error occurred: {e}")