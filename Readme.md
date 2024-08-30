<!-- ABOUT THE PROJECT -->
## About The Project

Test automation project to play around with python + playwright framework and investigate playwright abilities.

## Built With

Used Playwright framework with playwright-pytest plugin.

* [Playwright](https://playwright.dev/python/)
* [Playwright pytest](https://playwright.dev/python/docs/test-runners)

<!-- GETTING STARTED -->
## Getting Started

First of all, we will create a virtual environment (venv), and after that - install dependencies from requirements.txt.

## Creating venv

* python
  ```sh
  python -m venv .venv
  ```

## Activate the virtual environment

* on windows
  ```sh
  .venv\Scripts\activate
  ```

* macOS/Linux
  ```sh
  source .venv/bin/activate
  ```
## Dependencies installation

After we have activated venv, we can start installing dependencies.

* Install dependencies from requirements.txt
  ```sh
  pip install -r requirements.txt
  ```

<!-- USAGE EXAMPLES -->
## Usage

At the moment we are able to run few test cases with API tests.
For testing we have created two test cases, and each of them is using different web applications for verifying API requests.

* [Restful-booker](https://restful-booker.herokuapp.com/apidoc/index.html) web application. We are adding "verbose" (-v) and "show print statemt tags" (-s) for additional invomation
  ```sh
  pytest tests/api/test_api_booking.py -v -s
  ```

* [Restful-api.dev](https://restful-api.dev/)
  ```sh
  pytest tests/api/test_api_dev.py -v -s
  ```



<!-- ROADMAP -->
## Roadmap

- [x] Create repo
- [x] Add base for paje-object pattern
- [x] Add few API test-cases
    - [x] Restful-api.dev
    - [x] Restful-booker
- [x] Add allure reporter
- [x] Create pipeline for github actions
- [x] Configure github pipeline for github CI
- [x] Add allure report configuration to pipeline: saving history; uploading results on separate github page
- [x] Add few UI e2e test cases
- [ ] Add test reporting to telegram bot in case if tests executed from github CI
- [ ] Add load test examples
- [ ] Add description for prometeus & grafana configuration


## Allure reporter
Allure reporter will save the test results in "reports" folder after test execution.
* Checking allure report results
  ```sh
  allure serve reports
  ```