import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_HOST = os.getenv("MYSQL_HOST")
DATABASE_PORT = 3306
DATABASE_NAME = os.getenv("MYSQL_DATABASE")
DATABASE_USER = os.getenv("MYSQL_USER")
DATABASE_PASSWORD = os.getenv("MYSQL_PASSWORD")
PIHOLE_API_KEY = os.getenv("PIHOLE_API_KEY")
