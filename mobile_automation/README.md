# Mobile Automation - EDOT eWork

Automated testing for EDOT eWork Android mobile app using Appium and pytest.

## Setup

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Configure environment:**

```bash
cp .env.example .env
# Edit .env with your device and credentials
```

3. **Start Appium server:**

```bash
appium
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
mobile_automation/
├── config/         # Configuration settings
├── pages/          # Page Object Models
│   ├── base_page.py
│   └── login_page.py
├── tests/          # Test cases
│   └── test_login.py
├── utils/          # Helper utilities
├── reports/        # Test reports (gitignored)
├── conftest.py     # Pytest fixtures
└── .env            # Environment variables (gitignored)
```

## Test Coverage

- ✅ Login with valid credentials
- ✅ Login page verification
- ✅ Appium driver setup for Android

## Configuration

Edit `.env` file:

- `APPIUM_SERVER_URL` - Appium server URL (default: http://127.0.0.1:4723)
- `ANDROID_DEVICE_NAME` - Android device name (default: emulator-5554)
- `ANDROID_APP_PACKAGE` - App package ID (default: id.edot.ework)
- `ANDROID_APP_ACTIVITY` - App activity (default: SplashScreenActivity)
- `IMPLICIT_WAIT` - Implicit wait timeout in seconds (default: 10)
- `EXPLICIT_WAIT` - Explicit wait timeout in seconds (default: 30)
- `TEST_COMPANY_ID` - Test company ID (default: 5049209)
- `TEST_USERNAME` - Test username (default: qatestsalesman)
- `TEST_PASSWORD` - Test password (default: it.QA2025)

## Prerequisites

- Android device or emulator running
- Appium server installed and running
- Python 3.8+
