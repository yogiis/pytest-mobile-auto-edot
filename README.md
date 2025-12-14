# EDOT Automation Framework

Mobile & Web Automation testing framework using Appium, Selenium, and Pytest.

## Project Structure

```
pytest-mobile-auto-edot/
├── mobile_automation/   # Android mobile testing (Appium)
├── web_automation/      # Web testing (Selenium)
├── venv/               # Virtual environment
└── README.md
```

## Quick Start

### Mobile Automation

```bash
cd mobile_automation
pip install -r requirements.txt
cp .env.example .env
appium
pytest
```

### Web Automation

```bash
cd web_automation
pip install -r requirements.txt
cp .env.example .env
pytest
```

## Running Tests with Reports

### HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

### Allure Report

```bash
# Install Allure
brew install allure

# Run tests
pytest --alluredir=reports/allure-results

# View report
allure serve reports/allure-results
```

## Configuration

Each automation module has:

- `.env.example` - Environment variables template
- `config/config.py` - Configuration management
- `conftest.py` - Pytest fixtures
- `.gitignore` - Git ignore patterns

## For More Details

- See `mobile_automation/README.md` for mobile-specific setup
- See `web_automation/README.md` for web-specific setup
