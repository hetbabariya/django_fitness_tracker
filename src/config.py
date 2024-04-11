import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    EMAIL_FROM=os.environ["EMAIL_FROM"]
    EMAIL_PASS=os.environ["EMAIL_PASS"]
    JWT_ACCESS_TOKEN_LIFETIME=os.environ["JWT_ACCESS_TOKEN_LIFETIME"]
    JWT_REFRESH_TOKEN_LIFETIME=os.environ["JWT_REFRESH_TOKEN_LIFETIME"]