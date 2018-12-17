from dotenv import load_dotenv
import os

load_dotenv()


class Configuration:
    "Base configuratio class"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    TESTING = False
    DEBUG = False


class Development(Configuration):
    """Decelopment class"""
    DEBUG = True


class Testing(Development):
    """Testing configuration class"""
    TESTING = True


config = {
    "TESTING": Testing,
    "DEVELOPMENT": Development
}
default_config = config["DEVELOPMENT"]
