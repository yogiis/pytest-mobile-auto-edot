import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    
    BASE_URL = os.getenv("BASE_URL", "https://esuite.edot.id")
    
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "30"))
    
    MAXIMIZE_WINDOW = os.getenv("MAXIMIZE_WINDOW", "true").lower() == "true"
    
    TEST_EMAIL = os.getenv("WEB_TEST_EMAIL", "masyogikalem@gmail.com")
    TEST_PASSWORD = os.getenv("WEB_TEST_PASSWORD", "R4h4si4lup@")
