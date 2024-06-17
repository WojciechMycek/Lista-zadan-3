# API Test Automation with curl

This repository contains a Python script that automates the testing of API endpoints using `curl`. The script sends HTTP GET requests to specified endpoints and verifies the HTTP response status and key elements in the JSON response.

## How to Use

1. Ensure you have Python installed on your machine.
2. Clone this repository.
3. Run the script using Python:
    ```sh
    python api_test.py
    ```

## Endpoints Tested

1. `https://jsonplaceholder.typicode.com/posts/1` - Checks for keys: `userId`, `id`, `title`, `body`
2. `https://jsonplaceholder.typicode.com/comments?postId=1` - Checks for keys: `postId`, `id`, `name`, `email`, `body` in each comment
3. `https://jsonplaceholder.typicode.com/users/1` - Checks for keys: `id`, `name`, `username`, `email`

## Example Output

Test 1: PASSED - Passed
Test 2: PASSED - Passed
Test 3: PASSED - Passed
