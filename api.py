import os
import json

def send_request(url):
    response = os.popen(f"curl -s -w 'HTTPSTATUS:%{{http_code}}' {url}").read()
    
    try:
        status_code = response.split('HTTPSTATUS:')[-1]
        body = response.replace(f'HTTPSTATUS:{status_code}', '').strip()
        return int(status_code), body
    except ValueError:
        return None, None

def validate_response(status_code, body, required_keys):
    if status_code != 200:
        return False, "Invalid status code"

    try:
        json_body = json.loads(body)
    except json.JSONDecodeError:
        return False, "Invalid JSON response"

    if isinstance(json_body, list):
        for item in json_body:
            for key in required_keys:
                if key not in item:
                    return False, f"Missing key: {key} in one of the list items"
    else:
        for key in required_keys:
            if key not in json_body:
                return False, f"Missing key: {key}"

    return True, "Passed"

def test_endpoint(url, required_keys):
    status_code, body = send_request(url)
    result, message = validate_response(status_code, body, required_keys)
    return result, message

def main():
    tests = [
        {
            "url": "https://jsonplaceholder.typicode.com/posts/1",
            "required_keys": ["userId", "id", "title", "body"]
        },
        {
            "url": "https://jsonplaceholder.typicode.com/comments?postId=1",
            "required_keys": ["postId", "id", "name", "email", "body"]
        },
        {
            "url": "https://jsonplaceholder.typicode.com/users/1",
            "required_keys": ["id", "name", "username", "email"]
        }
    ]

    for i, test in enumerate(tests, 1):
        result, message = test_endpoint(test["url"], test["required_keys"])
        print(f"Test {i}: {'PASSED' if result else 'FAILED'} - {message}")

if __name__ == "__main__":
    main()
