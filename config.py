from dotenv import load_dotenv
load_dotenv()
from os import environ as env


FLASK_CONFIG = {
    #
}
FLASK_SECRET_KEY = env.get("FLASK_SECRET_KEY")
