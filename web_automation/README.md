# Web Automation - EDOT

Automated testing for EDOT web application using Selenium WebDriver and pytest.

## Setup

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Configure environment:**

```bash
cp .env.example .env
# Edit .env with your credentials
```

## Run Tests

**Run all tests:**

```bash
pytest tests/ -v
```

**Run with Allure report:**

```bash
pytest tests/ -v --alluredir=reports/allure-results
allure serve reports/allure-results
```

**Run with HTML report:**

```bash
pytest tests/ -v --html=reports/report.html --self-contained-html
```

## Project Structure

```
web_automation/
├── config/         # Configuration settings
├── pages/          # Page Object Models
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   └── company_registration_page.py
├── tests/          # Test cases
│   └── test_company_registration.py
├── utils/          # Helper utilities
├── reports/        # Test reports (gitignored)
├── conftest.py     # Pytest fixtures
└── .env            # Environment variables (gitignored)
```

## Test Coverage

- ✅ Company Registration Flow (Step 1, 2, 3)
- ✅ Login with email/password
- ✅ Navigation and form filling
- ✅ Dropdown selections
- ✅ Multi-step workflow

## Configuration

Edit `.env` file:

- `BROWSER` - Browser type (default: chrome)
- `HEADLESS` - Run browser in headless mode (default: false)
- `BASE_URL` - Application URL (default: https://esuite.edot.id)
- `IMPLICIT_WAIT` - Implicit wait timeout in seconds (default: 10)
- `EXPLICIT_WAIT` - Explicit wait timeout in seconds (default: 30)
- `MAXIMIZE_WINDOW` - Maximize browser window (default: true)
- `WEB_TEST_EMAIL` - Login email
- `WEB_TEST_PASSWORD` - Login password

## Prerequisites

- Python 3.8+
- Chrome browser installed
- ChromeDriver (installed automatically via webdriver-manager)
