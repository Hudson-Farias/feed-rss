from dotenv import load_dotenv
from os import  getenv

load_dotenv()

ENV_PATH = getenv('ENV_PATH')
load_dotenv(ENV_PATH)

REDIS_HOST = getenv('REDIS_HOST')
REDIS_PASSWORD = getenv('REDIS_PASSWORD')
REDIS_PORT = getenv('REDIS_PORT')
