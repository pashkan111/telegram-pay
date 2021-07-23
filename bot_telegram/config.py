import os
import dotenv


dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
EMAIL_PASSWORD = os.getenv("email_password")
HOST = os.getenv("HOST")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
