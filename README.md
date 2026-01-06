# HMCTS Test Automation Framework – Login (BDD)

## Overview

This repository contains a UI test automation framework developed as part of the **HMCTS Senior Developer in Test technical challenge**.

The framework demonstrates a clean, maintainable, and scalable approach to automating web application login functionality using **Python**, **pytest-bdd**, and **Playwright**.

---

## Application Under Test

- **URL:** https://bstackdemo.com

---

## Objectives

- Automate critical login user journeys
- Cover positive and negative authentication scenarios
- Demonstrate good automation design and engineering practices
- Provide a framework that is easy to understand and extend

---

## Test Coverage

### Login Scenarios
- Successful login with valid credentials
- Login failure with invalid credentials
- Authentication error validation

---

## Technology Stack

| Category | Tool |
|--------|------|
| Language | Python |
| Test Runner | pytest |
| BDD | pytest-bdd |
| Automation | Playwright |
| Design Pattern | Page Object Model (POM) |
| Reporting | pytest-html / Allure |
| CI Readiness | GitHub Actions |
| IDE | VS Code |

---

## Project Structure

hmcts-test-automation-challenge/
├── config/ # Environment and configuration files
├── features/ # Gherkin feature files
├── pages/ # Page Object Model classes
├── steps/ # BDD step definitions
├── tests/ # Test entry points
├── utils/ # Shared utilities (browser setup, logging)
├── reports/ # Test execution reports
├── pytest.ini
├── requirements.txt
└── README.md


---

## Design Approach

- **BDD (pytest-bdd)** is used to describe user journeys in a readable format
- **Page Object Model** separates UI interactions from test behaviour
- Step definitions are kept thin and delegate logic to Page Objects
- Playwright’s built-in waiting mechanisms are used to reduce flakiness
- Shared technical concerns are isolated in utility modules

---

## Prerequisites

- Python 3.9+
- pip
- Git

---

## Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd hmcts-test-automation-challenge

2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows

3. Install dependencies
pip install -r requirements.txt
playwright install
```

## Running the Tests
- Run all tests:
```bash
pytest -v
```

## Run tests in headed mode:
``` bash
pytest --headed
```

## Reporting
- HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

- Allure Report 
``` bash
pytest --alluredir=reports/allure
allure serve reports/allure
```
– Screenshots are captured on test failure to support debugging.

## CI/CD Readiness

– The framework is CI-ready and can be integrated with a CI pipeline (for example, GitHub Actions) to execute tests headlessly on each commit.

## Future Enhancements

- Parallel execution using pytest-xdist

- API and UI hybrid testing

- Dockerised execution

- Visual regression testing

- Enhanced logging and metrics

## Notes

- This repository is intentionally name-blind in line with the Civil Service recruitment process

- The focus is on quality, clarity, and maintainability rather than test volume
