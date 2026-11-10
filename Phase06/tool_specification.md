# API Tool Specification

## Task 24 — Define an API Tool
- **Tool name:** `get_post`
- **Description:** Retrieve one post by its numeric ID.
- **HTTP method:** `GET`
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/{post_id}`
- **Required inputs:** `post_id` (positive integer)
- **Optional inputs:** None
- **Expected output:** JSON object containing `userId`, `id`, `title`, and `body`
- **Possible errors:** 404 resource not found, 429 rate limit, 5xx server error, timeout, network/request failure
- **Authentication required:** No, for JSONPlaceholder's public demonstration endpoint

## Task 25 — Agent-Oriented Tool Interface
```json
{
  "name": "get_post",
  "description": "Retrieve a post by ID from JSONPlaceholder.",
  "parameters": {
    "type": "object",
    "properties": {
      "post_id": {"type": "integer", "description": "ID of the post to retrieve"}
    },
    "required": ["post_id"]
  }
}
```
- **Output fields:** `id`, `title`, `body`, `userId`
- **Error behavior:** Return a clear error for 404, 429, server errors, timeouts, and network failures. Do not expose secrets.
