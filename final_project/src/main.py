import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://jsonplaceholder.typicode.com"

def describe_status(status_code):
    messages = {
        200: "Success: request completed.",
        201: "Created: resource created.",
        400: "Bad request: check the request data.",
        401: "Unauthorized: valid authentication is required.",
        403: "Forbidden: access is not permitted.",
        404: "Resource not found.",
        429: "Rate limit exceeded: too many requests.",
        500: "Internal server error.",
        502: "Bad gateway.",
        503: "Service unavailable.",
    }
    return messages.get(status_code, f"HTTP response: {status_code}")

def get_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    try:
        response = requests.get(url, timeout=10)
        print(f"Status: {response.status_code}")
        if response.status_code == 404:
            print("Request failed.")
            print("Status Code: 404")
            print("Resource not found.")
            return None
        if response.status_code == 429:
            print("Rate limit exceeded. Wait before retrying.")
            return None
        if not response.ok:
            print(describe_status(response.status_code))
            return None

        post = response.json()
        print(f"Post ID: {post.get('id')}")
        print(f"Title: {post.get('title')}")
        print(f"Body: {post.get('body')}")
        return post
    except requests.Timeout:
        print("Request timed out. Try again later.")
    except requests.RequestException as exc:
        print(f"Network/request failure: {exc}")
    except ValueError:
        print("The response was not valid JSON.")
    return None

def main():
    print("Fetching post 1")
    get_post(1)

    print("\\nFetching posts 1–3")
    for post_id in (1, 2, 3):
        post = get_post(post_id)
        if post:
            print(f"Post {post_id}: {post.get('title')}")

    print("\\nFetching collection")
    try:
        response = requests.get(f"{BASE_URL}/posts", timeout=10)
        if response.status_code == 429:
            print("Rate limit exceeded.")
        elif not response.ok:
            print(describe_status(response.status_code))
        else:
            posts = response.json()
            print(f"Number of posts: {len(posts)}")
            print("First five titles:")
            for post in posts[:5]:
                print("-", post.get("title"))
    except requests.Timeout:
        print("Collection request timed out.")
    except requests.RequestException as exc:
        print(f"Collection network/request failure: {exc}")

if __name__ == "__main__":
    main()
