import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
    ANDROID_DEVICE_NAME = os.getenv("ANDROID_DEVICE_NAME", "emulator-5554")
    ANDROID_APP_PACKAGE = os.getenv("ANDROID_APP_PACKAGE", "id.edot.ework")
    ANDROID_APP_ACTIVITY = os.getenv("ANDROID_APP_ACTIVITY", "id.edot.onboarding.ui.splash.SplashScreenActivity")
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "30"))
    TEST_COMPANY_ID = os.getenv("TEST_COMPANY_ID", "5049209")
    TEST_USERNAME = os.getenv("TEST_USERNAME", "qatestsalesman")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "it.QA2025")
