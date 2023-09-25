from os import environ
from dotenv import load_dotenv

load_dotenv()


class CoreSetting:
    PROJECT_NAME = environ.get("PROJECT_NAME")
    PROJECT_VERSION = environ.get("PROJECT_VERSION")
    DB_USER_NAME = environ.get("DB_USER_NAME")
    DB_PASSWORD = environ.get("DB_PASSWORD")
    DB_HOST = environ.get("DB_HOST")
    DB_PORT = environ.get("DB_PORT")
    DB_NAME = environ.get("DB_NAME")
    API_ROOT_PATH = environ.get("API_ROOT_PATH")
    SIGN_MESSAGE_TO_LOGIN = environ.get("SIGN_MESSAGE_TO_LOGIN")
    ETH_RPC = environ.get("ETH_RPC")
    JWT_SECRET_KEY = str(environ.get("JWT_SECRET_KEY"))
    JWT_ALGORITHM = str(environ.get("JWT_ALGORITHM"))
    JWT_EXPIRE_MINUTES = int(environ.get("JWT_EXPIRE_MINUTES"))
    DB_CONNECTION_STR = (
        f"mysql://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


Setting = CoreSetting()
