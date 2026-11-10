# API-Lab Final Project

## Run
1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python src/main.py`

## API documentation
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/{post_id}` and `/posts`
- **Method:** `GET`
- **Parameters:** `post_id` is the path identifier for one post; the collection endpoint has no required parameters.
- **Request body:** None for GET.
- **Response:** A post object with `userId`, `id`, `title`, `body`; `/posts` returns a list of such objects.
- **Possible errors:** 404, 429, 5xx, timeout, network/request failure, invalid JSON.
- **Authentication:** Not required for this public demonstration API. For protected APIs, load credentials from environment variables or `.env`, and exclude `.env` from Git.
- **Agent tool idea:** Expose `get_post(post_id)` as a tool with validated input and structured output.
