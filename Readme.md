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

* [Restful-booker](https://restful-booker.herokuapp.com/apidoc/index.html) web application
We are adding "verbose" (-v) and "show print statemt tags" (-s) for additional invomation
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
- [ ] Add few UI e2e test cases


## Allure reporter
Allure reporter will save the test results in "reports" folder after test execution.
* Checking allure report results
  ```sh
  allure serve reports
  ```

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Playwright-pytest-url]: https://playwright.dev/python/docs/test-runners
[Pytest-icon]: https://miro.medium.com/v2/resize:fit:800/1*F2BHs6p9erpiGKro5Pg1uQ.png
[Playwright-url]: https://playwright.dev/python/
[Playwright-icon]: https://upload.wikimedia.org/wikipedia/commons/7/75/Playwright_Logo.svg