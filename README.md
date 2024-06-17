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

## Files

- `app.py`: The main application file.
- `test_app.py`: Unit tests for the application.
- `Makefile`: Contains rules to install dependencies, run tests, and run the application.
- `requirements.txt`: A placeholder for dependencies (not required for this application).

## Makefile Rules

- `install`: Installs dependencies.
- `test`: Runs unit tests.
- `run`: Runs the application.

## How to Use

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/simple-arithmetic-app.git
    cd simple-arithmetic-app
    ```

2. Install dependencies:
    ```sh
    make install
    ```

3. Run the tests:
    ```sh
    make test
    ```

4. Run the application:
    ```sh
    make run
    ```

## License

This project is licensed under the MIT License.
